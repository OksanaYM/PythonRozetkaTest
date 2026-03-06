from django.urls import path

from apps.user.views import UserListCreateView, UserToAdminView, AdminToUserView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user-list-create'),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name='user-to-admin'),
    path('/<int:pk>/admin_to_user', AdminToUserView.as_view(), name='admin-to-user'),
]