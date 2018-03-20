from django.conf.urls import url, include
from rest_framework import routers

from .viewsets import *

router = routers.DefaultRouter()

router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'images', ImageViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'organization', OrganizationViewSet)
router.register(r'location', LocationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]