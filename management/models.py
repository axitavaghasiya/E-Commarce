from pyexpat import model
from django.db import models
from django.forms import ModelForm

# Create your models here.

class Sliders(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)
    image = models.FileField(upload_to='media/')

class SliderForm(ModelForm):
    class Meta:
        model = Sliders
        fields = ['title','desc','image']


class category(models.Model):
    category_name = models.TextField(max_length=100)
    category_image = models.FileField(upload_to='media/')
    def __str__(self):
        return self.category_name

class categoryform(ModelForm):
    class Meta:
        model = category
        fields = ['category_name','category_image']


class sub_category(models.Model):
    sub_category_name = models.TextField(max_length=100)
    cat_id = models.ForeignKey(category,on_delete=models.CASCADE,default='')
    def __str__(self):
        return self.sub_category_name
class sub_categoryform(ModelForm):
    class Meta:
        model = sub_category
        fields = ['cat_id','sub_category_name']


class brands(models.Model):
    brands_name = models.TextField(max_length=100)
    brands_logo = models.FileField(upload_to='media/')
    cat_id = models.ForeignKey(category,on_delete=models.CASCADE,default='')
    def __str__(self):
        return self.brands_name
class brandsform(ModelForm):
    class Meta:
        model = brands
        fields = ['brands_name','brands_logo','cat_id']


class size_master(models.Model):
    size_name = models.TextField(max_length=100)
    def __str__(self):
        return self.size_name
class size_masterform(ModelForm):
    class Meta:
        model = size_master
        fields = ['size_name']

class product_master(models.Model):
    title = models.CharField(max_length=100,default='')
    desc = models.CharField(max_length=100,default='')
    image = models.FileField(upload_to='media/',default='')
    price = models.CharField(max_length=100,default='')
    qty = models.CharField(max_length=100,default='')
    cat_id = models.ForeignKey(category,on_delete=models.CASCADE,default='')
    sub_cat = models.ForeignKey(sub_category,on_delete=models.CASCADE,default='')
    brand_id = models.ForeignKey(brands,on_delete=models.CASCADE,default='')
    size_id = models.ForeignKey(size_master,on_delete=models.CASCADE,default='')
   
class product_masterform(ModelForm):
    class Meta:
        model = product_master
        fields = ['title','desc','image','price','qty','cat_id','sub_cat','brand_id','size_id']

class color_master(models.Model):
    code = models.CharField(max_length=100)

class color_masterform(ModelForm):
    class Meta:
        model = color_master
        fields = ['code']

class new_register(models.Model):
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Emailaddress = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

class change_pass(models.Model):
    password = models.CharField(max_length=100)
    newpassword = models.CharField(max_length=100)
    conformpassword = models.CharField(max_length=100)


class add_to_cart(models.Model):
    user_id = models.ForeignKey(new_register,on_delete= models.CASCADE)
    product_id = models.ForeignKey(product_master,on_delete= models.CASCADE)
    qty = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    amount = models.CharField(max_length=100)
    
class chackout_register(models.Model):
    Email = models.CharField(max_length=100)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    PostCode = models.CharField(max_length=100)
    user_id = models.ForeignKey(new_register,on_delete= models.CASCADE)
    cart_ids = models.CharField(max_length=500,default='[]')
    pay_status = models.CharField(max_length=50,default='unpaid')
    Amount = models.CharField(max_length=50,default='0')

