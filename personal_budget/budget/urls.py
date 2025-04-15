from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, IncomeViewSet, ExpenseViewSet, BudgetViewSet, UserRegistrationView
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()
# router.register(r'categories', CategoryViewSet)
router.register(r'incomes', IncomeViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'budgets', BudgetViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
