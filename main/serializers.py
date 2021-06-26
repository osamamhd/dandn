from rest_framework import serializers

from .models import Story

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = (
            "id", 
            "title",
            "body",
            "get_absolute_url",
            "pub_date",
            "type_of_story",
            "points"
        )