
from django.urls import path, include

from taskapp import views

urlpatterns = [
    path('',views.main,name='main'),
    path('admin_reg',views.admin_reg,name='admin_reg'),
    path('user_reg',views.user_reg,name='user_reg'),
    path('logout',views.logout,name='logout'),
    path('student_view_profile',views.student_view_profile,name='student_view_profile'),
    path('view_student',views.view_student,name='view_student'),
    path('admin_add_mark/<int:id>',views.admin_add_mark,name='admin_add_mark'),
    path('admin_view_mark/<int:id>',views.admin_view_mark,name='admin_view_mark'),
    path('admin_delete_mark/<int:id>',views.admin_delete_mark,name='admin_delete_mark'),
]
