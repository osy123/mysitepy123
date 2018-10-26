from datetime import timezone

from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from board import models
from board.models import Board


def list(request):
    board_list = Board.objects.all().order_by('-id')
    return render(request, 'board/list.html',{'board_list':board_list})

def modify(request):
    return render(request, 'board/modify.html')

def view(request):
    return render(request, 'board/view.html')

def write(request):
    board = Board()
    board.name = request.session['authuser']['name']
    board.title = request.POST['title']
    board.content = request.POST['content']

    board.save()
    return HttpResponseRedirect("/board")

def writeform(request):
    return render(request, 'board/write.html')

def delete(request):
    id = int(request.GET['id']) # string으로 들어와서 int값으로 바꿈 ,
    bd=Board.objects.filter(id=id)
    bd.delete()

    return HttpResponseRedirect("/board")

def view(request):
    id = int(request.GET['id'])
    bd = Board.objects.filter(id=id)
    results = bd[0]
    return render(request,'board/view.html',{'board':results})

def modifyform(request):
    id = request.GET['id']
    results = Board.objects.get(id=id)
    data= {'board':results}
    return render(request,'board/modify.html', data)

def modify(request):

    id = request.GET['id']
    results = Board.objects.get(id=id)

    results.title = request.POST['title']
    results.content = request.POST['content']


    results.save()
    return HttpResponseRedirect("/board/")