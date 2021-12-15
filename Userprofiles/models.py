from django.db import models
from core.models import User



class Curent_user_management(models.Model):
    Number_of_users = models.PositiveIntegerField(verbose_name="Number of Users",default=1)
    Number_of_sellers = models.PositiveIntegerField(verbose_name="Number of Sellers",default = 1)
    Number_of_buyers = models.PositiveIntegerField(verbose_name="Number of Buyers",default=1)
    Number_of_collectors = models.PositiveIntegerField(verbose_name= "Number of Collectors",default=1)
    Number_of_transporters = models.PositiveIntegerField(verbose_name="Number of Transporters",default=1)
    def __str__(self) :
        self.Number_of_users =  self.Number_of_transporters + self.Number_of_collectors + self.Number_of_sellers + self.Number_of_buyers
        return '{} - {} - {}'.format(self.Number_of_users,self.Number_of_buyers,self.Number_of_sellers)

class CompanyProfile(models.Model):
    company_name = models.CharField(verbose_name="Company Name",max_length=200)
    number_of_workers = models.SmallIntegerField(verbose_name="Number of Workers",default=1)
    your_position = models.CharField(verbose_name="Your Position",max_length=100)
    