from django.contrib.auth import get_user_model
from django.db import models

from cms.model_helper import TimedModel


User = get_user_model()

class ResourceType(TimedModel):
    name = models.CharField(max_length=255)
    status = models.IntegerField(
        default=1,
        choices=(
            (1, 'Active'), (0, 'Inactive')
        )
    )

    def __str__(self):
        return self.name
        

class Resource(TimedModel):
    reference_id = models.CharField(max_length=255)
    link = models.TextField(blank=True, null=True)
    resource_type = models.ForeignKey(ResourceType)
    created_by = models.ForeignKey(User)

    def __str__(self):
        return self.reference_id
