
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from myusers.views import UserView, MyUserDetail
from posts.views import PostView
from django.urls import path
from posts.views import ImageView
from likes.views import LikeViewSet
from chat.views import ChatViewSet

urlpatterns = [
]

router_user = routers.SimpleRouter()
router_user.register(r'user', UserView)

router_post = routers.SimpleRouter()
router_post.register(r'post', PostView)

router_chat = routers.SimpleRouter()
router_chat.register(r'chat', ChatViewSet)


router_like = routers.SimpleRouter()
router_like.register(r'likes', LikeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router_post.urls)),
    path('', include(router_like.urls)),
    path('', include((router_user.urls))),
    path('images/', ImageView.as_view(), name='image-upload'),
    path('user/<int:pk>/', MyUserDetail.as_view(), name='user'),
    path('', include((router_chat.urls))),
]
