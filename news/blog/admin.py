from django.contrib import admin
from.models import post


class postAdmin(admin.ModelAdmin):
  list_display=('tittle', 'slug', 'author', 'publish','status')
  list_filter = ('status', 'created', 'publish', 'author')
  search_fields = ('tittle', 'body')
  prepopulated_fields = {'slug': ('tittle',)}
  raw_id_fields = ('author',)
  date_hierarchy = 'publish'
  ordering = ['status', 'publish']

admin.site.register(post,postAdmin)

# Register your models here.
