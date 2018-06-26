from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import HomeView

#The format_suffix_pattern allows us to specify the data format (raw json or even html) when we use the URLs. It appends the format to be used to every URL in the pattern.

urlpatterns = [
      url(r'^bucketlists/$', HomeView.as_view(), name="home"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
