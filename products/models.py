from django.db import models
from core.models import User
from django.db.models.fields import PositiveIntegerField
from django.db.models.query import QuerySet
from django.forms import ModelForm
from django.forms.models import ModelChoiceField
from django.forms.widgets import FileInput, NumberInput, Select, TextInput, Textarea
from django import forms
class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Category Title")
    slug = models.SlugField(max_length=55, verbose_name="Category Slug")
    description = models.TextField(blank=True, verbose_name="Category Description")
    category_image = models.ImageField(upload_to='category', blank=True, null=True, verbose_name="Category Image")
    is_active = models.BooleanField(verbose_name="Is Active?")
    available_products = models.PositiveIntegerField(default=0,verbose_name="Available Products")

    class Meta:
        verbose_name_plural = 'Categories'
    

    def __str__(self):
        return '{} {}'.format(self.title,self.available_products)


UNITS = (('Kg','Kg'),
    ('Unit','Unit'))
    
class Units(models.Model):
    unit = models.CharField(max_length=20,verbose_name="unit")
    SI_Unit = models.BooleanField(verbose_name="is_SI_unit")



class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name="Product Title")
    unit = models.CharField(max_length=20,choices=UNITS,verbose_name="Units")
    slug = models.SlugField(max_length=160, verbose_name="Product Slug")
    sku = models.CharField(max_length=255, unique=True, verbose_name="Unique Product ID (SKU)")
    short_description = models.TextField(verbose_name="Short Description")
    detail_description = models.TextField(blank=True, null=True, verbose_name="Detail Description")
    product_image = models.ImageField(blank=True, null=True, verbose_name="Product Image",default = 'Products/product.png')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name="Product Categoy", on_delete=models.CASCADE,blank=False)
    is_active = models.BooleanField(verbose_name="Is Active?")
    is_featured = models.BooleanField(verbose_name="Is Featured?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
    available_units = models.PositiveIntegerField(verbose_name="Available Units",default=1)
    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-updated_at', )

    def __str__(self):
        return '{} {} {} {} {} {} {} {}'.format( self.title,self.unit,self.sku,self.short_description ,self.price,self.available_units,self.category,self.updated_at)
class add_product_class(ModelForm):
    def __init__(self, *args, **kwargs):
        super(add_product_class, self).__init__(*args, **kwargs)
        self.fields['unit'].empty_label = None
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field and isinstance(field , forms.TypedChoiceField):
                field.choices = field.choices[1:] 
    class Meta:
        model = Product
        fields = ['title','unit','short_description','product_image','price','available_units']
        widgets = {
            'title' : TextInput(attrs={'class':"form-control"}),
            'unit' : Select(choices=UNITS,attrs={'class':"form-select"}),
            'short_description' : Textarea(attrs={'class':"form-control"}),
            'product_image' : FileInput(attrs={'class':"form-file-input"}),
            'price':NumberInput(attrs={'class':"form-control"}),
            'available_units':NumberInput(attrs={'class':"form-control"}),
          }
        help_texts = {
            'title':'hello',
        }