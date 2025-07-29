import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = "alexeysazanov"
email = "alexeysazanov@gmail.com"
password = "sazanov"

if not User.objects.filter(username=username).exists():
    print("Создаю суперпользователя...")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print("Суперпользователь уже существует.")
