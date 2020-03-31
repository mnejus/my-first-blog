from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	
	class Meta:
		model = Post
		fields = ('title', 'text',)
		labels = {
			'title':('Tytuł wpisu'),
			'text':('Treść wpisu'),
		}
