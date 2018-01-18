from django.contrib import admin

from internet_shop.models import Category, Good, Colors, Sizes

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'related_parent', 'get_level',)

    def related_parent(self, obj):
        try:
            return obj.parent.name
        except AttributeError:
            return None

    related_parent.short_description = 'Parent'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Good)
admin.site.register(Colors)
admin.site.register(Sizes)