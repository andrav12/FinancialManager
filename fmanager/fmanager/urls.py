from django.urls import path
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
urlpatterns += [
    path(r'home/', Homepage.as_view(), name='home_page'),
    path(r'cards-list/', CardsList.as_view(), name='cards_list'),
    path(r'transactions-list/', TransactionsList.as_view(), name='trans_list'),
    path(r'goals-list/', GoalsList.as_view(), name='goals_list'),
    path(r'transaction-detail/<int:pk>/', TransactionDetail.as_view(), name='trans_detail'),
    path(r'goal-detail/<int:pk>/', GoalDetail.as_view(), name='goal_detail'),
    path(r'transaction-new/', TransactionCreate.as_view(), name='trans_new'),
    path(r'card-new/', CardCreate.as_view(), name='card_new'),
    path(r'goal-new/', GoalCreate.as_view(), name='goal_new'),
]
