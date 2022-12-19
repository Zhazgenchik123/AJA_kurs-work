from django.shortcuts import render, get_object_or_404, redirect
from .models import Articles, Coureses, Aja_look
from . import models
from .forms import JobForm


def index(request):
    art = Articles.objects.all()
    return render(request, 'home/index.html', {'art': art})


def detail_view(request, id):
    lang = get_object_or_404(models.Articles, id=id)
    art = Articles.objects.all()
    context ={
        'lang': lang,
        'art': art,
    }
    return render(request, 'home/join_hood.html', context)


def voc(request):
    error = ''
    aja = Aja_look.objects.all()
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voc')
        else:
            error = 'incorrect form'
    form = JobForm
    data = {
        'form': form,
        'error': error,
        'aja': aja,
    }
    return render(request, 'home/vocation.html', data)


def about_us(request):
    return render(request, 'home/about_us.html')


def courses(request):
    course = Coureses.objects.all()

    info = {
        'course': course,
    }
    return render(request, 'home/courses.html', info)


def detail_course_view(request, id):
    detail = get_object_or_404(models.Coureses, id=id)
    course = Coureses.objects.all()
    context = {
        'detail': detail,
        'course': course,
    }
    return render(request, 'home/course_detail.html', context)
