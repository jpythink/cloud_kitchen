# Django core import
from django.shortcuts import render , redirect

# Django auth mixin
from django.contrib.auth.mixins import LoginRequiredMixin

# import razorpay
import razorpay

#Apps Model Import 
from apps.restaurant.models import Food
from apps.finance.models import Transaction
from apps.authentication.models import CustomUsers

# Generic views imports
from django.views.generic import CreateView, View, DeleteView, UpdateView

class Paymentview(View, LoginRequiredMixin):
    template_name = "finance/payment.html"

    def get(self, request):
        address = request.session.get('address')
        phone = request.session.get('phone')
        customer = CustomUsers.objects.get(id=request.session.get('customer'))   
        cart = request.session.get('cart')
        foods = Food.get_foods_by_id(request.session.get('foods'))
        print("This is the finance app ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++>>>>>")
        print(address, phone, customer, cart, foods)
        print("this is the custome object ===========================================>>>>",customer)
        details =  [address, phone, customer, cart, foods]

        # Get Total Amout 
        price=0
        for food in foods:
            one_food=food.price*cart.get(str(food.id))
            price=price+one_food

        #razorpay client, payment_id
        client = razorpay.Client(auth=("rzp_test_HEjhLuxzjbQpb2", "2O8iww11khXfilLTaVyOMS6J"))
        payment_id = client.order.create({'amount': price*100, 'currency':'INR', 'payment_capture': '1' })
        print("payment_id : ",payment_id )
        transaction = Transaction(made_by=customer, amount=price, payment_id= payment_id['id']) 

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


        return render(request, self.template_name,{ 'details' :details, "price" : price, 'payment_id' : payment_id })

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
    template_name = "finance/success.html"

    def post(self, request):

        a= request.POST
        print("This is the successview =====================================================>>>>>>>>>")
        print(a)
        return render(request, self.template_name)