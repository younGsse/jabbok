from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from ..models import Question
from django.db.models import Q

# Create your views here.
def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('search', '')
    part = request.GET.get('part', '')

    question_list = Question.objects.order_by('-createDate')

    if kw:
        if part == 'subject':
            question_list = question_list.filter(
                Q(subject__icontains=kw)
            ).distinct()
        if part == 'subcon':
            question_list = question_list.filter(
                Q(subject__icontains=kw) |
                Q(content__icontains=kw)
            ).distinct()
        if part == 'author':
            question_list = question_list.filter(
                Q(author__username__icontains=kw)
            ).distinct()

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {
        'question_list': page_obj,
        'page': page,
        'kw': kw,
    }
    return render(request, 'board/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question
    }
    return render(request, 'board/detail.html', context)
