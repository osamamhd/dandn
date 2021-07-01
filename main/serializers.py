from rest_framework import serializers

from .models import Story

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = (
            "id", 
            "title",
            "body",
            "truncateBody",
            "dop",
            "get_absolute_url",
            "type_of_story",
            "points"
        )