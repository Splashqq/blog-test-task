from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from apps.auth import GlobalAuth
from apps.post.api import router as post_router
from config import settings

api = NinjaAPI(urls_namespace="Blog API", docs_url="/docs", auth=GlobalAuth())

api.add_router("/", post_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
