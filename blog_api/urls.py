from django.urls import include, path, re_path

from .views import PostDetail, PostList, UserPostList

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
    path("", PostList.as_view(), name="post_list"),
    re_path("^user/(?P<id>.+)/$", UserPostList.as_view()),
    path("api-auth/", include("rest_framework.urls")),
]
