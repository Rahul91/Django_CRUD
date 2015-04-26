from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pincode/', include('pincode.urls')),
    #url(r'^ajax_search/',include('ajax_search.urls')),
    #url(r'^home/', 'pincode.views.hello'),
    #url(r'^home_template/', 'pincode.views.hello_template'),
    #url(r'^home_template_again/', 'pincode.views.hello_template_again'),
    #url(r'^home_template_aga/', 'pincode.views.hello_temp'),

    #url(r'^admin/', include(admin.site.urls)),

]
