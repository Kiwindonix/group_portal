from django.urls import path
from .views import diary_view, get_marks, migrate_users_view

urlpatterns = [
    path('/', get_marks, name='diary'),
    path('migrate-users/', migrate_users_view, name='migrate_users'), #оновити базу даних
]