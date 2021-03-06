from django.conf import settings
from .models import Student
import datetime


def SITENAME(request):
    # return {'SITENAME': settings.APP_NAME, 'no_of_weeks': settings.NO_OF_WEEKS}
    context = {'SITENAME': settings.APP_NAME,
               'NO_OF_WEEKS': settings.NO_OF_WEEKS}
    if request.user.is_authenticated:
        if request.user.user_type == 3 or request.user.user_type == "3":  # Student
            start_date = request.user.student.start_date
            date = datetime.datetime.today().strftime('%Y-%m-%d')
            date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            days = abs(start_date - date).days
            week = days // 7
            if start_date is None:
                week = 0
            else:
                if week == 0:
                    week = 1
            context['WEEK'] = week
    return context
