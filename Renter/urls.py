from django.conf.urls import patterns, url, include

from Renter import views
from Renter.renterapi import RenterResource

entry_resource = RenterResource()
# maps urls
urlpatterns = patterns('',
    url(r'^(?P<renter_id>\d+)/details$', views.showdetails, name='showdetails'),
    url(r'^(?P<renter_id>\d+)/details/(?P<rentfor_year>\d+)$', views.showRentDetailsForyear, name='showRentDetailsForyear'),
    url(r'^(?P<houseowner_id>\d+)/addnew$', views.addrenterinfo, name='addrenterinfo'),
    url(r'^(?P<renter_id>\d+)/edit$', views.editrenterinfo, name='editrenterinfo'),
    url(r'^(?P<renter_id>\d+)/delete$', views.deleterenterinfo, name='deleterenterinfo'),
    url(r'^(?P<flag>\d+)/submit$', views.submitrentinfo, name='submitrentinfo'),
    (r'^renterapi/', include(entry_resource.urls)),
    #url(r'^HOspcf/(?P<houseowner_id>\d+)/$', views.detail, name='detail')
)