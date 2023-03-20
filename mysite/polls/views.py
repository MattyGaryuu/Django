from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.

def Yuri(request):
    context = {
        "nome" : "Yuri Alberto",
        "url" : "https://scontent.fssz1-1.fna.fbcdn.net/v/t39.30808-6/336532489_189827437099728_9136934708366109271_n.jpg?_nc_cat=1&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeGkIlFFFutiBFrNPAAT331GtKbuLnMvMhG0pu4ucy8yESqGZHibYQFgTlJ6wFN4_vk-bumjKsp9vWvlEhcvttuK&_nc_ohc=_LiSF6Zx5j4AX-zdY2Z&_nc_ht=scontent.fssz1-1.fna&oh=00_AfDyav_h8s6Z8ABDwq-NUKGFdrp3Xp-pTi5DvLWdqjrcKQ&oe=641CFC76"
    }
    return render(request, "Yuri.html", context)

def index(request):
    latest_question_list = Question.objects.order_by('-question_date')[:5]
    context = {
        "latest_question_list" : latest_question_list,
    }
    return render(request,'index.html', context)

def detail(request, question_id):
    return HttpResponse(f"Você está vendo a pergunta numero {question_id}")

def results(request, question_id):
    return HttpResponse(f"O resultado da pergunta numero {question_id} é: ")

def vote(request, question_id):
    return HttpResponse(f"Você está respondendo na questão {question_id}")
