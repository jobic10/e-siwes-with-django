from django.shortcuts import render

# Create your views here.


def student_home(request):
    student = get_object_or_404(Student, admin=request.user)
    context = {}
    return render(request, 'student_template/home_content.html', context)
