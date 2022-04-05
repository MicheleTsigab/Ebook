from .views import authorViewset,ebookViewset,authored_ebook
from django.urls import path
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'author', authorViewset)
router.register(r'ebook',ebookViewset)
router.register(r'authored_ebook',authored_ebook)
urlpatterns = [
    #path('',first_api_view)

]
urlpatterns += router.urls