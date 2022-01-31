from django.conf import settings
from django.contrib import admin
from django.urls import path
from strawberry.django.views import AsyncGraphQLView

from project.schema import schema


if settings.DEBUG:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('graphql/', AsyncGraphQLView.as_view(schema=schema))
    ]
else:
    urlpatterns = [
        # Safe urls grabbed from .env
    ]