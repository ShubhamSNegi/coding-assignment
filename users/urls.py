from rest_framework import routers
from django.urls import path, re_path
from .views import AuthViewSet, UserApis

router = routers.DefaultRouter(trailing_slash=False)
router.register('auth', AuthViewSet, basename='auth')

urlpatterns = [
    re_path(r'(?P<pk>[0-9]+)/$', UserApis.as_view())
]
urlpatterns += router.urls