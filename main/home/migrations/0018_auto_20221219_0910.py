# Generated by Django 3.2.9 on 2022-12-19 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20221218_1815'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'язык программирования', 'verbose_name_plural': 'языки программирования'},
        ),
        migrations.RemoveField(
            model_name='articles',
            name='full_text_3',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='full_text_4',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='full_text_5',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='full_text_6',
        ),
    ]
