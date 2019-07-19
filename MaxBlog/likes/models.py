from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes',  on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(_('Object id'))
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return "Like for {0} {1}".format(self.content_type.model, self.object_id)

    class Meta:
        verbose_name = _('Like')
        verbose_name_plural = _('Likes')