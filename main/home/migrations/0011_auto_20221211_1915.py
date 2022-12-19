# Generated by Django 3.2.9 on 2022-12-11 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20221211_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='advantage_1',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Примущество-1'),
        ),
        migrations.AddField(
            model_name='articles',
            name='advantage_2',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Примущество-2'),
        ),
        migrations.AddField(
            model_name='articles',
            name='advantage_3',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Примущество-3'),
        ),
        migrations.AlterField(
            model_name='coureses',
            name='text_1',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Что дает профессия 1'),
        ),
        migrations.AlterField(
            model_name='coureses',
            name='text_2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Что дает профессия 2'),
        ),
        migrations.AlterField(
            model_name='coureses',
            name='text_3',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Что дает профессия 3'),
        ),
    ]
