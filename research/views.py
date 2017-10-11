from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core import serializers

from django.contrib.auth.models import User
from cms.helper import handle_uploaded_file
from .models import ResourceType, Resource, File, Article
from .serializers import ResourceSerializer



@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def index(request, id=None):
    """ 
    Return a list of all resources.
    """

    if id is None:
        resource = Resource.objects.select_related()
    else:
        resource = Resource.objects.select_related().filter(pk=id)

    serializer = ResourceSerializer(resource, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def upload(request):
    """
    Save all file types and/or text
    """
    file_content = request.FILES.get('content', False)

    resource = Resource()
    resource.subject = request.POST.get('subject')
    resource.created_by = request.user
    resource_type = None

    if file_content:
        for type in ResourceType.objects.order_by('order_by').exclude(mime_type=""):
            if (type.mime_type is not None) and (resource_type is None):
                if (type.mime_type in file_content.content_type):
                    resource_type = type
        # handle_uploaded_file(file_content)
        file = File(resource=file_content)
        file.save()
        
        resource.reference_id = file.id
        resource.link = file.resource
        
    else:
        print(request)
        resource.resource_type = ResourceType.objects.filter(pk=7)[0]
        article = Article(resource=request.POST.get('content'))
        article.save()

    resource.resource_type = resource_type
    resource.save()

    return Response(ResourceSerializer(resource).data)
