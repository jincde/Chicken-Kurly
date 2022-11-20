from django import forms
from .models import Article, ReComment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "image"]


class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        
        fields = ["content",]
        labels = {
            'content': '답글'
        }