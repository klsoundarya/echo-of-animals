from .models import BlogPost, Comment
from django import forms
from django.utils.text import slugify

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'featured_image', 'description', 'habitat', 'sound_cloudinary', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                'rows': 3, 'placeholder': 'Enter name of the animal'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                'rows': 3, 'placeholder': 'Write your blog content here...'}),
            'habitat': forms.Textarea(attrs={'class': 'form-control',
                'rows': 3, 'placeholder': 'Write short on animal habitat'}),
            'author': forms.TextInput(attrs={'class': 'form-control',
                'rows': 3, 'placeholder': 'Enter your name'}),
        }
    
    def clean_title(self):
        """
        Ensure the title is unique by checking the slug field
        """
        title = self.cleaned_data['title']
        slug = slugify(title)
        if BlogPost.objects.filter(slug=slug).exists():
            raise forms.ValidationError("A blog post with a similar title already exists. Please choose a different title.")
        return title


class CommentForm(forms.ModelForm):
    """
    Form class for users to comment on a post 
    """
    class Meta:
        model = Comment 
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your comment...'
            }),
        }