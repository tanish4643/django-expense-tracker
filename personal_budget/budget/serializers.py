from rest_framework import serializers
from .models import Category, Income, Expense, Budget
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'type']

class IncomeSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Income
        fields = ['id', 'user', 'category', 'amount', 'date']

    def create(self, validated_data):
        # Extract the nested user and category data
        category_data = validated_data.pop('category')

        # Create the related User and Category instances
        category = Category.objects.create(**category_data)  # Use ** to unpack the dictionary

        # Now create the Income instance, linking the created user and category
        income = Income.objects.create(user=validated_data.pop("user"), category=category, **validated_data)
        return income

class ExpenseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    
    class Meta:
        model = Expense
        fields = ['id', 'user', 'category', 'amount', 'date']
    
    def create(self, validated_data):
        # Extract the nested user and category data
        category_data = validated_data.pop('category')

        # Create the related User and Category instances
        category = Category.objects.create(**category_data)  # Use ** to unpack the dictionary

        # Now create the Expense instance, linking the created user and category
        expense = Expense.objects.create(user=validated_data.pop("user"), category=category, **validated_data)
        return expense

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id', 'user', 'amount', 'category', 'month']

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # Ensures password is not returned in responses
        }

    def create(self, validated_data):
        # Create user instance and hash password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user