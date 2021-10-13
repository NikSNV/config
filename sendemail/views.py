import re

from django.shortcuts import render

from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from config.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL


def contact_view(request):
    # если метод GET, вернем форму
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            to_emails_temp = form.cleaned_data['to_emails']
            # Выбираем всех получателей
            to_emails = re.findall('\S+@\S+', to_emails_temp)
            message = form.cleaned_data['message']
            try:
                email = EmailMessage(subject, message, DEFAULT_FROM_EMAIL, to_emails)
                # отправим письмо в формате html так как используем html-редактор
                email.content_subtype = 'html'
                email.send()
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('success')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "email.html", {'form': form})


def success_view(request):
    return HttpResponse('Почта успешно отправлена.')
