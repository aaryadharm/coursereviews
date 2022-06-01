from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import os
# from config.definitions import ROOT_DIR
import pandas as pd

# Create your views here.
def index(request):
    return render(request, "rate/index.html")