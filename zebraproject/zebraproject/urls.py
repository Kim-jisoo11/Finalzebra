"""zebraproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from zebraapp import views
from django.conf import settings
from django.conf.urls.static import static
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main, name ="main"),
    path('login/',accounts.views.login, name = 'login'),
    path('logout/',accounts.views.logout, name = 'logout'),
    path('signup/',accounts.views.signup, name = 'signup'),
    path('product/<int:category_id>/', views.show_product, name='product'),
    path('childproduct/<int:product_id>/', views.show_childproduct, name = 'childproduct' ),
    path('mypage/', views.show_myPage, name = 'mypage'),
    path('mypage/submit_myItem', views.submit_myItem_in_myPage, name = 'submit_myItem_pop'),
    # path('submit_myitem/', views.submit_myItem_in_myPage, name = 'submit_myItem'),
    path('mypage/create_myItem', views.create_myItem_in_myPage, name = 'create_myItem'),
    path('mypage/detail_myItem/<int:my_Items_id>', views.detail_myItem_in_myPage, name = 'detail_myItem_pop'),
    path('mypage/<int:my_Items_id>', views.detail_myItem_in_myPage, name = 'detail_myItem'),
    path('mypage/<int:my_Items_id>/update_myItem', views.update_myItem_in_myPage, name = 'update_myItem'),
    path('mypage/<int:my_Items_id>/delete_myItem', views.delete_myItem_in_myPage, name = 'delete_myItem'),
    path('tip/',views.tip, name ="tip"),
    path('tip/<int:tip_id>',views.tip_detail, name ="tip_detail"),
    path('childproduct/<int:product_id>/like',views.like, name ="productlike"),
        
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
