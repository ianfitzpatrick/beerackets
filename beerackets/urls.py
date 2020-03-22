from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
import notifications.urls
from .views import Home

admin.site.site_header = 'Beerackets Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(
        '^inbox/notifications/',
        include(notifications.urls,
            namespace='notifications')
    ),
    path('', Home.as_view(), name='home')
]
