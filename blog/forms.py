from django import forms
from ckeditor.widgets import CKEditorWidget
from blog.models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(), label='Conteúdo')

    class Meta:
        model = Post
        fields = (
            'title', 'subtitle', 'category', 'image', 'content', 'status')
