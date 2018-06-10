from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy


class HomePage(generic.TemplateView):
    template_name = "home.html"


class ShowProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/show_profile.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug:
            user = get_object_or_404(User, username=slug)
        else:
            user = self.request.user

        if user == self.request.user:
            kwargs["editable"] = True
        kwargs["show_user"] = user
        return super().get(request, *args, **kwargs)


class SignupView(generic.edit.FormView):
    template_name = "profiles/sign_up.html"
    form_class = SignUpForm
    success_url = reverse_lazy("show_me")

    def form_valid(self, form):
        user = form.save()
        user.refresh_from_db()  # update with user's profile instance
        # Add additional profile fields from sign-up form
        user.profile.birthdate = form.cleaned_data.get("birthdate")
        user.profile.user_type = 1 if form.cleaned_data.get(
            "is_hero") is True else 0
        user.save()
        raw_password = form.cleaned_data.get("password1")
        user = authenticate(username=user.username, password=raw_password)
        login(self.request, user)
        return super().form_valid(form)
