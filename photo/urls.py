from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from authentication import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('albums/', include('album.urls')),
    path('picture/', include('picture.urls')),
    path('authors/', include('author.urls')),
    path('category/', include('category.urls')),
    path('accounts/', include('authentication.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', auth_views.profile, name='profile'),
    path('profile/edit/', auth_views.edit, name='profile_edit'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
