# Generated by Django 4.0.2 on 2022-02-19 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0010_category_post_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='has_answer',
            field=models.BooleanField(default=True),
        ),
    ]
