from django.db import models
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.core.fields import StreamField

from wagtail.core.models import Page
from wagtail.admin import edit_handlers
from wagtail.images.edit_handlers import ImageChooserPanel

from . import blocks
from . import fields


class HomePage(Page):
    name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    about_me = fields.BoldAndItalicRichTextField(
        "Acerca de mi",
        null=True,
        blank=True
    )
    photo = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='+'
    )

    experiences = StreamField([
        ('experiences', blocks.ExperienceBlock()),
    ], null=True, blank=True)

    studies = StreamField([
        ('studies', blocks.StudyBlock()),
    ], null=True, blank=True)

    skills_and_workflows = StreamField([
        ('skills', blocks.SkillBlock()),
        ('workflows', blocks.WorkflowBlock()),
    ], null=True, blank=True)

    interests = fields.BoldAndItalicRichTextField(
        "Mis Intereses",
        null=True,
        blank=True
    )

    awards = StreamField([
        ('awards', blocks.AwardBlock())
    ], null=True, blank=True)

    content_panels = Page.content_panels + [
        edit_handlers.MultiFieldPanel([
            edit_handlers.FieldPanel('name'),
            edit_handlers.FieldPanel('last_name'),
            edit_handlers.FieldPanel('address'),
            edit_handlers.FieldPanel('email'),
            edit_handlers.FieldPanel('phone_number'),
            edit_handlers.FieldPanel('about_me', classname="lead")
        ], heading="Información Básica"),
        ImageChooserPanel('photo', 'Foto de Perfil'),
        edit_handlers.MultiFieldPanel([
            edit_handlers.StreamFieldPanel('experiences'),
            edit_handlers.StreamFieldPanel('studies'),
            edit_handlers.StreamFieldPanel('skills_and_workflows'),
            edit_handlers.StreamFieldPanel('awards'),
        ], "Información Profesional"),
        edit_handlers.MultiFieldPanel([
            edit_handlers.FieldPanel('interests'),
        ], heading="Gustos, Intereses, etc")
    ]


@register_setting(icon="placeholder")
class SocialMediaSetting(BaseSetting):
    facebook = models.URLField(
        help_text="Link a tu cuenta de Facebook",
        blank=True,
        null=True
    )
    github = models.URLField(
        help_text="Link a tu cuenta de GitHub",
        blank=True,
        null=True
    )
    gitlab = models.URLField(
        help_text="Link a tu cuenta de GitLab",
        blank=True,
        null=True
    )
    linkedin = models.URLField(
        help_text="Link a tu cuenta de Linkedin",
        blank=True,
        null=True
    )
    instagram = models.URLField(
        help_text="Link a tu cuenta de Instagram",
        blank=True,
        null=True
    )

    panels = [
        edit_handlers.FieldPanel('facebook'),
        edit_handlers.FieldPanel('github'),
        edit_handlers.FieldPanel('gitlab'),
        edit_handlers.FieldPanel('linkedin'),
        edit_handlers.FieldPanel('instagram'),
    ]

    class Meta:
        verbose_name = "Configuración de Redes Sociales"
