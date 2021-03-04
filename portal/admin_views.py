from django.shortcuts import render
from .models import Company, Student, Logbook, FinalRemark

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
