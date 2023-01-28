from django.urls import re_path
from .views import CompanyApis, CompanyCreateView


urlpatterns = [
    re_path(r'(?P<pk>[0-9]+)/$', CompanyApis.as_view()),
    re_path('', CompanyCreateView.as_view())
]
