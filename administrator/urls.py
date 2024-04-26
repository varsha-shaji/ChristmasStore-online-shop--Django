# urls.py

from django.urls import path
from .views import admin_home, admin_logout, add_new_category, add_new_product, view_categories, view_products, users,updatecategory,deletecategory,updateproduct,deleteproduct
urlpatterns = [
    path('admin/', admin_home, name="admin_home"),
    path('admin_logout/', admin_logout, name="admin_logout"),
    path('add_new_category/', add_new_category, name="add_new_category"),
    path('add_new_product/', add_new_product, name="add_new_product"),
    path('view_categories/', view_categories, name="view_categories"),
    path('view_products/', view_products, name="view_products"),
    path('users/', users, name="users"),
    path('updatecategory/<int:category>', updatecategory, name="updatecategory"),
    path('deletecategory/<int:category>', deletecategory, name="deletecategory"),
    path('updateproduct/<int:product>', updateproduct, name="updateproduct"),
    path('deleteproduct/<int:product>', deleteproduct, name="deleteproduct"),
]
