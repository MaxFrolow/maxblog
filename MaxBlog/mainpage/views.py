from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView,FormView
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string
from django_filters.views import FilterView
from .models import Post, Comment
from .forms import CreatePostForm, CreateCommentForm
from .filters import PostFilter
from django.db.models import Count
from .filtermixins import UserPostMixin


def asside_block(context, queryset):
    newest = queryset[:2]
    favorite = queryset.order_by('likes')[0:4]
    css_count = queryset.filter(category='CSS').count()
    js_count = queryset.filter(category='JavaScript').count()
    jq_count = queryset.filter(category='Jquery').count()
    wd_count = queryset.filter(category='Web Design').count()
    context.update({'css_count':css_count,
                    'js_count':js_count,
                    'jq_count':jq_count,
                    'wd_count':wd_count,
                    'favorite': favorite,
                    'newest': newest
                    })
    return context

class PostListView(FilterView):
    filterset_class = PostFilter
    queryset = Post.objects.all()
    template_name = 'post/mainpage.html'
    strict = False
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        asside_block(context, self.queryset)


        return context

class MyPostsView(PostListView):
    queryset = Post.objects.all()

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)


class PostDetailView(DetailView):
    template_name = 'post/blog-post.html'
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):

        #adding CreateCommentForm
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update({'form': CreateCommentForm})

        asside_block(context, self.queryset)


        return context

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


class PostUpdateView(UpdateView, UserPostMixin):
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


class PostDeleteView(DeleteView, UserPostMixin):
    template_name = 'post/delete_form.html'
    success_url = '/'
    queryset = Post.objects.all()

class CommentCreateView(CreateView, LoginRequiredMixin):
    model = Comment
    form_class = CreateCommentForm
    template_name = 'post/blog-post.html'
    success_url = '/'


    def form_valid(self, form):
        data_form = form.save(commit=False)
        data_form.author = self.request.user
        data_form.post_id = self.kwargs['post_id']
        data_form.save()
        return JsonResponse({
            'status':'ok',
            'comment': render_to_string('post/includes/comment.html',
                                        context={'comment':data_form})

        })

    def form_invalid(self, form):
        return JsonResponse({'status':'fail', 'form': str(form)})



class CommentDetailView(LoginRequiredMixin, UpdateView):
    template_name = "post/includes/comment.html"
    context_object_name = 'comment'
    fields = '__all__'
    model = Comment
