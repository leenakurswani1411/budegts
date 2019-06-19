from django.db import models
from django.contrib.auth.models import User

class ExpenseCategory(models.Model):
    title = models.CharField('title', max_length=100)
    description = models.CharField('Description', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class ExpenseAccount(models.Model):
    title = models.CharField('title', max_length=100)
    balance = models.IntegerField('balance', default=0)
    description = models.CharField('Description', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class ExpenseItem(models.Model):
    title = models.CharField('Title', max_length=100)
    amount = models.IntegerField('Amount', default=0)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE , blank=True, null=True)
    description = models.CharField('Description', max_length=200, blank=True, null=True)
    date = models.DateField('Date', max_length=200)

    account = models.ForeignKey(ExpenseAccount, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Leena(models.Model):
    name = models.CharField('Name', max_length=100)
    query = models.CharField('Query', max_length=100)
    email = models.CharField('Email', max_length=100)

    def __str__(self):
        return self.name