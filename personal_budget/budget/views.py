from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Category, Income, Expense, Budget
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer, IncomeSerializer, ExpenseSerializer, BudgetSerializer, UserRegistrationSerializer
import json

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    category = CategorySerializer()
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Get the request data (no need to manually parse JSON here, DRF does this for you)
        data = request.data
        
        # Use the serializer to validate and create the Income instance
        serializer = self.get_serializer(data=data)
        
        if serializer.is_valid():
            # If valid, save and return the created object
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            return Income.objects.filter(user_id=user_id)
        return Income.objects.filter(id=self.kwargs["pk"])

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Get the request data (no need to manually parse JSON here, DRF does this for you)
        data = request.data
        
        # Use the serializer to validate and create the Expense instance
        serializer = self.get_serializer(data=data)
        
        if serializer.is_valid():
            # If valid, save and return the created object
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            return Expense.objects.filter(user_id=user_id)
        return Expense.objects.filter(id=self.kwargs["pk"])

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            return Budget.objects.filter(user_id=user_id)
        return Budget.objects.filter(id=self.kwargs["pk"])

class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # Save the new user and return a success response
            serializer.save()
            return Response({"message": "User created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)