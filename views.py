from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionAPIView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        # Calculate and update balances before saving the new transaction
        transaction = serializer.save()
        paid_by_user = transaction.paid_by
        participants = transaction.participants.all()
        total_participants = len(participants)
        owed_amount = transaction.amount / total_participants

        for participant in participants:
            # Update balances for participants
            participant.balance -= owed_amount
            participant.save()

            # Update balances for the person who paid
            paid_by_user.balance += owed_amount
            paid_by_user.save()
