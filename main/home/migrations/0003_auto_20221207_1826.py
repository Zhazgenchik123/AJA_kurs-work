# Generated by Django 3.2.9 on 2022-12-07 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_coureses_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='coureses',
            name='text_1',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Что дает профессия'),
        ),
        migrations.AddField(
            model_name='coureses',
            name='text_2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Что дает профессия'),
        ),
        migrations.AddField(
            model_name='coureses',
            name='text_3',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Что дает профессия'),
        ),
        migrations.AddField(
            model_name='coureses',
            name='what_give_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Что дает профессия'),
        ),
    ]
