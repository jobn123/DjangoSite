from django.shortcuts import render

# # Create your views here.

# -*- coding: utf-8 -*-
from django.http import HttpResponse
from west.models import Character
from django.views.decorators import csrf
# def first_page(request):
#     staff_list = Character.objects.all()
#     response = ""
#     response1 = ""
#     for var in staff_list:
#       response1 += var.name + " "
#     response = response1
#     return HttpResponse("<p>" + response +"</p>")

def templay(request):
  context = {}
  context['label'] = 'Hello World'
  return render(request, 'templay.html', context)

#staff info
def staff(request):
  staff_list = Character.objects.all()
  # response = ""
  # response1 = ""
  # for var in staff_list:
  #   context = {'label': var.name}
  return render(request, 'templay.html', {'staffs': staff_list})

def form(request):
  return render(request, 'form.html')

def investigate(request):
  #get method
  # rlt = request.GET['staff']
  # return HttpResponse(rlt)
  
  #post method
  ctx = {}
  if request.POST:
  #   ctx['rlt'] = request.POST['staff']
  # return render(request, "investigate.html", ctx)
  
  #将post 的数据 放到数据库中
    submitted = request.POST['staff']
    new_record = Character(name = submitted)
    new_record.save()
  all_records = Character.objects.all()
  ctx['staff'] = all_records
  return render(request, "investigate.html", ctx)