# Generated by Django 4.2.8 on 2023-12-25 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_is_published_alter_comment_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Запись опубликована?'),
        ),
    ]
