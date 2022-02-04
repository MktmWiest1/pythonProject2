from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("cloth1/", views.Cloth1ListView.as_view(), name="cloth1_list"),
    path("cloth2/", views.Cloth2ListView.as_view(), name="cloth2_list"),
    path("cloth3/", views.Cloth3ListView.as_view(), name="cloth3_list"),
    path("cloth4/", views.Cloth4ListView.as_view(), name="cloth4_list"),
    path("add-order/", views.OrderCreateView.as_view(), name="order_create"),
    path("products/<int:id>/", views.ClothDetailView.as_view(), name="product_detail"),
    path("cloth1/<int:id>/", views.ClothDetailView.as_view(), name="cloth1_detail"),

]


