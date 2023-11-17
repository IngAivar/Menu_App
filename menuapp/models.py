from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=255, null=True, blank=True)
    named_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        if self.url:
            return self.url
        elif self.named_url:
            return reverse(self.named_url)
        else:
            return '#'
