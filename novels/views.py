from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Novel
from .forms import NovelForm
from django.db.models import Q
from django.utils import timezone
# Create your views here.

def index(request):
    novel_db_list = Novel.objects.values_list('title').distinct()
    novel_list = []
    for novel in novel_db_list:
        novel_list.append(novel[0])

    title = request.GET.get('title', '')
    page = request.GET.get('page', '1')
    if title:
        subtitle_list = Novel.objects.filter(
            Q(title=title)
        ).distinct().order_by('-createDate')
        paginator = Paginator(subtitle_list, 10)
        page_obj = paginator.get_page(page)
        context = {
            'novel_list': novel_list,
            'subtitle_list': page_obj,
            'page': page,
        }
        return render(request, 'novels/novel_home.html', context)
    return render(request, 'novels/novel_home.html', {'novel_list': novel_list})

@login_required(login_url='common:login')
def detail(request, novel_id):
    novel = get_object_or_404(Novel, pk=novel_id)
    context = {
        'novel': novel
    }
    return render(request, 'novels/novel_detail.html', context)

@login_required(login_url='common:login')
def novel_create(request):
    if request.method == 'POST':
        form = NovelForm(request.POST)
        if form.is_valid():
            novel = form.save(commit=False)
            novel.author = request.user
            novel.createDate = timezone.now()
            novel.save()
            return redirect('novels:index')
    else:
        form = NovelForm()
    return render(request, 'novels/novel_form.html', {'form': form})
