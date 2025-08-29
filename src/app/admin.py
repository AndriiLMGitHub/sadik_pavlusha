from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import GalleryPhoto
from django.utils.translation import gettext_lazy as _


class GalleryPhotoAdminForm(forms.ModelForm):
    image = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False,
        label = _("Зображення")
    )

    class Meta:
        model = GalleryPhoto
        fields = ('title', 'image')


@admin.register(GalleryPhoto)
class GalleryPhotoAdmin(admin.ModelAdmin):
    form = GalleryPhotoAdminForm

    list_display = ('title', 'image_preview', 'created_at', 'id')
    search_fields = ('title',)
    ordering = ('-created_at',)

    # 🔹 Додаємо фільтри по датах
    list_filter = ('created_at', 'modified_at')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 60px; height: auto;" />', obj.image.url)
        return "-"
    image_preview.short_description = _("Попередній перегляд")

    def save_model(self, request, obj, form, change):
        """
        Якщо користувач вибрав кілька фото,
        то для кожного створюється окремий запис GalleryPhoto
        """
        files = request.FILES.getlist('image')
        if files:
            for f in files:
                GalleryPhoto.objects.create(
                    title=obj.title or f.name,
                    image=f
                )
        else:
            super().save_model(request, obj, form, change)
