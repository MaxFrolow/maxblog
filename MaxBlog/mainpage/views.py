from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.utils.translation import ugettext_lazy as _
from django_filters.views import FilterView
from .models import Post, Comment
from .forms import CreatePostForm, CreateCommentForm





def index(request):
    #context = {"object_list": Post.objects.all()}
    return render(request, 'index.html')

class PostListView(ListView):
    queryset = Post.objects.all()
    template_name = 'post/mainpage.html'
    paginate_by = 14


class PostDetailView(DetailView):
    template_name = 'post/blog-post.html'
    queryset = Post.objects.all()

class PostCreateView(CreateView, LoginRequiredMixin):
    form_class = CreatePostForm
    template_name = 'post/form.html'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context.update({'btn_text': _('Create')})
        return context

    def form_valid(self, form):
        new_form = form.save(commit=False)
        new_form.author = self.request.user
        new_form.save()
        return HttpResponseRedirect('/')


class PostUpdateView(UpdateView):
    form_class = CreatePostForm
    template_name = 'post/form.html'
    queryset = Post.objects.all()
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context.update({'btn_text': _('Update')})
        return context
    def get_success_url(self):
        return reverse_lazy('mainpage:detail', kwargs={'pk': self.object.pk})


class PostDeleteView(DeleteView):
    template_name = 'post/delete_form.html'
    success_url = '/'
    queryset = Post.objects.all()

class CommentCreateView(CreateView):
    form_class = CreateCommentForm
    template_name = 'post/includes/comment_form.html'
    model = Comment
    success_url = '/'

    def form_valid(self, form):
        data_form = form.save(commit=False)
        data_form.author = self.request.User
        data_form.post_id = self.kwargs['post_id']
        data_form.save()
        return JsonResponse({
            
        })