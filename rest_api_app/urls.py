from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import HomeView,DetailsView,DoctorListView,DoctorListDetailsView,HomePageView,get_data

from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static 

#The format_suffix_pattern allows us to specify the data format (raw json or even html) when we use the URLs. It appends the format to be used to every URL in the pattern.

urlpatterns = [
      url(r'^$',HomePageView.as_view(),name="homepage"),   
      url(r'^data/$',get_data,name="data"),         
      url(r'^auth/',include('rest_framework.urls',namespace='rest_framework')), 
      url(r'^doctors/$', DoctorListView.as_view(), name="doctor"),
      url(r'doctors/(?P<pk>[0-9]+)/$',DoctorListDetailsView.as_view(), name="doctor_details"),      
      url(r'^bucketlists/$', HomeView.as_view(), name="home"),
      url(r'^bucketlists/(?P<pk>[0-9]+)/$',DetailsView.as_view(), name="details"),
      url(r'^get-token/', obtain_auth_token),


]+static(settings.MEDIA_URL,documents_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
