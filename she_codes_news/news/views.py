from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm


class AddStoryView(generic.CreateView):
    form_class = StoryFormcontext_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        print("here2")
        print(self.request.GET.get('search'))
        search_var = self.request.GET.get('search', "")
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.filter(title__contains=search_var)[:3]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date').filter(title__contains=search_var)[3:]
        
        return context

        

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = StoryForm
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        #set author to the user logged in
        form.instance.author = self.request.user
        return super().form_valid(form)
