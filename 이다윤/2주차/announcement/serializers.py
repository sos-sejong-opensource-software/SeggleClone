from rest_framework import serializers
from .models import Announcement, User

########################
"""

serializer가 무슨 역할을 하는지 반드시 파악해주세요.
views에서 serializer로 무엇을 하는지 반드시 파악해주시고, 왜 이렇게 코드를 작성했을까 생각해주세요.

"""
########################


class UsernameSerializer(serializers.ModelSerializer):
    """
    user의 id, username 정보를 다루는 serializer
    """
    class Meta:
        model = User
        fields = ['id', 'username']

class AnnouncementSerializer (serializers.ModelSerializer):
    """
    announcement의 모든 정보를 다루는 serializer
    """
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'context', 'created_user', 'created_time', 'last_modified', 'visible', 'important']

class AnnouncementInfoSerializer(serializers.ModelSerializer):
    """
    announcement의 정보(일반 user에게 보일 정보)를 다루는 serializer 
    """
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'created_time', 'last_modified', 'visible', 'important']

class AnnouncementCheckSerializer(serializers.ModelSerializer):
    ########################
    """
    announcement의 visible, important 정보만을 다루는 serializer
    """
    class Meta:
        model = Announcement
        fields = ['visible', 'important']
    ########################