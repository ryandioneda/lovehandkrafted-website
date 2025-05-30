"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView)

API_PREFIX = "api"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f"accounts/", include("allauth.urls")),

    path(f"{API_PREFIX}/schema/", SpectacularAPIView.as_view(), name="api-schema"),

    path(f"{API_PREFIX}/docs/", SpectacularSwaggerView.as_view(url_name="api-schema"), name="api-docs"),

    path(f"{API_PREFIX}/authentication/", include("src.apps.authentication.api.urls")),

    path(f"{API_PREFIX}/newsletter/", include("apps.newsletter.api.urls")),

    path(f"{API_PREFIX}/products/", include("apps.products.api.urls")),
]
