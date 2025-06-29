from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        print("Processing payment of amount:", amount)

    
    def cancel(self, amount):
        print("Payment cancelled for amount:", amount)



class StripePayment(PaymentProcessor):
    
    def pay(self, amount):
        print(f"Paid ${amount} via Stripe")
    
    

    
    



class PaypalPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Paid ${amount} via Paypal")
    
    def cancel(self, amount):
        print(f"Paypal payment of ${amount} cancelled")

# client code
def process_payment(payment_processor, amount):
    payment_processor.pay(amount)

paypal = PaypalPayment()
process_payment(paypal, 100)

stripe = StripePayment()
process_payment(stripe, 200)
stripe.cancel(200)
