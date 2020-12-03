from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, ChildProduct, MyItem, Tip, TipBody, Likes
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import F
import json
from django.http import JsonResponse
import operator
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def main(request):
    userCount = User.objects.all().count()
    userCount = userCount + 12560
    return render(request,'main.html', {'userCount' : userCount})


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
    childproducts = ChildProduct.objects.filter(product=product_id)
    likes = Likes.objects.filter(user=request.user)
    likeCnt = Likes.objects.filter(user=request.user).count()
    i = 0

    for like in likes:
        for child in childproducts:
            if child.id == like.product.id:
                print(child.name, "찾았다")
                child.likes = 1
                print(child.likes)


    return render(request,'childproduct.html' , {'product':product, 'childproducts':childproducts, 'likes' : likes, 'likeCnt' : likeCnt})

def show_myPage(request):
    myItems_myLevel = MyItem.objects.all()
    count = myItems_myLevel.count()
    print(type(count))
    return render(request,'myPage.html', {'myItems_myLevel':myItems_myLevel, 'count':count})

def submit_myItem_in_myPage(request):
    return render(request, 'sub_Item_myPage.html')

def create_myItem_in_myPage(request):
    myItems = MyItem()
    myItems.itemName = request.GET['itemName']
    myItems.itemShop = request.GET['itemShop']
    myItems.itemDate = request.GET['itemDate']
    myItems.save()
    return redirect('submit_myItem_pop')

def detail_myItem_in_myPage(request, my_Items_id):
    myItems_detail = get_object_or_404(MyItem, pk=my_Items_id)
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

# 좋아요 누르기
@login_required
def like(request, childproduct_id):
    user = request.user
    childproduct = ChildProduct.objects.get(id=childproduct_id)
    product = get_object_or_404(Product, pk = childproduct.product.id)
    likes = Likes.objects.filter(user=user)
    flag = 0 # flag = 1 이면 like에 이미 있다는 뜻. like에서 빼기

    for like in likes:
        if childproduct.id == like.product.id:
            flag = 1
            break
    
    print(flag, "플래그")
    if flag == 1: #삭제
        Likes.objects.filter(user=user, product=childproduct).delete()
        print(childproduct.name, " 삭제 되었음")
        
    else: #추가
        like = Likes.objects.create(user=user, product=childproduct)
        print(childproduct.name, " 추가 되었음")

    likeCnt = Likes.objects.filter(user=user).count()
    print(likeCnt)

    childproduct.save()

    return HttpResponseRedirect(reverse('childproduct', args=[product.id]))
    

# 찜
@login_required
def likeCart(request):
    categories = Category.objects.all()
    likes = Likes.objects.filter(user=request.user)
    totalSum = 0
    for items in likes:
        totalSum = totalSum + 1
   
    return render(request, 'likeCart.html', {'likes' : likes, 'totalSum' : totalSum})

# 찜 삭제
@login_required
def delete_like(request, childproduct_id):
    user = request.user
    likes = Likes.objects.filter(user=request.user)
    likeCnt = Likes.objects.filter(user=user).count()
    quantity = 0
    print(likeCnt)
    
    if request.method == 'POST':
        try:
            pk = request.POST.get('product')
            childproduct = ChildProduct.objects.get(pk=pk)
            # childproduct.likes = 0
            for i in likes:
                if i.product == childproduct :
                    quantity = quantity + 1
                    print(quantity)
            if quantity > 0 :
                # childproduct = ChildProduct.objects.filter(pk=pk)
                likes = Likes.objects.filter(user=request.user, product_id=pk)
                likes.delete()
                return redirect('likeCart')
        except:
            return redirect('likeCart')
