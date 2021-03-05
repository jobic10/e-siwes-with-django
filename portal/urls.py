from django.urls import path
from . import company_views, admin_views, student_views, views

urlpatterns = [
    # * General
    path("", views.login_page, name='login_page'),
    path("doLogin/", views.doLogin, name='user_login'),
    path("logout_user/", views.logout_user, name='user_logout'),

    # * Admin
    path("admin/home/", admin_views.admin_home, name='admin_home'),
    path("admin/student/add", admin_views.add_student, name="add_student"),
    path("check_email_availability", admin_views.check_email_availability,
         name="check_email_availability"),
    path("admin_view_profile", admin_views.admin_view_profile,
         name='admin_view_profile'),
    path("student/manage/", admin_views.manage_student, name='manage_student'),
    path("student/edit/<int:student_id>",
         admin_views.edit_student, name='edit_student'),
    path("company/add", admin_views.add_company, name='add_company'),
    path("company/manage/", admin_views.manage_company, name='manage_company'),

    path("company/edit/<int:company_id>",
         admin_views.edit_company, name='edit_company'),
    # * Company
    path("company/home/", company_views.company_home, name='company_home'),

    # * Student
    path("student/home/", student_views.student_home, name='student_home'),

]
