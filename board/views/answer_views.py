from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

from ..forms import AnswerForm
from ..models import Question, Answer

@login_required(login_url='common:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.createDate = timezone.now()
            answer.author = request.user
            answer.question = question
            answer.save()
            return redirect('board:detail', question.id)
    else:
        form = AnswerForm()
    context = {
        'question': question,
        'form': form,
    }
    return render(request, 'board/detail.html', context)

@login_required(login_url='common:login')
def answer_modify(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, 'Not authority')
        return redirect('board:detail', question_id=answer.question.id)
    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modifyDate = timezone.now()
            answer.save()
            return redirect('board:detail', answer.question.id)
    form = AnswerForm(instance=answer)
    context = {
        'form': form,
    }
    return render(request, 'board/answer_form.html', context)

@login_required(login_url='common:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    question_id = answer.question.id
    if request.user != answer.author:
        messages.error(request, 'Not authority')
        return redirect('board:detail', question_id=question_id)
    answer.delete()
    return redirect('board:detail', question_id=question_id)
