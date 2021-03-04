from django.shortcuts import render, get_object_or_404

# Create your views here.


def company_home(request):
    me = get_object_or_404(Staff, admin=request.user)
    total_students = Student.objects.filter(company=me).count()
    context = {
        'page_title': 'Industrial-Based (Company) Dashboard',
        'total_students': total_students,
    }
    return render(request, 'company_template/home_content.html', context)
