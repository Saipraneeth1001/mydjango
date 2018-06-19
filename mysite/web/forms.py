from django import forms
from web.models import Post, Comment

# we need to import forms to use them as we did on line 1
# to connect our forms to models we have to import them there ....
# all we need is two forms right now i.e Post and comment forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'content', 'title')

        widget = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
