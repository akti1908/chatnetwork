from rest_framework import viewsets, generics
from myusers.models import My_user
from myusers.serializers import My_user_Serializer


class UserView(viewsets.ModelViewSet):
    queryset = My_user.objects.all()
    serializer_class = My_user_Serializer


class MyUserDetail(generics.RetrieveAPIView):
    queryset = My_user.objects.all()
    serializer_class = My_user_Serializer





# class ChatView(viewsets.ModelViewSet):
#     queryset = Chat.objects.all()
#     serializer_class = ChatSerializer


# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import User
# from .serializers import UserSerializer
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
