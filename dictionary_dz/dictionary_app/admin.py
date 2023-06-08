from django.contrib import admin

from dictionary_app.models import Word, Definition

admin.site.register(Word)
admin.site.register(Definition)
