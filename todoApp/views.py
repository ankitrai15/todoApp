from turtle import clear
from django.http import request
from django.shortcuts import render,redirect
from todoList.models import todoList

def home(request):
    rslt = {}
    if request.method == 'POST':
        item = request.POST.get('itemData')
        data = todoList(item_name = item)
        data.save()
        rslt = todoList.objects.all()
        return redirect('/')
    rslt = todoList.objects.all()
    return render(request,'index.html',{'rslt':rslt})

def dltRcd(request,id):
    
    dltrcd = todoList.objects.get(id = id)
    dltrcd.delete()
    return redirect('/')

def clearAll(request):
    
    clearData = todoList.objects.all()
    clearData.delete()
    return redirect('/')