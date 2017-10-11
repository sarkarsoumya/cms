from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings

from cms.model_helper import TimedModel


User = get_user_model()

class ResourceType(TimedModel):
    name = models.CharField(max_length=50)
    status = models.IntegerField(
        default=1,
        choices=(
            (1, 'Active'), (0, 'Inactive')
        )
    )
    order_by = models.IntegerField(default=0)
    mime_type = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.name
        

class Resource(TimedModel):
    subject = models.CharField(max_length=255)
    reference_id = models.CharField(max_length=255)
    link = models.TextField(blank=True, null=True)
    resource_type = models.ForeignKey(ResourceType)
    created_by = models.ForeignKey(User, editable=False)

    def __str__(self):
        return self.subject
        

class File(TimedModel):
    resource = models.FileField(upload_to=settings.MEDIA_URL)
    slug = models.SlugField()

    def __str__(self):
        return self.slug


class Article(TimedModel):
    resource = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.slug