from django import forms
from .models import Articles

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        query = Articles.objects.filter(title__icontains=title)
        if query.exists():
            self.add_error("title", f"\"{title}\" already exists")
        return data

class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data #dict
    #     print("cleaned_data", cleaned_data)
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == "this is a new article":
    #         raise forms.ValidationError('This title is taken!')
    #     print("title", title)
    #     return title

    def clean(self):
        cleaned_data = self.cleaned_data #dict
        print("cleaned_data", cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == "this is a new article":
            self.add_error("title", "This title is taken")
            # raise forms.ValidationError('This title is taken!')
        if "today" in content and "today" in title.lower():
            self.add_error("content", "today is not a valid word in this article content")
            raise forms.ValidationError('This content is not a valid word in this whatever article')
        return cleaned_data