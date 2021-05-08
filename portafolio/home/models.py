from django.db import models

from wagtail.core.models import Page
from wagtail.admin import edit_handlers
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    about_me = models.TextField(max_length=255, blank=True, null=True)
    photo = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        edit_handlers.MultiFieldPanel([
            edit_handlers.FieldPanel('name', 'Mi nombre'),
            edit_handlers.FieldPanel('last_name', 'Mi apellido'),
            edit_handlers.FieldPanel('address', 'Dirección'),
            edit_handlers.FieldPanel('email', 'Correo'),
            edit_handlers.FieldPanel('phone_number', 'Número telofónico'),
            edit_handlers.FieldPanel('about_me', 'Acerca de mi')
        ], "Información Básica"),
        ImageChooserPanel('photo', 'Foto de Perfil')
    ]
