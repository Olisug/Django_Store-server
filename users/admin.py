from django.contrib import admin

from .models import Profile
from products.admin import BasketAdmin


# UserAdmin.fieldsets += (
#     ('Extra Fields', {'fields': ('birth_date', )}),
# )

# admin.site.register(Profile, UserAdmin)


@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'birth_date')
    inlines = (BasketAdmin,)
