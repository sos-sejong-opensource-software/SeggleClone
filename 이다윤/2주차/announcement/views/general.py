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
    # page size 설정
    page_size_query_param = 'limit'

class AnnouncementView(APIView, PaginationHandlerMixin):
    # 모두 접근 가능
    permission_classes = [AllowAny]
    # pagination style 설정
    pagination_class = BasicPagination

    # 04-01 공지 리스트 전체 조회
    def get(self, request):
        announcements = Announcement.objects.exclude(visible=False)
        keyword = request.GET.get('keyword', '')
        if keyword:
            announcements = announcements.filter(title__icontains=keyword)
        # page: 요청된 페이지의 데이터만 포함하는 object. (반복 가능한 object)
        page = self.paginate_queryset(announcements)
        if page is not None:
            # pagination이 끝나지 않는다면 get_paginated_response 는 주어진 data 에 대하여 page style 을 매긴 Response object 를 반환한다
            serializer = self.get_paginated_response(AnnouncementInfoSerializer(page, many=True).data)
        else:
            # pagination이 끝난다면
            serializer = AnnouncementInfoSerializer(announcements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnnouncementDetailView(APIView):
    # 04-02 announcement_id인 announcement 조회
    permission_classes = [AllowAny]
    def get(self, request, announcement_id):
        announcement = get_announcement(announcement_id)
        serializer = AnnouncementSerializer(announcement)
        return Response(serializer.data)