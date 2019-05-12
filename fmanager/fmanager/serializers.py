from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from fmanager.fmanager.constants import GoalState
from fmanager.fmanager.models import Card, Goal, Transaction


class CardSerializer(ModelSerializer):

    class Meta:
        model = Card
        fields = (
            'id',
            'name',
            'user',
            'number',
            'cvv',
            'amount',
            'expireDate',
        )


class GoalSerializer(ModelSerializer):

    class Meta:
        model = Goal
        fields = (
            'id',
            'name',
            'user',
            'state',
            'objective',
            'amountCollected',
        )

    def update(self, instance, validated_data):
        # TODO use amount set by user
        card = Card.objects.filter(amount__gte=10)[0]
        if not card:
            raise serializers.ValidationError("You dont have enough money")
        card.amount = card.amount - 10
        card.save()
        instance.amountCollected += 10
        if instance.amountCollected >= instance.objective:
            instance.state = GoalState.ACHIEVED
        instance.save()
        return instance

    def validate(self, data):
        # Object-level validation
        # Custom validation logic will go here
        # card = Card.objects.filter(id=data['card'].id)
        if data['amountCollected'] >= data['objective']:
            raise serializers.ValidationError("Your goal is already completed")
        return data


class TransactionSerializer(ModelSerializer):

    class Meta:
        model = Transaction
        fields = (
            'id',
            'name',
            'card',
            'description',
            'amount',
        )

    def validate(self, data):
        # Object-level validation
        # Custom validation logic will go here
        card = Card.objects.filter(id=data['card'].id)
        if data['amount'] > card[0].amount:
            raise serializers.ValidationError("You dont have enough money.")
        return data

    def create(self, validated_data):
        card = Card.objects.filter(id=validated_data['card'].id)[0]
        card.amount = card.amount - validated_data['amount']
        card.save()
        return Transaction.objects.create(**validated_data)