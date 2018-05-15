from django.contrib import admin
from django.urls import path, include
from django.conf import settings

import profiles.urls
from profiles.views import HomePage
import viewschapter.urls
import formschapter.urls
import sightings.urls

admin.site.site_header = "SuperBook Secret Area"

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include(profiles.urls)),
    path('sightings/', include(sightings.urls)),
    path('', include(viewschapter.urls, namespace='viewschapter')),
    path('', include(formschapter.urls, namespace='formschapter')),
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
