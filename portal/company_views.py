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
