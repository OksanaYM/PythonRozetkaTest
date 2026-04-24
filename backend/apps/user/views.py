import os

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.core.permissions.is_admin_or_allow_any_post_permission import IsAdminOrAllowAnyPost
from apps.core.permissions.is_superuser_permission import IsSuperUser
from apps.user.serializers import UserSerializer
from apps.user.services.user_service import UserService

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

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
        user_service = UserService(user)
        user_service.to_admin()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AdminToUserView(GenericAPIView):
    permission_classes = (IsSuperUser,)

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        user_service = UserService(user)
        user_service.to_user()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserEmailTestView(GenericAPIView):
    permission_classes = (AllowAny,)
    def get(self, *args, **kwargs):
        template = get_template('test_email_rozetka.html')
        html_content = template.render({'name': 'Oksana'})
        msg = EmailMultiAlternatives(
            subject='Email Rozetka Test',
            from_email=os.environ.get('EMAIL_HOST_USER'),
            to=['ok.moyseyivna@ukr.net', 'moyseyivna@ukr.net'],
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        return Response({'message': 'Email Rozetka Test sent'}, status=status.HTTP_200_OK)