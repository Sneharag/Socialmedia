from django.shortcuts import render

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from socialapp.serializers import UserSerializer,PostSerializer

from socialapp.models import Post

from rest_framework import authentication,permissions

class SignUpView(CreateAPIView):

    serializer_class=UserSerializer

class PostListCreateView(ListAPIView,CreateAPIView):

    queryset=Post.objects.all()

    serializer_class=PostSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):

        serializer.save(owner=self.request.user)

class PostRetrieveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=PostSerializer

    queryset=Post.objects.all()

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    

