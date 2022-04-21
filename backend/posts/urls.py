from rest_framework import routers

from posts.views import BlogPostViewSet

router = routers.DefaultRouter()
router.register('blogpost', BlogPostViewSet)
