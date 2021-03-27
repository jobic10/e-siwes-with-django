from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Company, Student, Logbook, FinalRemark, CustomUser
from .forms import *
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
import requests as r
from django.template.loader import render_to_string
from django.conf import settings
# Create your views here.


def admin_home(request):
    total_company = Company.objects.all().count()
    total_student = Student.objects.all().count()
    context = {
        'page_title': "Administrative Dashboard",
        'total_students': total_student,
        'total_companies': total_company,
        'started': Student.objects.exclude(start_date=None).count()

    }
    return render(request, 'admin_template/home_content.html', context)


@csrf_exempt
def check_email_availability(request):
    email = request.POST.get("email")
    try:
        user = CustomUser.objects.filter(email=email).exists()
        if user:
            return HttpResponse(True)
        return HttpResponse(False)
    except Exception as e:
        return HttpResponse(False)


def add_student(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    admin = CustomUserForm(request.POST or None)
    context = {'form': form, 'page_title': 'Add Student'}
    if request.method == 'POST':
        if form.is_valid() and admin.is_valid():
            student = form.save(commit=False)
            admin = admin.save(commit=False)
            admin.user_type = 3  # 3 Stands for Student

            # Send mail
            data = {'msg': "Welcome, Please use this password to login your account <b>" +
                    str(request.POST.get('password'))+"</b> ", 'SITENAME': settings.APP_NAME}
            msg_html = render_to_string(
                'email/email.html', data)
            msg_plain = render_to_string(
                'email/email.txt', data)
            admin.save()
            student.admin = admin
            student.save()
            messages.success(request, "Successfully Added")
            context['form'] = StudentForm()
            try:
                send_mail(
                    'Account Creation',
                    msg_plain,
                    settings.EMAIL_HOST_USER,
                    [request.POST.get('email')],
                    html_message=msg_html,
                )
            except:
                pass
        else:
            messages.error(request, "Invalid Data Provided ")
    return render(request, 'admin_template/add_student_template.html', context)


def admin_view_profile(request):
    admin = get_object_or_404(Admin, admin=request.user)
    form = CustomUserForm(
        request.POST or None, request.FILES or None, instance=admin.admin)
    context = {'form': form,
               'page_title': 'View/Edit Profile'
               }
    print(str(admin.admin.__dict__))
    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, request.user)

                # adminForm.save()
                messages.success(request, "Profile Updated!")
                return redirect(reverse('admin_view_profile'))
            else:
                messages.error(request, "Invalid Data Provided")
        except Exception as e:
            messages.error(
                request, "Error Occurred While Updating Profile " + str(e))
    return render(request, "admin_template/admin_view_profile.html", context)


def manage_student(request):
    students = CustomUser.objects.filter(user_type=3)
    context = {
        'students': students,
        'page_title': 'Manage Students'
    }
    return render(request, "admin_template/manage_student.html", context)


def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    form = StudentEditForm(request.POST or None,
                           request.FILES or None, instance=student)
    form2 = CustomUserForm(request.POST or None, instance=student.admin)
    context = {
        'form': form,
        'form2': form2,
        'student_id': student_id,
        'page_title': 'Edit Student'
    }
    if request.method == 'POST':
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.success(request, "Successfully Updated")
            return redirect(reverse('edit_student', args=[student_id]))
        else:
            messages.error(request, "Please Fill Form Properly!")
    else:
        return render(request, "admin_template/edit_student_template.html", context)


def admin_view_profile(request):
    admin = get_object_or_404(Admin, admin=request.user)
    form = CustomUserForm(
        request.POST or None, request.FILES or None, instance=admin.admin)
    context = {'form': form,
               'page_title': 'View/Edit Profile'
               }
    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, request.user)

                # adminForm.save()
                messages.success(request, "Profile Updated!")
                return redirect(reverse('admin_view_profile'))
            else:
                messages.error(request, "Invalid Data Provided")
        except Exception as e:
            messages.error(
                request, "Error Occurred While Updating Profile " + str(e))
    return render(request, "admin_template/admin_view_profile.html", context)


def manage_company(request):
    companies = CustomUser.objects.filter(user_type=2)
    context = {
        'companies': companies,
        'page_title': 'Manage Companies'
    }
    return render(request, "admin_template/manage_company.html", context)


def manage_logbook(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id', 0)
        student = get_object_or_404(Student, id=student_id)
        remark = request.POST.get('remark', None)
        if remark is None:
            messages.error(request, "Please fill in the remark!")
        else:
            obj, created = FinalRemark.objects.update_or_create(
                student=student, defaults={'remark': remark})
            messages.success(request, "Action Saved")
    students = CustomUser.objects.filter(user_type=3)
    context = {
        'students': students,
        'page_title': 'View Student\'s Logbook'
    }
    return render(request, "admin_template/manage_logbook.html", context)


def add_company(request):
    form = CompanyForm(request.POST or None, request.FILES or None)
    admin = CustomUserForm(request.POST or None)
    context = {'form': form, 'form2': admin, 'page_title': 'Add Company'}
    if request.method == 'POST':
        if form.is_valid() and admin.is_valid():
            company = form.save(commit=False)
            admin = admin.save(commit=False)
            admin.user_type = 2  # 2 Stands for Company
            admin.save()
            company.admin = admin
            company.save()
            messages.success(request, "Successfully Added")
            # Send mail
            data = {'msg': "Welcome, Please use this password to login your account <b>" +
                    str(request.POST.get('password'))+"</b> "}
            msg_html = render_to_string(
                'email/email.html', data)
            msg_plain = render_to_string(
                'email/email.txt', data)
            message = "Hello There! Your SIWES account has been created. Further details are in your mail."
            to = request.POST.get('phone')

            try:
                r.get(full_url)
                send_mail(
                    'Account Creation',
                    msg_plain,
                    settings.EMAIL_HOST_USER,
                    [request.POST.get('email')],
                    html_message=msg_html,
                )
            except:
                pass
            context['form'] = CompanyForm()
            context['form2'] = CustomUserForm()
        else:
            messages.error(request, "Invalid Data Provided ")
    return render(request, 'admin_template/add_company_template.html', context)


def edit_company(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    form = CompanyForm(request.POST or None,
                       request.FILES or None, instance=company)
    form2 = CustomUserForm(request.POST or None, instance=company.admin)
    context = {
        'form': form,
        'form2': form2,
        'company_id': company_id,
        'page_title': 'Edit Company'
    }
    if request.method == 'POST':
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.success(request, "Successfully Updated")
            return redirect(reverse('edit_company', args=[company_id]))
        else:
            messages.error(request, "Please Fill Form Properly!")
    else:
        return render(request, "admin_template/edit_company_template.html", context)


def delete_company(request, company_id):
    companies = CustomUser.objects.filter(user_type=2)
    context = {
        'companies': companies,
        'page_title': 'Manage Companies'
    }
    company = get_object_or_404(Company, id=company_id)
    admin = company.admin
    # Check if any student is assigned to this company
    exist = Student.objects.filter(company=company).count()
    if exist > 0:
        messages.error(request, "Sorry, there exists " + str(exist) +
                       " students assigned to this Company. What would you like to do about this ?")
    else:
        admin.delete()
        company.delete()  # Delete Company and Delete User

        messages.success(request, "Company has been deleted.")

    return redirect(reverse('manage_company'))
