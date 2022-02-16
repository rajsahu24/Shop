from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name='store'),
    path('<slug:category_slug>/',views.store,name='products_id_category'),
    path('<slug:category_slug>/<slug:product_slug>',views.product_details,name='products_details')
]