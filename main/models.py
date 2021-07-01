from django.utils import timezone
from django.db import models
from autoslug import AutoSlugField

TYPES = (
    ('dream', 'Dream'),
    ('nightmare', 'Nightmare')
)

class Story(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique_with='pub_date__month')
    body = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    type_of_story = models.CharField(max_length=20, choices=TYPES, default='dream')
    points = models.IntegerField(default=0)

    class Meta:
        ordering = ["-points"]

    def __str__(self):
        return self.title

    def dop(self):
        return self.pub_date.strftime('%b %d, %Y')

    def truncateBody(self):
        trancateBy = 200
        if len(f'{self.body}') > trancateBy:
            return f'{self.body}'[:trancateBy] + '...'
        else:
            return f'{self.body}'

    def get_absolute_url(self):
        return f'/{self.slug}/'