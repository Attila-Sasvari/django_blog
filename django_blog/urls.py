from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# for GraphQL
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from accounts import views as acc_views

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/authors', acc_views.authors, name='authors'),
    path('accounts/fixme', acc_views.fixme, name='fixme'),
    path('accounts/edit', acc_views.update_profile, name='update_profile'),
    path('accounts/register', acc_views.register, name='register'),
    path('accounts/profile', acc_views.view_profile, name='view_profile'),
    path('accounts/edit', acc_views.update_profile, name='update_profile'),
    path('api/v1/', include('api.urls')),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path("file-upload/", include('upload.urls')),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
