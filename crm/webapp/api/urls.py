from django.urls import path, include
from webapp.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserViewSet, basename='user')  # No need to use basename unless necessary
router.register('records', views.RecordViewSet, basename='record')

urlpatterns = [
    path('', include(router.urls)),  # Ensure the viewset URLs are included under 'api/'
]
