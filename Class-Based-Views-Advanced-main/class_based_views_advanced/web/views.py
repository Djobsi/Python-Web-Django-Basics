import json
import random

from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from class_based_views_advanced.web.models import Todo


# def index(request):
#     context = {
#         'todo_list': [t.title for t in Todo.objects.all()],
#     }
#
#     return HttpResponse(json.dumps(context))


class SearchTodoByTitleForm(forms.Form):
    title_pattern = forms.CharField(
        max_length=Todo.MAX_LENGTH_TITLE,
        required=False,
    )

    is_done = forms.BooleanField(
        required=False,
    )


class DetailTodoView(views.DetailView):
    model = Todo
    template_name = 'web/detail_todo.html'
    slug_field = 'slug'
    query_pk_and_slug = True

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        tenant = self.request.GET.get("tenant", None)
        if tenant is not None:
            queryset = queryset.filter(tenant=tenant)
        return queryset


class LatestCreatedMixin:
    latest_created_count = 5

    def get_queryset(self):
        return super().get_queryset().order_by('-pk')[:self.latest_created_count]


class ListTodoView(views.ListView):
    model = Todo
    # latest_created_count = 7

    # queryset = Todo.objects.all()
    template_name = "web/list-todo.html"

    # Static way
    paginate_by = 5

    # Dynamic way
    # def get_paginate_by(self, queryset=None):
    #     return random.randint(2, 5)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Todos list'

        context['search_form'] = SearchTodoByTitleForm(
            initial={
                "title_pattern": self.get_title_pattern(),
            }
        )

        return context

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = self.apply_filter(queryset)

        return queryset

    def apply_filter(self, queryset):
        title_pattern = self.get_title_pattern()
        if title_pattern:
            queryset = queryset.filter(title__icontains=title_pattern)

        # is_done = self.get_is_done_filter()
        # if is_done is not None:
        #     queryset = queryset.filter(is_done=is_done)

        return queryset

    def get_title_pattern(self):
        return self.request.GET.get("title_pattern", None)

    def get_is_done_filter(self):
        return self.request.GET.get("is_done", None) == 'on'


class CreateTodoView(views.CreateView):
    model = Todo
    fields = ('title', 'description')

    template_name = "web/create-todo.html"
    success_url = reverse_lazy('todos-list')


'''
CRUD:
1. Create
    - CreateView
2. Read (details, list)
    - DetailView
    - ListView
3. Update
    - UpdateView
4. Delete
    - DeleteView

'''