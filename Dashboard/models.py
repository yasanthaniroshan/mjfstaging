from django.db import models
from core.models import User
from django.db.models import fields
from django.db.models.base import Model
from products.models import Product 
from core.models import User
from django.forms import ModelForm
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name="Quantity")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
    Is_collected_with_collecter = models.BooleanField(verbose_name="is collected with collecter")
    Is_transported_With_Transporter = models.BooleanField(verbose_name="is trasported with traspoter")
    Collecter_precentage = models.PositiveIntegerField(default=0.02,verbose_name="Collecter Precentages")
    Transpoter_Tip = models.DecimalField(max_digits=8 , decimal_places= 2 , verbose_name="Transpoter Tip")
    
    def __str__(self):
        return str(self.user)
    @property
    def total_price(self):
        price = self.quantity * self.product.price
        if self.Is_collected_with_collecter == True and self.Is_transported_With_Transporter == False :
            Totalprice = price + self.Collecter_precentage * price
        elif self.Is_collected_with_collecter == False and self.Is_transported_With_Transporter == True :
            Totalprice = price + self.Transpoter_Tip
        elif self.Is_transported_With_Transporter == True and self.Is_collected_with_collecter == True :
            Totalprice = price + price * self.product.price + self.Transpoter_Tip
        elif self.Is_transported_With_Transporter == False and self.Is_collected_with_collecter == False :
            Totalprice = price 
        return Totalprice
    # Creating Model Property to calculate Quantity x Price
   

STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
)

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
  
    product = models.ForeignKey(Product, verbose_name="Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    ordered_date = models.DateTimeField(auto_now_add=True, verbose_name="Ordered Date")
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=50,
        default="Pending"
        )

class Sales_records_individual(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="User")
    sale_value = models.DecimalField(verbose_name="Sales_value",max_digits=8,decimal_places=2)
    date_involved = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    Created = models.DateTimeField(auto_now_add=True)


class Sales_records_total(models.Model):
    Total_revenue = models.DecimalField(verbose_name="Total Revenue",max_digits=6,decimal_places=2,default=100.89)
    Total_buyers_invovlved = models.PositiveIntegerField(verbose_name="Total Buyers Involved",default=13)
    Total_sellers_involved = models.PositiveIntegerField(verbose_name="Total Sellers Involved",default=89)
    Total_collectors_involved = models.PositiveIntegerField(verbose_name="Totak Collectors Involved",default=8)
    Total_transporters_involved = models.PositiveIntegerField(verbose_name="Total Transporters Involved",default=2)
    Total_users_involved = models.PositiveIntegerField(verbose_name="Total users Involved",default=112)
    last_updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        self.Total_users_involved =  self.Total_buyers_invovlved + self.Total_collectors_involved + self.Total_sellers_involved + self.Total_transporters_involved
        return '{} - {} + {} + {} + {} = {}'.format(self.Total_revenue,self.Total_buyers_invovlved,self.Total_sellers_involved,self.Total_collectors_involved,self.Total_transporters_involved,self.Total_users_involved)

