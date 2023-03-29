# Django core import
from django.shortcuts import render , redirect
from django.urls import reverse

# Django auth mixin
from django.contrib.auth.mixins import LoginRequiredMixin  
from cloud_kitchen.settings import STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SECRET
# import razorpay
# import razorpay
import stripe
from django.conf import Settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
stripe.api_key = STRIPE_SECRET_KEY
endpoint_secret = STRIPE_WEBHOOK_SECRET

#Apps Model Import 
from apps.restaurant.models import Food
from apps.finance.models import Transaction
from apps.authentication.models import CustomUsers

# Generic views imports
from django.views.generic import View

class Paymentview(View, LoginRequiredMixin):
    template_name = "finance/payment.html"

    def get(self, request):
        address = request.session.get('address')
        phone = request.session.get('phone')
        customer = CustomUsers.objects.get(id=request.session.get('customer'))   
        cart = request.session.get('cart')
        foods = Food.get_foods_by_id(request.session.get('foods'))
        details =  [address, phone, customer, cart, foods]

        # Get Total Amout 
        price=0
        for food in foods:
            one_food=food.price*cart.get(str(food.id))
            price=price+one_food
        host = self.request.get_host()
        # order_id = request.POST.get('order-id')
        # order = Order.
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    # 'price': '{{PRICE_ID}}',
                    # 'quantity': 1,
                    'price_data' : {
                        'currency':'inr',
                        'unit_amount' : price*100,
                        'product_data' : {
                            'name' : 'food-order',
                        },
                    },
                    'quantity' : 1,
                },
            ],
            mode='payment',
            # success_url=YOUR_DOMAIN + '/success.html',
            # cancel_url=YOUR_DOMAIN + '/cancel.html',
            success_url="http://{}{}".format(host,reverse("finance:payment-success")),
            cancel_url="http://{}{}".format(host,reverse("finance:payment-cancle")),
        )

        return redirect(checkout_session.url, code=303)

        #razorpay client, payment_id
        # client = razorpay.Client(auth=("rzp_test_HEjhLuxzjbQpb2", "2O8iww11khXfilLTaVyOMS6J"))
        # payment_id = client.order.create({'amount': price*100, 'currency':'INR', 'payment_capture': '1' })
        # print("payment_id : ",payment_id )
        # transaction = Transaction(made_by=customer, amount=price, payment_id= payment_id['id'])

#---------------------------------(made_by, amount, order_id, payment_id)
# import razorpay
# client = razorpay.Client(auth=("YOUR_ID", "YOUR_SECRET"))

# DATA = {
#     "amount": 100,
#     "currency": "INR",
#     "receipt": "receipt#1",
#     "notes": {
#         "key1": "value3",
#         "key2": "value2"
#     }
# }
# client.order.create(data=DATA)
#---------------------------------


        # return render(request, self.template_name,{ 'details' :details, "price" : price, 'payment_id' : payment_id })

        # def save(self, *args, **kwargs):
        #    if self.order_id is None and self.created_at and self.id:
        #         self.order_id = self.created_at.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        #     return super().save(*args, **kwargs)

        #note- oder save for restaurant
        # for food in foods:
        #     print(cart.get(str(food.id)))
        #     order = Order(customer=CustomUsers(id=customer),
        #                 food=food,
        #                 price=food.price,
        #                 address=address,
        #                 phone=phone,
        #                 quantity=cart.get(str(food.id)))
        #     order.save()
        # request.session['cart'] = {}
        # return redirect('restaurant:cart')


class Callbackview(View, LoginRequiredMixin):
    template_name = "finance/callback.html"

    def get(self, request):
        return render(request, self.template_name)


class Successview(View,LoginRequiredMixin):
    template_name = "finance/cancle.html"

    def get(self, request):

        context = {
            'payment_status' : "success"
        }
        return render(request, self.template_name, context)

class Cancleview(View, LoginRequiredMixin):
    template_name = "finance/cancle.html"

    def get(self, request):

        context = {
            'payment_status' : "cancle"
        }
        return render(request, self.template_name, context)

@csrf_exempt
def my_webhook_view(request):
  payload = request.body

  # For now, you only need to print out the webhook payload so you can see
  # the structure.
  print(payload)

  return HttpResponse(status=200)

# @csrf_exempt
# def my_webhook_view(request):
#   payload = request.body
#   sig_header = request.META['HTTP_STRIPE_SIGNATURE']
#   event = None

#   try:
#     event = stripe.Webhook.construct_event(
#       payload, sig_header, endpoint_secret
#     )
#   except ValueError as e:
#     # Invalid payload
#     return HttpResponse(status=400)
#   except stripe.error.SignatureVerificationError as e:
#     # Invalid signature
#     return HttpResponse(status=400)

#     # handle the checkout.sesstion.completed event 
#     if event['type'] == 'checkout.sesstion.completed':
#         session = event['data']['object']

#         if sesstion.payment_status == "paid":
#             #fullfill the purchase
#             fullfill_order()

#   return HttpResponse(status=200)

# def fullfill_order():
#     pass