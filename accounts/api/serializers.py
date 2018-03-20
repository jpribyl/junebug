from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.urls import reverse_lazy

User = get_user_model()


# public display user serializer
class UserDisplaySerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()


    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'follower_count',
            'url',
            # 'email',
        ]

    # you can define and run methods inside the serializer
    # this method must have the same name as the SerializerMethodField()
    def get_follower_count(self, obj):
        print(obj.username)
        return 0


    def get_url(self, obj):
        return reverse_lazy(
            'profiles-detail', 
            kwargs={'username': obj.username})
