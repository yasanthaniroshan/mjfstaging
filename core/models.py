from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import fields
from django.db.models.enums import Choices
from django.forms.models import ModelForm
from django import forms
from django.forms.widgets import EmailInput, FileInput, NumberInput, Select, TextInput, Textarea

GENDER_TYPES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
USER_ROLES_MARKET = (
    ('Buyer', 'Buyer'),
    ('Producer', 'Producer'),
    ('Collecter','Collecter'),
    ('Transporter','Transporter'),
)
DISTRICTS_IN_SL = (
    ('Amp','Ampara'),
    ('Anu','Anuradhapura'),
    ('Bad','Badulla'),
    ('Bat','Batticaloa'),
    ('Col','Colombo'),
    ('Gal','Galle'),
    ('Gam','Gampaha'),
    ('Ham','Hambanthota'),
    ('Jaf','Jaffna'),
    ('Kal','Kaluthara'),
    ('Kan','Kandy'),
    ('Keg','Kegalle'),
    ('Kil','Kilinochchi'),
    ('Kur','Kurunagala'),
    ('Man','Mannar'),
    ('Mat','Matale'),
    ('Math','Mathara'),
    ('Mon','Monaragala'),
    ('Mul','Mullativu'),
    ('Nuw','Nuwara Eliya'),
    ('Pol','Polonnaruwa'),
    ('Put','Puttalam'),
    ('Rat','Rathnapura'),
    ('Tri','Trincomalee'),
    ('Vav','Vavuniya'),
)
class User(AbstractUser):


    gender = models.CharField(choices=GENDER_TYPES,verbose_name="Gender",default="Male",max_length=10)
    user_role_in_market = models.CharField(choices=USER_ROLES_MARKET,verbose_name="User Role",default="Producer",max_length=15)
    national_ID_Number = models.CharField(max_length=12,verbose_name="National ID Number")
    Address = models.CharField(max_length=150, verbose_name="Nearest Location")
    district = models.CharField(choices=DISTRICTS_IN_SL,max_length=150, verbose_name="District",default="Colombo")
    avatar = models.ImageField(upload_to = 'User_avatars', blank = True,null = True,default = 'svg/avatar.svg')
    Whatsapp_number = models.CharField(max_length=12,verbose_name="Whatsapp Number")
    
    def __str__(self):
     return self.username

class Userform(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Userform, self).__init__(*args, **kwargs)
        self.fields['gender'].empty_label = None
        self.fields['user_role_in_market'].empty_label = None
        self.fields['district'].empty_label = None
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field and isinstance(field , forms.TypedChoiceField):
                field.choices = field.choices[0:]
    class Meta:
        model = User
        fields = ['first_name','last_name','gender','user_role_in_market','national_ID_Number','Address','district','avatar','Whatsapp_number']
        widgets = {
            'first_name' : TextInput(attrs={'class':"form-control"}),
            'last_name' : TextInput(attrs={'class':"form-control"}),
            'email' : EmailInput(attrs={'class':"form-control"}),
            'gender' : Select(choices=GENDER_TYPES,attrs={'class':"form-select"}),
            'user_role_in_market' : Select(choices=USER_ROLES_MARKET,attrs={'class':"form-select"}),
            'national_ID_Number' : NumberInput(attrs={'class':"form-control"}),
            'Address' : Textarea(attrs={'class':"form-control"}),
            'district' : Select(choices =DISTRICTS_IN_SL ,attrs={'class':"form-select"}),
            'avatar' : FileInput(attrs={'class':"form-file-input"}),
            'Whatsapp_number':NumberInput(attrs={'class':"form-control"}),
          }
        help_texts = {
            'Whatsapp_number':"Use this format - +947XXXXXXXX"
            }
# class company_proile(models.Model):
    