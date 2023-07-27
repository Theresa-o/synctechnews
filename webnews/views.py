from django.shortcuts import redirect, render
from django.db.models import Q
from django.core.paginator import Paginator
from django.views import View
from news.models import NewsItem
from .forms import NewsItemForm

class WebNewsView(View):
    def get(self, request):
        search_param = request.GET.get('search')
        type_param = request.GET.get('type')

        queryset = NewsItem.objects.all()

        if search_param:
            queryset = queryset.filter(
                Q(by__icontains=search_param) |
                Q(title__icontains=search_param) |
                Q(item_type__icontains=search_param)
            )
            
        if type_param:
            queryset = queryset.filter(item_type=type_param)

        paginator = Paginator(queryset, per_page=101)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'news_items': page_obj,
            'form': NewsItemForm()
        }

        return render(request, 'home.html', context)


class NewsItemCreateView(View):
    def get(self, request):
        form = NewsItemForm()
        context = {
            'form': form
        }
        return render(request, 'post.html', context)

    def post(self, request):
        form = NewsItemForm(request.POST)
        if form.is_valid():
            news_item = form.save(commit=False)
            news_item.api_created = True
            news_item.save()
            return redirect('home') 
        else:
            context = {
                'form': form
            }
            return render(request, 'post.html', context)