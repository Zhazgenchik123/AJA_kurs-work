# Generated by Django 3.2.9 on 2022-12-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20221208_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='coureses',
            name='about_course',
            field=models.TextField(blank=True, null=True, verbose_name='о курсе'),
        ),
        migrations.AlterField(
            model_name='coureses',
            name='suitable_for_whom_1',
            field=models.CharField(blank=True, default='For beginners', max_length=100, null=True, verbose_name='Кому подходит 1'),
        ),
        migrations.AlterField(
            model_name='coureses',
            name='suitable_for_whom_2',
            field=models.CharField(blank=True, default='For beginners', max_length=100, null=True, verbose_name='Кому подходит 2'),
        ),
    ]
