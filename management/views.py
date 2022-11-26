from django.shortcuts import render
from management.models import Sliders,SliderForm,category, categoryform, sub_category, sub_categoryform, brands, brandsform, size_master,product_master, size_masterform, product_masterform,color_master,color_masterform
# Create your views here.
def add_slider(request):
    form = SliderForm()
    if 'save' in request.POST:
        frm = SliderForm(request.POST,request.FILES)
        frm.save()
    return render(request,'add_slider.html',{'form':form})

def category_1(request):
    form = categoryform()
    if 'save' in request.POST:
        frm = categoryform(request.POST,request.FILES)
        frm.save()
    return render(request,'add_category.html',{'form':form})


def sub_category_1(request):
    form = sub_categoryform()
    if 'save' in request.POST:
        frm = sub_categoryform(request.POST,request.FILES)
        frm.save()
    return render(request,'add_sub_category.html',{'form':form})

def brands_1(request):
    form = brandsform()
    if 'save' in request.POST:
        frm = brandsform(request.POST,request.FILES)
        frm.save()
    return render(request,'add_brands.html',{'form':form})


def size_master_1(request):
    
    form = size_masterform()
    if 'save' in request.POST:
        frm = size_masterform(request.POST,request.FILES)
        frm.save() 
    return render(request,'size_master.html',{'form':form})

def product_master_1(request):
    form = product_masterform()
    if 'save' in request.POST:
        frm = product_masterform(request.POST,request.FILES)
        frm.save()
    return render(request,'product_master.html',{'form':form})  


def color_master_1(request):
    form = color_masterform()
    if 'save' in request.POST:
        frm = color_masterform(request.POST,request.FILES)
        frm.save()
    return render(request,'add_color_master.html',{'form':form})