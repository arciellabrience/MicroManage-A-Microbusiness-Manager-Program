"""CLPDesign4 URL Configuration

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
from django.urls import path, include
from django.contrib.auth import views as auth_views

from general.views import (home_view, item_relation_view, price_adjustment_view, about_us)
from general import views
# from login.views import (login_view, register_page, logoutUser, register_details_page, password_reset_request)
from login.views import (login_view, register_page, logoutUser, password_reset_request)
from products.views import (new_product_view, edit_product_view, delete_product_view)
from raw.views import (new_raw_view, edit_raw_view, delete_raw_view)
# from databases.views import (sold_products_view, existing_products_view, raw_database_view)
from orders.views import (sold_products_view)
from raw.views import (raw_database_view)
from products.views import (existing_products_view)
from orders.views import (add_order)
from dashboard.views import (dashboard_with_pivot)

from products.views import (view_edit_product, view_delete_product)
from raw.views import (view_edit_raw, view_delete_raw)

# login_view, registerPage, logoutUser,

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', views.home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_page, name='register'),
    # path('register_details/', register_details_page, name='register_details'),

    path('logout/', logoutUser, name='logout'),

    path('add_order/', add_order, name='add_order'),
    # path('add_order/', views.add_order, name='add_order'),

    # path('add_order/', dashboard_with_pivot, name='add_order'),

    path('new_product/', new_product_view, name='new_product'),
    path('new_raw/', new_raw_view, name='new_raw'),

    #ITEM RELATION AND PRICE ADJUSTMENT DI NA NEED
    # path('item_relation/', item_relation_view, name='item_relation'),
    # path('price_adjustment/', price_adjustment_view, name='price_adjustment'),


    # path('edit_product/', edit_product_view, name='edit_product'),
    path('edit_product/<str:pk>/', edit_product_view, name='edit_product'),
    # path('edit_raw/', edit_raw_view, name='edit_raw'),
    path('edit_raw/<str:pk>/', edit_raw_view, name='edit_raw'),
    # path('delete_product', delete_product_view, name='delete_product'),
    path('delete_product/<str:pk>', delete_product_view, name='delete_product'),
    # path('delete_raw/', delete_raw_view, name='delete_raw'),
    path('delete_raw/<str:pk>', delete_raw_view, name='delete_raw'),
    path('sold_database/', sold_products_view, name='sold_database'),
    path('products_database/', existing_products_view, name='products_database'),
    path('raw_database/', raw_database_view, name='raw_database'),

    path('about_us/', about_us, name='about_us'),

    path('view_edit_product/', view_edit_product, name="view_edit_product"),
    path('view_edit_raw/', view_edit_raw, name="view_edit_raw"),

    path('view_delete_product/', view_delete_product, name="view_delete_product"),
    path('view_delete_raw/', view_delete_raw, name="view_delete_raw"),

    # path('accounts/', include('django.contrib.auth.urls')),

    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
    # path("password_reset", views.password_reset_request, name="password_reset")
    # path('password_reset', auth_views.PasswordChangeView.as_view(template_name='password/password_reset.html'))
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password/password_reset.html', subject_template_name='password/password_reset_email.txt', email_template_name='password/password_reset_email.html',
    #          # success_url='/login/'
    #      ), name='password_reset')
    # path('password_reset/', password_reset_request, name="password_reset")


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password/password_reset.html"), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_done.html"), name="password_reset_done"),
    path('reset_password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_complete.html"), name="password_reset_complete"),

    #DI TO NAGAMIT ATM
    path('dashboard/', include('dashboard.urls'))
]
