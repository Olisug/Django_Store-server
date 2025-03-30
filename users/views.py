from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail, BadHeaderError
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserLoginForm, UserRegisterForm, ContactForm
from store.settings import EMAIL_HOST_USER


def registration(request, **kwargs):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        return redirect('products:index')
    return render(request,
                  'users/registration.html',
                  locals(),)
                #   context={'title': 'Регистрация'},
                #   **kwargs)


class CustomLoginView(SuccessMessageMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    fields = ('username', 'password',)
    success_message = 'Вы успешно зашли в свой'
    redirect_authenticated_user = True
    title = 'Вход'

    def get_success_url(self) -> str:
        return reverse_lazy('products:index')


class CustomLogoutView(LogoutView):
    template_name = 'users/logout.html'
    fields = '__all__'
    redirect_authenticated_user = True
    title = 'Выход'

    def get_success_url(self) -> str:
        return reverse_lazy('products:index')


def contact_view(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            # from_email = request.user.email,
            message = form.cleaned_data['message']
            try:
                send_mail(
                          subject=subject,
                          message=message,
                          from_email=EMAIL_HOST_USER,
                          recipient_list=(EMAIL_HOST_USER,),
                          fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('products:index')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request,
                  "users/request_form.html",
                  context={'form': form,
                           'title': 'Отправка сообщения в тех.поддержку'})


def success_view(request):
    return render(request,
                  'users/success.html')
