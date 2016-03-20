from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from mufc import views

urlpatterns = [
    url(r'^players/$', views.MufcList.as_view(), name='mufc-list'),
    url(r'^players/(?P<pk>[0-9]+)/$', views.MufcDetail.as_view(), name='mufc-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)