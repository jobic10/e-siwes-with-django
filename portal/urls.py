from django.urls import path
from . import company_views, admin_views, student_views, views

urlpatterns = [
    # * General
    path("", views.login_page, name='login_page'),
    path("doLogin/", views.doLogin, name='user_login'),
    path("logout_user/", views.logout_user, name='user_logout'),


    # * Admin
    path("admin/home/", admin_views.admin_home, name='admin_home'),

    # * Company
    path("company/home/", company_views.company_home, name='company_home'),


    # * Student
    path("student/home/", student_views.student_home, name='student_home'),

]
