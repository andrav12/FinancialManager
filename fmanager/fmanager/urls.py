
from rest_framework.routers import DefaultRouter


# We define a router object. It will look at our viewsets, decide
# what URLs we need and create them automatically so we don't have to
from fmanager.fmanager.views import *

router = DefaultRouter()
# Register the viewsets that the router must analyze
router.register(r'card', CardViewSet, base_name='card')
router.register(r'transaction', TransactionViewSet, base_name='transaction')
router.register(r'goal', GoalViewSet, base_name='goal')

# The variable `urlpatterns` will simply receive the URLs computed by the router
# Lets open a shell, import the variable `router` and have a look at the URLs
# it produces
urlpatterns = router.urls
