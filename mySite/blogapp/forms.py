from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    #DESCRIPTION:
    # setting up all the froms we want to include into web page
    # class meta is a django feature that automaticatlly set up forms for you.
    class Meta:
        model = Post # connects to the model
        fields = ('author','title', 'text',) # what fields on the model that you want to be created as a from

        # setting up the widgets to allow CSS, JS or any static styling to the forms
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),# connected to three classes
        }

class CommentForm(forms.ModelForm):
    #DESCRIPTION:
    #setting up all the froms we want to include into web page

    class Meta:
        model = Comment # connect to a model

        # from that model, you decide which you want to include to be created
        # as a form.
        fields = ('author', 'text')

        # allows connection static files or styling files to the created from widgets.
        widgets = {
        'author':forms.TextInput(attrs={'class': 'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
