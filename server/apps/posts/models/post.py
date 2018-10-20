import uuid
from django.db import models
from django.conf import settings


class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_by',
    )

    liked_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_by',
    )

    heading = models.CharField(
        max_length=128,
        blank=False,
        null=False,
    )

    text = models.TextField(
        blank=False,
        null=False,
    )

    class Meta:
        app_label = 'posts'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.created_by.get_full_name() + self.heading
