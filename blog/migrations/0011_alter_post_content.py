# Generated by Django 5.1.3 on 2024-11-27 15:46

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_rename_tag_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=markdownx.models.MarkdownxField(),
        ),
    ]
