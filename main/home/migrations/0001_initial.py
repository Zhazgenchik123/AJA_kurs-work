# Generated by Django 3.2.9 on 2022-12-06 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название')),
                ('place', models.CharField(blank=True, max_length=19, null=True, verbose_name='Номер языка')),
                ('dificult', models.CharField(blank=True, max_length=19, null=True, verbose_name='Легкость')),
                ('quantity', models.CharField(blank=True, max_length=35, null=True, verbose_name='Количество программистов')),
                ('full_text_1', models.TextField(blank=True, null=True, verbose_name='статья-1')),
                ('full_text_2', models.TextField(blank=True, null=True, verbose_name='статья-2')),
                ('full_text_3', models.TextField(blank=True, null=True, verbose_name='статья-3')),
                ('full_text_4', models.TextField(blank=True, null=True, verbose_name='статья-4')),
                ('full_text_5', models.TextField(blank=True, null=True, verbose_name='статья-5')),
                ('full_text_6', models.TextField(blank=True, null=True, verbose_name='статья-6')),
                ('image', models.ImageField(blank=True, upload_to='media/img/')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Coureses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название')),
                ('title_text', models.CharField(blank=True, max_length=300, null=True, verbose_name='Описание')),
                ('duration', models.CharField(blank=True, max_length=100, null=True, verbose_name='Длительность')),
                ('price', models.CharField(blank=True, max_length=100, null=True, verbose_name='Стоимость')),
                ('komu_podhodit', models.CharField(blank=True, max_length=100, null=True, verbose_name='Кому подходит')),
                ('komu_podhodit_text', models.CharField(blank=True, max_length=300, null=True, verbose_name='Кому подходит текст')),
                ('komu_podhodit_1', models.CharField(blank=True, max_length=100, null=True, verbose_name='Кому подходит_1')),
                ('komu_podhodit_text_1', models.CharField(blank=True, max_length=300, null=True, verbose_name='Кому подходит текст_1')),
                ('profits', models.CharField(blank=True, max_length=200, null=True, verbose_name='Что дает')),
                ('person_1', models.CharField(blank=True, max_length=200, null=True, verbose_name='Первый человек')),
                ('earn_money_1', models.CharField(blank=True, max_length=200, null=True, verbose_name='сколько зарабатывает первый человек')),
                ('person_2', models.CharField(blank=True, max_length=200, null=True, verbose_name='второй человек')),
                ('earn_money_2', models.CharField(blank=True, max_length=200, null=True, verbose_name='сколько зарабатывает второй человек')),
                ('person_3', models.CharField(blank=True, max_length=200, null=True, verbose_name='Третий человек')),
                ('earn_money_3', models.CharField(blank=True, max_length=200, null=True, verbose_name='сколько зарабатывает третий человек')),
                ('first_image', models.ImageField(blank=True, null=True, upload_to='media/img/')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True, verbose_name='Имя')),
                ('vocation', models.CharField(max_length=30, null=True, verbose_name='Фамилия')),
                ('t_number', models.CharField(max_length=30, null=True, verbose_name='Ваш телефон')),
                ('href', models.TextField(max_length=350, null=True, verbose_name='Ваша ссылка')),
            ],
            options={
                'verbose_name': 'Вокансия',
                'verbose_name_plural': 'Вокансии',
            },
        ),
    ]
