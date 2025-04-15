from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    type_choices = [
        ('income', 'Income'),
        ('expense', 'Expense')
    ]
    type = models.CharField(choices=type_choices, max_length=7)
    
    def __str__(self):
        return self.name

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    
    def __str__(self):
        return f"Income: {self.amount} from {self.category.name}"

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    
    def __str__(self):
        return f"Expense: {self.amount} for {self.category.name}"

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.TextField()
    month = models.TextField()
    # start_date = models.DateTimeField()
    # end_date = models.DateTimeField()
    
    def __str__(self):
        return f"Budget ${self.amount} for user ${self.user.email}"
