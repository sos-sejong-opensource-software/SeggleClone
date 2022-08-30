from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.pagination import PageNumberPagination #pagination
from utils.pagination import PaginationHandlerMixin #pagination
from ..models import Announcement
from ..serializers import AnnouncementSerializer, AnnouncementInfoSerializer
from utils.get_obj import *
from rest_framework.permissions import AllowAny

class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'

class AnnouncementView(APIView, PaginationHandlerMixin):
    # pagination
    permission_classes = [AllowAny]
    pagination_class = BasicPagination

    # 04-01 공지 리스트 전체 조회
    def get(self, request):
        announcements = Announcement.objects.exclude(visible=False)
        ########################
        """
        
        코드 작성 (주석된 것을 참고하여 코드 작성. 작성했다면 주석을 해제하고 작동이 되는지 확인해주세요.)
        
        """
        ########################
        # return Response(serializer.data, status=status.HTTP_200_OK)


class AnnouncementDetailView(APIView):
    # 04-02 announcement_id인 announcement 조회
    permission_classes = [AllowAny]
    def get(self, request, announcement_id):
        ########################
        """
        
        코드 작성 (주석된 것을 참고하여 코드 작성. 작성했다면 주석을 해제하고 작동이 되는지 확인해주세요.)
        
        """
        ########################
        # return Response(serializer.data)