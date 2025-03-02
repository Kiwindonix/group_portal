from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta, date

# Create your views here.


#Зміна кольору оцінки, якщо оцінка олівцем(сірий)
# і якщо оцінка остаточна ручкою (синім або чорним)\


#Якщо запит відправляє студент, то показувати йому усі предмети і усі його оцінки,
# якщо запит відправляє вчитель, то показувати йому оцінки по його предмету усіх студентів


from .models import Student, Diary, Mark, Subject

def diary_view(request):
    # Отримання всіх даних із щоденника
    diary_entries = Diary.objects.all()
    
    # Приклад контексту для передачі в шаблон
    context = {
        'diary_entries': diary_entries,
    }
    return render(request, 'diary/diary.html', context)



def get_marks(request, student_id=None, date=None):
    
    today = timezone.now().date()       # Отримуємо поточну дату

    start_of_week = today - timedelta(days=today.weekday())  # Понеділок        # Визначаємо дату початку тижня (неділя)
    end_of_week = start_of_week + timedelta(days=6)  # Неділля      # Визначаємо дату закінчення тижня (неділя)
    
    try:
        student = Student.objects.get(pk=1) #pk=student_id
    except Student.DoesNotExist:
        # Обробка помилки, якщо студента не знайдено
        return render(request, 'student_not_found.html')  # Створіть відповідний шаблон
    
    # Отримуємо оцінки за тиждень
    marks = Mark.objects.filter(day__range=(start_of_week, end_of_week)).select_related('student', 'subject')  # Отримуємо оцінки
    
    info = Subject.objects.all()

    days_of_week = [(start_of_week + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(6)]  # Список дат тижня
    
    # Створюємо словник для зберігання оцінок за кожен день тижня для кожного предмету
    weekly_schedule = {}
    
    for subject in info:
        weekly_schedule[subject] = {}
        for day in days_of_week:
            try:
                mark = Mark.objects.get(student=student, subject=subject, day=day)
                weekly_schedule[subject][day] = {'mark': mark.mark, 'is_final': mark.is_final}
            except Mark.DoesNotExist:
                weekly_schedule[subject][day] = None  # Оцінки немає

    context = {     
        "student": student,
        "marks": marks,
        "weekly_schedule": weekly_schedule,
        "days_of_week": days_of_week,
        "info": info,
        "days": {
            "m":start_of_week.strftime("%d.%m"),
            "t":(start_of_week + timedelta(days=1)).strftime("%d.%m"),
            "w":(start_of_week + timedelta(days=2)).strftime("%d.%m"),
            "th":(start_of_week + timedelta(days=3)).strftime("%d.%m"),
            "f":(start_of_week + timedelta(days=4)).strftime("%d.%m"),
            "s":(start_of_week + timedelta(days=5)).strftime("%d.%m"),
        }
    }
    return render(request, 'diary/diary.html', context)



from django.http import HttpResponse
from auth_system.models import CustomUser
from .models import Student, Teacher

def migrate_users_view(request):
    existing_users = CustomUser.objects.all()
    for user in existing_users:
        if user.is_superuser:
            if not Teacher.objects.exists(teacher=user):
                Teacher.objects.create(
                    teacher = user
                )
                print(f'Added superuser as teacher: {user}')
        else:
            if not Student.objects.filter(student=user).exists():
                Student.objects.create(
                    student = user
                )
                print(f'Added user as student: {user}')
    
    return HttpResponse("User migration completed.")
