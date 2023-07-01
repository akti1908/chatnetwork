from rest_framework import serializers
from myusers.models import My_user
from posts.models import Post
from posts.serializers import PostSerializer


class My_user_Serializer(serializers.ModelSerializer):
    posts = serializers.SerializerMethodField()

    class Meta:
        model = My_user
        fields = ['id', 'nickname', 'email', 'password', 'posts']

    def get_posts(self, obj):
        posts = Post.objects.filter(author=obj)
        serializer = PostSerializer(posts, many=True)
        return serializer.data




