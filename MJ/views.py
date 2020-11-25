from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):

    template_name = 'MJ/home.html'


class HomeView2(TemplateView):

    template_name = 'MJ/home2.html'


class HomeErrorView(TemplateView):

    template_name = 'MJ/home_error.html'


class IntroView(LoginRequiredMixin, TemplateView):

    template_name = 'MJ/intro.html'


class SNSView(LoginRequiredMixin, TemplateView):

    template_name = 'MJ/sns.html'