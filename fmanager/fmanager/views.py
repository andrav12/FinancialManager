# Create your views here.
from rest_framework import viewsets, renderers
from rest_framework.decorators import list_route
from rest_framework.response import Response

from fmanager.fmanager.serializers import *


class CardViewSet (viewsets.ModelViewSet):
    serializer_class = CardSerializer

    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)


class GoalViewSet (viewsets.ModelViewSet):
    serializer_class = GoalSerializer

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    template_name = 'new_transaction.html'

    def get_queryset(self):
        queryset = []
        cards = Card.objects.filter(user=self.request.user)
        for card in cards:
            queryset += Transaction.objects.filter(card=card)

        return queryset

    @list_route(renderer_classes=[renderers.TemplateHTMLRenderer])
    def blank_form(self, request, *args, **kwargs):
        serializer = TransactionSerializer()
        return Response({'serializer': serializer})
