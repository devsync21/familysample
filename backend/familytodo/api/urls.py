from familytodo.api.views import MemberViewSet, TodolistViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'member', MemberViewSet, basename='member')
router.register(r'todolist', TodolistViewSet, basename='todolist')

urlpatterns = router.urls
