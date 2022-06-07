from abc import abstractmethod, ABC


class PaymentStrategy(ABC):

    @abstractmethod
    def execute_payment(self, amount: float) -> None:
        pass


class BankAccountStrategy(PaymentStrategy):
    def execute_payment(self, amount: float) -> None:
        print(f"Payment of ${amount} made from bank account.")


class PayPalStrategy(PaymentStrategy):
    def execute_payment(self, amount: float) -> None:
        print(f"Payment of ${amount} made from PayPal.")


class GooglePayStrategy(PaymentStrategy):
    def execute_payment(self, amount: float) -> None:
        print(f"Payment of ${amount} made from GooglePay.")


class Customer:
    payment_method: PaymentStrategy

    def setup_payment_strategy(self, payment_strategy: PaymentStrategy):
        self.payment_method = payment_strategy

    def execute_payment(self, amount: float) -> None:
        try:
            self.payment_method.execute_payment(amount)
        except AttributeError as e:
            print("Please set up your payment method before payment.")
