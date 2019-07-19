from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import CreateView

from .models import Like



class LikeCreateView(LoginRequiredMixin, CreateView):
    model = Like

    def get_counter(self, query):
        return self.model.objects.filter(**query).count()

    def get(self, request, *args, **kwargs):
        query = {
            'content_type_id': self.kwargs['type'],
            'objects_id': self.kwargs['id'],
        }
        like, is_created = self.model.objects.get_or_create(user_id=request.user.id, **query)
        if not is_created:
            likes.delete()
        return JsonResponse({'status': 'ok', 'counter': self.get_counter(query)})