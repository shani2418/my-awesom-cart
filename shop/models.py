from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField #inheritance #migrate no use karo hato and makemigrations no pan niche git bash ma..python manage.py migrate ai rite
    product_name = models.CharField(max_length=50)#migrations n use karvi atle shop ni under bani jai je change hoi yee.....
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)#migrate thi database change thai
    pub_date = models.DateField() #createsuperuser pan vapru : password 1234, email:shanichauhan@, name:shani
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name #atale apde product nu nam lakhel ave atle aa karu

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

def __str__(self):
    return self.update_desc[0:7] + "..."
#koi pan model banavi ane add karvu j pade admin.py ni ander

#second models ma category and image and price and subcategory umryu ane have
#makemigrations karu atake migration vala folder ma bani jai foldeer
#ane pachhi migrate karvi pachhi apda admin ma javanu...
#python manage.py shell kari...from shop.models import Product and from django.utils import timezone and
#jene add kaevanu hoi ye
#myprod.save()...and myprod.product_id