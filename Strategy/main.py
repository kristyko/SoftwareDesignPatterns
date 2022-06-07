from customer import Customer, PayPalStrategy, GooglePayStrategy


def main():
    paypal_payment = PayPalStrategy()
    google_pay_strategy = GooglePayStrategy()

    customer = Customer()
    customer.execute_payment(30)

    customer.setup_payment_strategy(paypal_payment)
    customer.execute_payment(100)

    customer.setup_payment_strategy(google_pay_strategy)
    customer.execute_payment(20)


if __name__ == '__main__':
    main()
