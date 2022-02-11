from django.contrib import admin

from .models import News, Comment


class CommentInLine(admin.TabularInline):
	model = Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'created_at']
	list_filter = ['flag']
	search_fields = ['content']
	inlines = [CommentInLine]
	fieldsets = (
		('Заголовок', {
			'fields': ('title',),
			'description': 'заголовок новости'
		}),
		('Основные характеристики', {
			'fields': ('content', 'flag'),
			'description': 'основные характеристики новости',
			'classes': ('collapse',)
		}),
	)
	actions = ['mark_visible', 'mark_invisible']

	def mark_visible(self, request, queryset):
		queryset.update(flag=True)

	def mark_invisible(self, request, queryset):
		queryset.update(flag=False)

	mark_visible.short_description = 'активно'
	mark_invisible.short_description = 'неактивно'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['id', 'username', 'comment', 'news']
	list_filter = ['username']
	search_fields = ['content']
	actions = ['delete_comment']

	def delete_comment(self, request, queryset):
		queryset.update(comment='Удалено администратором')

	delete_comment.short_description = 'Удалено администратором'
