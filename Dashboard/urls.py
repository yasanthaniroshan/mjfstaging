from django.urls import path


from .views import add_product, dashboard,products,updateuser,profile,contactdetails

urlpatterns = [
    path('dashboard/',dashboard,name = "dashboard"),
    path('add-product/<str:keyward>',add_product,name = "add-product"),
    path('products/',products,name = "products"),
    path('update-user',updateuser,name = "update_user"),
    path('contact-details',contactdetails,name = "contact_details"),
    path('user/<int:user_id>',profile, name= "profile")
]