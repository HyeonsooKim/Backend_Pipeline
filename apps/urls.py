from django.urls import path, include

urlpatterns = [
    path('users/', include('apps.user.urls')),
    path('boards/', include('apps.board.urls')),
]