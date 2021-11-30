from django.urls import path,include
from twotwo import views
urlpatterns = [
    path('hii/',views.hii,name='hii'),
    path("hello/",views.hello,name='hello'),
    path('Complete_Data/',views.Complete_Data,name='Complete_Data'),
    path('Individual_Info/',views.Individual_Info,name='Individual_Info'),
    path('Branch_Details/',views.Branch_Details,name='Branch_Details'),
    path('Branch_Det/',views.Branch_Det,name='Branch_Det'),
    path('passper/',views.passper,name='passper'),
    path('passper1/',views.passper1,name='passper1'),
    path('bnchpass/',views.bnchpass,name='bnchpass'),
    path('home/',views.home,name='home'),
    path('sub_topper_list',views.sub_topper_list,name='sub_topper_list'),
    path('yesorno',views.yesorno,name='yesorno'),
    path('branch_selection',views.branch_selection,name='branch_selection'),

]
