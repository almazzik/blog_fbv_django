from django.urls import path, re_path
from .views import PostDetail, PostList, UserPostList
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list"),
    re_path('^user/(?P<id>.+)/$', UserPostList.as_view()),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]