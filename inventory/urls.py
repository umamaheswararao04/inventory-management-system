from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    # ---------- WEB VIEWS ----------
    path('', views.dashboard, name='dashboard'),

    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),

    path('stock-in/<int:pk>/', views.stock_in, name='stock_in'),
    path('stock-out/<int:pk>/', views.stock_out, name='stock_out'),

    path('category/add/', views.category_create, name='category_create'),
    path('supplier/add/', views.supplier_create, name='supplier_create'),

    path('stock/history/', views.stock_history_view, name='stock_history'),

    # ---------- API ENDPOINTS ----------
    path('api/products/', api_views.api_products, name='api_products'),
    path('api/stock/in/', api_views.api_stock_in, name='api_stock_in'),
    path('api/stock/out/', api_views.api_stock_out, name='api_stock_out'),
    path('api/stock/history/', api_views.api_stock_history, name='api_stock_history'),
]
