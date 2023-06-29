from django.contrib import admin
from core.models import Categoria, Editora, Autor, Livro, Compra, ItensCompra

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)


class ItensInline(admin.TabularInline):
    model = ItensCompra


class CompraAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = (
        ItensInline,
    )


admin.site.register(Compra, CompraAdmin)
