from django.shortcuts import render
from .models import Category, Product, ChildProduct, MyItem, Tip, TipBody
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import F
import operator
# Create your views here.
def main(request):
    return render(request,'main.html')


def show_product(request, category_id):
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    products = Product.objects.filter(category=category).order_by('pub_date')
    # childproducts = ChildProduct.objects.get(pk = product_id)
    paginator = Paginator(products, 12)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    return render(request, 'product.html', {'category': category, 'categories': categories ,'posts' : posts})


def show_childproduct(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    childproduct = ChildProduct.objects.all()

    return render(request,'childproduct.html' , {'product':product, 'childproduct':childproduct})

def show_myPage(request):
    myItems_myLevel = MyItem.objects.all()
    return render(request,'myPage.html', {'myItems_myLevel':myItems_myLevel})

def submit_myItem_in_myPage(request):
    return render(request, 'sub_Item_myPage.html')

def create_myItem_in_myPage(request):
    myItems = MyItem()
    # if request.method == "POST":
    #     myItems.myItemName = request.POST.get('itemName')
    #     myItems.myItemShop = request.POST.get('itemShop')
    #     myItems.myItemDate = request.POST.get('itemDate')
    #     myItems.save()
    
    myItems.itemName = request.GET['itemName']
    myItems.itemShop = request.GET['itemShop']
    myItems.itemDate = request.GET['itemDate']
    myItems.save()
    return redirect('mypage')

def detail_myItem_in_myPage(request, my_Items_id):
    myItems = get_object_or_404(MyItem, pk=my_Items_id)
    return render(request, 'detail_Item_myPage.html', {'myItems_detail':myItems_detail})

def update_myItem_in_myPage(request, my_Items_id):
    myItems_update = get_object_or_404(MyItem, pk=my_Items_id)
    
    if request.method == "POST":
        myItemName = request.POST.get('itemName')
        myItemShop = request.POST.get('itemShop')
        myItemDate = request.POST.get('itemDate')
        myItems_update.itemName = myItemName
        myItems_update.itemShop = myItemShop
        myItems_update.itemDate = myItemDate
        myItems_update.save()
        return redirect('detail_myItem', my_Items_id)
    return render(request, 'update_Item_myPage.html', {'myItems_update':myItems_update})

def delete_myItem_in_myPage(request, my_Items_id):
    myItems = get_object_or_404(MyItem, pk=my_Items_id)
    myItems.delete()
    return redirect('mypage')

def tip(request):
    tips = Tip.objects.all()
    return render(request, 'tip.html',{'tips':tips})

def tip_detail(request, tip_id):
    tip = get_object_or_404(Tip, pk=tip_id)
    return render(request, 'tip_detail.html', {'tip':tip})