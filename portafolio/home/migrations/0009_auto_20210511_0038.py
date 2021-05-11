# Generated by Django 3.1.8 on 2021-05-11 00:38

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210510_0234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='skills',
        ),
        migrations.AddField(
            model_name='homepage',
            name='skills_and_workflows',
            field=wagtail.core.fields.StreamField([('skills', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.CharBlock(help_text='Escribe el nombre del Icono. Ej. fa-node-js'))])), ('workflows', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(max_length=80))]))], blank=True, null=True),
        ),
    ]
