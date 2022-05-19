from django.contrib import admin
from .models import Player, Category, Team

admin.site.register(Player)

# class CategoryAdmin(admin.ModelAdmin): # category모델의 name 필드에 값이 입력되면 자동으로 slug가 만들어짐
#     prepopulated_fields = {
#         'slug': ('categoryName', )
#     }
admin.site.register(Category)
admin.site.register(Team)
# Register your models here.
