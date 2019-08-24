import django_filters
from django import forms
from .models import Post

class PostFilter(django_filters.FilterSet):
    filter_title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={
                'class':'search-input',
                'placeholder':'Enter Your Search ...'
                }
            )
        )


    order_by = django_filters.OrderingFilter(
        fields = ['created_datetimes']
    )

    filter_category = django_filters.CharFilter(
        field_name='category',
    )

    class Meta:
        model = Post
        fields = ('filter_title', 'filter_category')
