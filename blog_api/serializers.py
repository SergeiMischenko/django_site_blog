from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ("id", "author", "title", "body", "created")
