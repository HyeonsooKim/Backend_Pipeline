from django.urls import path, include

urlpatterns = [
    path('users/', include('apps.user.urls')),
    path('boards/', include('apps.board.urls')),
    path('statistic/', include('apps.statistic.urls')),
    path('data/', include('apps.data.urls')),
]