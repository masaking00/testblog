from django.shortcuts import render
from django.views import generic

from .models import Memo

class MemoListView(generic.ListView):
    model = Memo