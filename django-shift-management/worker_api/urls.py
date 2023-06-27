from django.urls import include, path
from rest_framework import routers
from .views import WorkerViewSet, ShiftViewSet


router = routers.DefaultRouter()
router.register(r'workers', WorkerViewSet)
router.register(r'shifts', ShiftViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
