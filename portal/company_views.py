from django.shortcuts import render, HttpResponse, get_object_or_404, redirect, reverse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
# Create your views here.


def company_home(request):
    me = get_object_or_404(Company, admin=request.user)
    total_students = Student.objects.filter(company=me).count()
    context = {
        'page_title': 'Industrial-Based (Company) Dashboard',
        'total_students': total_students,
    }
    return render(request, 'company_template/home_content.html', context)


def company_view_profile(request):
    admin = get_object_or_404(Company, admin=request.user)
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
                return redirect(reverse('company_view_profile'))
            else:
                messages.error(request, "Invalid Data Provided")
        except Exception as e:
            messages.error(
                request, "Error Occurred While Updating Profile " + str(e))
    return render(request, "company_template/company_view_profile.html", context)


def view_logbook(request, logbook_id):
    me = request.user
    logbook = get_object_or_404(Logbook, id=logbook_id)
    if logbook.student.company != me.company:
        messages.error(request, "Sorry, you do not have access to this")
        return redirect(reverse('company_students'))
    context = {
        'logbook': logbook,
        'page_title': 'View Logbook',
    }
    return render(request, "company_template/view_logbook.html", context)


def view_student_logbook(request, student_id):
    me = request.user
    student = get_object_or_404(Student, id=student_id, company=me.company)
    logbooks = Logbook.objects.filter(student=student).order_by('-week')
    context = {
        'student': student,
        'logbooks': logbooks,
        'page_title': 'View Student Logbook',
    }
    return render(request, "company_template/view_student_logbook.html", context)


def view_students(request):
    me = request.user
    students = Student.objects.filter(company=me.company)
    context = {
        'students': students,
        'page_title': 'View Students',
    }
    return render(request, "company_template/view_students.html", context)


def update_logbook(request, logbook_id):
    if request.method != 'POST':
        return redirect(reverse('company_students'))
    logbook = get_object_or_404(Logbook, id=logbook_id)
    if logbook.student.company != request.user.company:
        messages.error(
            request, "Sorry, you do not have access to this resource")
        return redirect(reverse('company_students'))

    remark = request.POST.get('remark')
    if len(remark) < 5:
        messages.error(request, "Please fill the form properly!")
        return redirect(reverse('company_students'))
    logbook.remark = remark
    logbook.save()
    messages.success(request, "Logbook Remarks Saved")
    return redirect(reverse('company_view_logbook', args=[logbook_id]))
