from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "category", "tags", "status"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 8, "class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }

    # Field-level Validation: මාතෘකාව අකුරු 5ට වඩා වැඩි විය යුතුය
    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title

    # Form-level Validation: මාතෘකාව සහ විස්තරයේ මුල් කොටස සමාන විය නොහැක
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")

        if title and content and title.lower() in content.lower()[:50]:
            raise forms.ValidationError("Don't repeat the title verbatim at the start of the content.")
        return cleaned_data
    
    fields = ["title", "content", "category", "tags", "status", "cover_image"]