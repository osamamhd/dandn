from django.utils import timezone
from django.db import models
from autoslug import AutoSlugField

TYPES = (
    ('dream', 'Dream'),
    ('nightmare', 'Nightmare')
)

class Story(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    body = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    type_of_story = models.CharField(max_length=20, choices=TYPES, default='dream')
    points = models.IntegerField(default=0)

    class Meta:
        ordering = ["-points"]

    def __str__(self):
        return self.title