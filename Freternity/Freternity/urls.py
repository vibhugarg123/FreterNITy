from django.conf.urls import include , url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import login_view
from accounts.views import logout_view
from accounts.views import register_view
from Posts.views import home_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',login_view,name='login'),
    url(r'^logout/',logout_view,name='logout'),
    url(r'^register/',register_view,name='register'),
    url(r'^posts/', include("Posts.urls", namespace='posts')),
    url(r'^$', home_page, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
