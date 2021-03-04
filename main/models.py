from django.utils import timezone
from django.db import models
from autoslug import AutoSlugField

class Story(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    body = models.TextField(blank=True)
    pub_date = models.DateField(default=timezone.now().strftime("%m-%d-%y"))
    points = models.IntegerField(default=0)

    class Meta:
        ordering = ["-points"]

    def __str__(self):
        return self.title