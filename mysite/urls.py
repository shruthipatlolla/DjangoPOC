from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
     
     url(r'^testData/', include('testData.urls')),
     url(r'^admin/', admin.site.urls),
]
