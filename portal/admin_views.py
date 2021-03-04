from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Company, Student, Logbook, FinalRemark, CustomUser
from .forms import *
from django.contrib import messages

# Create your views here.


def admin_home(request):
    total_company = Company.objects.all().count()
    total_student = Student.objects.all().count()
    context = {
        'page_title': "Administrative Dashboard",
        'total_students': total_student,
        'total_company': total_company,

    }
    return render(request, 'admin_template/home_content.html', context)


def add_student(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    admin = CustomUserForm(request.POST or None)
    context = {'form': form, 'page_title': 'Add Student'}
    if request.method == 'POST':
        if form.is_valid() and admin.is_valid():
            student = form.save(commit=False)
            admin = admin.save(commit=False)
            admin.user_type = 3  # 3 Stands for Student
            admin.save()
            student.admin = admin
            student.save()
            messages.success(request, "Successfully Added")
        else:
            messages.error(request, "Invalid Data Provided ")
    return render(request, 'admin_template/add_student_template.html', context)


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


def admin_view_profile(request):
    admin = get_object_or_404(Admin, admin=request.user)
    form = AdminForm(request.POST or None, request.FILES or None,
                     instance=admin)
    context = {'form': form,
               'page_title': 'View/Edit Profile'
               }
    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                messages.success(request, "Profile Updated!")
                return redirect(reverse('admin_view_profile'))
            else:
                messages.error(request, "Invalid Data Provided")
        except Exception as e:
            messages.error(
                request, "Error Occured While Updating Profile " + str(e))
    return render(request, "admin_template/admin_view_profile.html", context)
