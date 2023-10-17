
from django.urls import include, path


from . import views

urlpatterns = [
    # ... your existing URL patterns ...
    path('api/transactions/', views.TransactionAPIView.as_view(), name='transaction_api'),
]


