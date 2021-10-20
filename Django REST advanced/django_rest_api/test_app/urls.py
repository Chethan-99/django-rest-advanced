from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import SimpleAPIView, StaticView
from django.conf.urls.static import static
from django .conf import settings


router = DefaultRouter()
router.register("static", StaticView)


urlpatterns = [
    path('product',SimpleAPIView.as_view()),
    path("", include(router.urls))
] + static(settings.MEDIA_URL, document_rooot=settings.MEDIA_ROOT)
