
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^secretadmin/', admin.site.urls),
    url(r'^auth/', include('myauth.urls')),
    url(r'^', include('integral.urls', namespace='integral')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
