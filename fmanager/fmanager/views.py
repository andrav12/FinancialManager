# Create your views here.
from django.shortcuts import redirect
from rest_framework import viewsets, renderers
from rest_framework.decorators import list_route
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

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
    template_name = 'edit_transaction.html'

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


class CardsList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'cards.html'

    def get(self, request):
        queryset = Card.objects.all()
        return Response({'cards': queryset})


class TransactionsList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'transactions.html'

    def get(self, request):
        queryset = Transaction.objects.all()
        return Response({'transactions': queryset})


class GoalsList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'goals.html'

    def get(self, request):
        queryset = Goal.objects.all()
        queryset = [[goal, (goal.amountCollected * 100) / goal.objective] for goal in queryset]
        return Response({'goals': queryset})


class TransactionCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'new_transaction.html'

    def get(self, request):
        serializer = TransactionSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('trans_list')


class GoalCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'new_goal.html'

    def get(self, request):
        serializer = GoalSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = GoalSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('goals_list')


class CardCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'new_card.html'

    def get(self, request):
        serializer = CardSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = CardSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('cards_list')


class TransactionDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'edit_transaction.html'

    def get(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        serializer = TransactionSerializer(transaction)
        return Response({'serializer': serializer, 'transaction': transaction})

    def post(self, request, pk):
        transaction = get_object_or_404(Transaction, pk=pk)
        serializer = TransactionSerializer(transaction, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'transaction': transaction})
        serializer.save()
        return redirect('trans_list')


class GoalDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'edit_goal.html'

    def get(self, request, pk):
        goal = get_object_or_404(Goal, pk=pk)
        serializer = GoalSerializer(goal)
        return Response({'serializer': serializer, 'goal': goal})

    def post(self, request, pk):
        goal = get_object_or_404(Goal, pk=pk)
        serializer = GoalSerializer(goal, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'goal': goal})
        serializer.save()
        return redirect('goals_list')


class Homepage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'homepage.html'

    def get(self, request):
        return Response({"message": "Hello, world!"})
