from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from blog import settings
from post.api import GlobalAuth
from post.api import router as blog_router

api = NinjaAPI(urls_namespace="Blog API", docs_url="/docs", auth=GlobalAuth())

api.add_router("/blog/", blog_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
