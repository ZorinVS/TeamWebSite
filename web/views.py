from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Work
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.template import loader

def index(request):
    return render(request, 'web/index.html')

def solutions(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'web/solutions.html', {'posts': posts})

def solution_detail(request, pk):  # <--- ОБЯЗАТЕЛЬНО pk здесь!
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'web/solution_detail.html', {'post': post})


def works(request):
    works = Work.objects.all().order_by('-created_at')
    return render(request, 'web/works.html', {'works': works})



def portfolio(request):
    works = Work.objects.all().order_by('-created_at')
    return render(request, 'web/portfolio.html', {'works': works})

def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f"Сообщение с сайта от {form.cleaned_data['name']}"
            message = f"Email: {form.cleaned_data['email']}\n\n{form.cleaned_data['message']}"
            try:
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
                return JsonResponse({'message': 'Спасибо, ваше сообщение отправлено!'})
            except Exception as e:
                return JsonResponse({'error': 'Ошибка при отправке письма.'}, status=500)
        else:
            return JsonResponse({'error': 'Некорректные данные формы.'}, status=400)

    # если обычный GET
    form = ContactForm()
    return render(request, 'web/contacts.html', {'form': form})

def robots(request):
    content = loader.render_to_string("robots.txt")
    return HttpResponse(content, content_type="text/plain")
