from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
			url(r'^all/sort_by_pincode', 'pincode.views.pincodes_pincode'),
			url(r'^all/sort_by_state', 'pincode.views.pincodes_state'),
			url(r'^all/sort_by_district', 'pincode.views.pincodes_district'),
			url(r'^all/', 'pincode.views.pincodes'),
			url(r'^get/(?P<pincode_id>\d+)/$', 'pincode.views.pincode_single'),
			url(r'^create/', 'pincode.views.create'),
			url(r'^update/', 'pincode.views.update'),
			#url(r'^search/$', 'pincode.views.search_pincodes'),
			#url(r'^search_items/', 'pincode.views.search_items'), 


]