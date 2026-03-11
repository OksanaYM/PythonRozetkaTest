from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.response import Response

from apps.core.permissions.is_admin_or_allow_any_post_permission import IsAdminOrAllowAnyPost
from apps.core.permissions.is_superuser_permission import IsSuperUser
from apps.user.serializers import UserSerializer

UserModel = get_user_model()

class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrAllowAnyPost,)



class UserToAdminView(GenericAPIView):
    permission_classes = (IsSuperUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_staff:
            user.is_staff = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AdminToUserView(GenericAPIView):
    permission_classes = (IsSuperUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)