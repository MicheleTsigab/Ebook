from .views import authorViewset,first_api_view
from django.urls import path
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'authors', authorViewset)

urlpatterns = [
    path('',first_api_view)

]
urlpatterns += router.urls