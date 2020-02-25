from django.urls import path
from . import views

urlpatterns=[
  path('',views.index,name='index'),
  path('home',views.index,name='index'),
  path('reg',views.reg,name='reg'),
  path('reglogic',views.reglogic,name='reglogic'),
  path('viewall',views.viewall,name='viewall'),
  path('findcourse',views.findcourse,name='findcourse'),
  path('deletecourse',views.deletecourse,name='deletecourse'),
  path('courseupdate',views.courseupdate,name='courseupdate')
  
] 