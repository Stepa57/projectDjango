# Generated by Django 4.2.8 on 2023-12-24 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_is_published_alter_post_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_published',
        ),
        migrations.AlterField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
