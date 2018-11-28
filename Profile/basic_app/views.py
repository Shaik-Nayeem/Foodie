from django.shortcuts import render,redirect
from basic_app.forms import ProductForm
from basic_app.models import Product,Menu
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.urlresolvers import reverse

import json
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.



def home1(request,*args,**kwargs):
    return render(request,'auth/auth_social.html')

@login_required
def home(request):
    user=request.user
    if user.has_perm('basic_app.is_admin'):
        return redirect(reverse('show'))
    elif user.has_perm('basic_app.is_user'):
        return redirect(reverse('student'))
    else:
        return render(request,'product_form.html')
        

def validate_username(request):

    
        username = request.POST.get('username', None)
    
        data = {
        'is_taken': Product.objects.filter(name__iexact=username).exists(),
              
        }
        return JsonResponse(data)


def unauth(request):
    
    return render(request,'hii.html')
def hii(request,pk):
    
    product=Product.objects.get(pk=pk)

    form=ProductForm(request.POST,request.FILES,instance=product or None)
    if form.is_valid():
          form.save()

          return redirect('show')

    return render(request,'show.html',{'form':form})
    #return HttpResponse(form)


def validate_usernam(request):

    if request.is_ajax():
       name = request.POST['username']

       products=Product.objects.get(name=name)
       print(products)
       #name=request.GET.get('username', None)
      

       data = {}
       data['result'] = 'you made a request'
       data['result1'] = 'Nayeem'

       data['name'] =name
            

       return HttpResponse(json.dumps(data), content_type="application/json")


@permission_required('basic_app.is_admin')
def show(request):
    products=Product.objects.all()
    #for e in products:
      #print(e.menu_set.all())

    return render(request,'show.html',{'products':products})

def insert(request):
   #name= request.POST.get("title", "")
    form=ProductForm(request.POST,request.FILES or None)
    if form.is_valid():
           form.save()

           return redirect('show')

    return render(request,'show.html')



def view(request,pk):

    product=Product.objects.get(pk=pk)#//$org =Organization::where('organization_name',$org_name);
    #c1=Menu(product=product)
    
    return render(request,'view.html',{'product':product})


def create_product(request):

   # form=ProductForm()

   
 
    return render(request,'product_form.html')


def update(request,pk):

    product=Product.objects.get(pk=pk)
   # form=ProductForm(instance=product)
    return render(request,'product_view.html',{'product':product})

"""def edit(request,pk):
    product=Product.objects.get(pk=pk)

    form=ProductForm(request.POST,request.FILES,instance=product or None)
    if form.is_valid():
           form.save()

           return redirect('show')

    return render(request,'product_view.html',{'form':form})"""

def delete(request,pk):

    product=Product.objects.get(pk=pk)

    product.delete()

    return redirect('show')



    