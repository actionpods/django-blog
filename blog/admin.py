from django.contrib import admin
from blog.models import Blog, Category
from django import forms
from tinymce.widgets import TinyMCE

class BlogAdminForm(forms.ModelForm):
    #Set the editor to a WYSIWYG or Markdown
    #NOTE: Be sure to edit the template to reflect a change.
    body = forms.CharField(widget=TinyMCE())
    class Meta:
        model = Blog
        fields = '__all__'

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    form = BlogAdminForm
    prepopulated_fields = {
                           'slug': ('title',),
                           }


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
