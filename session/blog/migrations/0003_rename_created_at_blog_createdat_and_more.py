# Generated by Django 5.0.3 on 2024-03-26 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_createdat_blog_created_at_blog_text_effects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='created_at',
            new_name='createdAt',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='text_effects',
        ),
    ]
