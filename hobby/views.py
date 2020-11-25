from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from hobby.models import Idol, Member, Ent
from django.contrib.auth.mixins import LoginRequiredMixin


class HobbyModelView(LoginRequiredMixin, TemplateView):
    template_name = 'hobby/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Idol', 'Member', 'Ent']
        return context


class IdolList(ListView):
    model = Idol


class MemberList(ListView):
    model = Member


class EntList(ListView):
    model = Ent


class IdolDetail(DetailView):
    model = Idol


class MemberDetail(DetailView):
    model = Member


class EntDetail(DetailView):
    model = Ent