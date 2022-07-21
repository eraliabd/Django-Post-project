from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')  # qanaqa field lar ko'rinishi
    list_filter = ('status', 'created', 'publish', 'author')  # qaysi fieldlar filter qilinishi
    search_fields = ('title', 'body')  # qaysi fieldlar orqali qidiruv berilishi
    prepopulated_fields = {'slug': ('title',)}  # o'zi tayyorlab olinadigan fieldlar (title ga qarab slug yasab oladi)
    raw_id_fields = ('author',)  # qatorli id fieldlar (search belgisi bosilsa barcha authorlar qator ko'rinishida choqib keladi,
                                # biron author tanlansa ushani idsi chiqib qoladi)
    date_hierarchy = 'publish'  # admin paneldagi posts modelida tepasida chop etilgan sana chiqib turishi
    ordering = ('status', 'publish')  # statusi va publishi ga qarab sartirofka(tartiblash) qilish

admin.site.register(Comment)