# Generated by Django 4.0.2 on 2022-02-18 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0006_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='posted',
            new_name='postname',
        ),
    ]
