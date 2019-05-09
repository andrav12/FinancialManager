from django.contrib import admin

# Register your models here.
from fmanager.fmanager.models import Card, Goal, Transaction


class CardAdmin(admin.ModelAdmin):

    list_display = ['name', 'user', 'amount']
    list_filter = ['user', 'amount']

# This is how we tell Django to use the class TaskAdmin as the UI configuration
# for the UI


admin.site.register(Card, CardAdmin)


class GoalAdmin(admin.ModelAdmin):

    list_display = ['name', 'description', 'objective', 'amountCollected']
    list_filter = ['user', 'objective', 'amountCollected']


admin.site.register(Goal, GoalAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'amount']
    list_filter = ['card', 'amount']


admin.site.register(Transaction, TransactionAdmin)
