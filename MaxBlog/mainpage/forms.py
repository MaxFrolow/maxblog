from .models import Post, Comment
from django import forms
from django.utils.translation import ugettext_lazy as _



class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'second_title', 'text', 'image', 'category']
        widgets = {
            'title': forms.TextInput(),
            'second_title': forms.TextInput(),
            'text': forms.Textarea(),
                    }
        category = forms.MultipleChoiceField(
            widget=forms.CheckboxSelectMultiple,
            choices=Post.CATEGORY_CHOICES
        )

        image = forms.ImageField(
            label=_('Title image'),
            widget=forms.FileInput(
                attrs={
                    'class': 'input'
                },
            ),
            required=False
        )
        #category = forms.ModelChoiceField()


        def __init__(self, *args, **kwargs):
            super(CreatePostForm, self).__init__(*args, **kwargs)
            self.fields['title'].widget.attrs.update({'class': 'input', name: 'title'})
            self.fields['second_title'].widget.attrs.update({'class': 'input', name: 'Second title'})
            self.fields['text'].widget.attrs.update({'class': 'input', name: 'Text'})
            self.fields['category'].widget.attrs.update({'class': 'input', name: 'Category'})



class CreateCommentForm(forms.ModelForm):


    text = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'class': 'input',
                'placeholder': 'Message',
                'name': 'message'
            }
        )
    )

    class Meta:
        model = Comment
        fields = ['text']
