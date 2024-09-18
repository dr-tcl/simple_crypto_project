from typing import Union

from django.db import transaction

from user.models import Balance
from django.db.models import F


class BalanceRepository:
    @staticmethod
    def check_if_user_balance_enough(user_id: int, balance: float) -> bool:
        return Balance.objects.filter(user_id=user_id, balance__gte=balance).exists()

    @classmethod
    def decrease_user_balance(cls, user_id: int, deduction_amount: Union[int, float]) -> None:
        with transaction.atomic():
            try:
                if cls.check_if_user_balance_enough:
                    raise ValidationError("user balance is not enough.")

                Balance.objects.select_for_update().filter(user_id=user_id).update(
                    balance=F('balance') - deduction_amount)
            except Exception as exc:
                print(exc)
                transaction.set_rollback(True)
                raise exc
