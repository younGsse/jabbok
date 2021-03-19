from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from ..forms import QuestionForm
from ..models import Question

from django.utils import timezone

# Create your views here.

@login_required(login_url='common:login')
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.createDate = timezone.now()
            question.author = request.user
            question.save()
            return redirect('board:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'board/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, "Not authority")
        return redirect('board:detail', question_id=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modifiedDate = timezone.now()
            question.save()
            return redirect('board:detail', question_id=question_id)
    else:
        form = QuestionForm(instance=question)
    context = {
        'form': form
    }
    return render(request, 'board/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, "Not authority")
        return redirect('board:detail', question_id=question_id)
    question.delete()
    return redirect('board:index')
