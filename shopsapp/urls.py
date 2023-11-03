from django.urls import path
from shopsapp import views

urlpatterns=[
    path('shoppg/',views.shoppg,name="shoppg"),
    path('add/',views.add,name="add"),
    path('save_category/',views.save_category,name="save_category"),
    path('dis/',views.dis,name="dis"),
    path('editcat/',views.editcat,name="editcat"),
    path('editcat/<int:dataid>/',views.editcat,name="editcat"),
    path('update/<int:dataid>/',views.update,name="update"),
    path('delete_cat/<int:dataid>/',views.delete_cat,name="delete_cat"),
    path('pro/',views.pro,name="pro"),
    path('savepro/',views.savepro,name="savepro"),
    path('dispro/',views.dispro,name="dispro"),
    path('editpro/<int:proid>/',views.editpro,name="editpro"),
    path('updatepro/<int:proid>/',views.updatepro,name="updatepro"),
    path('deletepro/<int:proid>/',views.deletepro,name="deletepro"),
    path('adminlog/',views.adminlog,name="adminlog"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('viewcontact/',views.viewcontact,name="viewcontact"),
    # path('delete/<int:dataid>/',views.delete,name="delete"),



]