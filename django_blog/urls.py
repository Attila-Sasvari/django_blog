from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from django.contrib.sitemaps.views import sitemap

from accounts import views as acc_views
from .feeds import LatestPostsFeed
from .sitemaps import BlogSitemap


urlpatterns = [
    path('accounts/logout', acc_views.logout, name='logout'),
    path('accounts/authors', acc_views.authors, name='authors'),
    path('accounts/edit', acc_views.update_profile, name='update_profile'),
    path('accounts/register', acc_views.register, name='register'),
    path('accounts/profile', acc_views.view_profile, name='view_profile'),
    path('accounts/edit', acc_views.update_profile, name='update_profile'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path('admin/', admin.site.urls),
    path('dashboard', include('dashboard.urls')),
    path('api/v1/', include('api.urls')),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path("file-upload/", include('upload.urls')),
    path("sitemap.xml", sitemap, {"sitemaps": {
         'blog': BlogSitemap}}, name="sitemap"),
    path('', include('blog.urls')),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
