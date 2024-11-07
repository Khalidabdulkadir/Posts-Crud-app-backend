from rest_framework import serializers
from .models import Post

class Postserialisers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','body','date']