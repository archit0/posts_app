from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.posts.models import Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(
        read_only=True,
        required=False,
    )

    liked_by = serializers.PrimaryKeyRelatedField(
        many=True,
        required=False,
        queryset=User.objects.all(),
    )

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
