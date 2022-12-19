from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=100, null=True, blank=True)
    place = models.CharField('Номер языка', max_length=19, null=True, blank=True)
    dificult = models.CharField('Легкость', max_length=19, null=True, blank=True)
    quantity = models.CharField('Количество программистов', max_length=35, null=True, blank=True)
    advantage_1 = models.CharField('Примущество-1', max_length=550, null=True, blank=True)
    advantage_2 = models.CharField('Примущество-2', max_length=550, null=True, blank=True)
    advantage_3 = models.CharField('Примущество-3', max_length=550, null=True, blank=True)
    disadvantage_1 = models.CharField('Недостаток-1', max_length=550, null=True, blank=True)
    disadvantage_2 = models.CharField('Недостаток-2', max_length=550, null=True, blank=True)
    disadvantage_3 = models.CharField('Недостаток-3', max_length=550, null=True, blank=True)
    full_text_1 = models.TextField('о языке', null=True, blank=True)
    full_text_2 = models.TextField('текст под заголовкам', null=True, blank=True)

    date = models.DateField('Дата', null=True, blank=True)

    image = models.ImageField(upload_to='media/img/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'язык программирования'
        verbose_name_plural = 'языки программирования'


class Job(models.Model):
    name = models.CharField('Имя', null=True, max_length=30)
    vocation = models.CharField('Фамилия', null=True, max_length=30)
    t_number = models.CharField('Ваш телефон', null=True, max_length=30)
    href = models.TextField('Ваша ссылка', null=True, max_length=350)

    def __str__(self):
        return self.vocation

    class Meta:
        verbose_name = 'Вокансия'
        verbose_name_plural = 'Вокансии'


class Coureses(models.Model):
    title = models.CharField('Название', max_length=100, null=True, blank=True)
    title_text = models.CharField('Описание', max_length=300, null=True, blank=True)
    duration = models.CharField('Длительность', max_length=100, null=True, blank=True)
    price = models.CharField('Стоимость', max_length=100, null=True, blank=True)
    start_time = models.TextField('С какого времени работает', max_length=100, null=True, blank=True)

    detail_title = models.CharField('Детальное название', max_length=100, null=True, blank=True)
    detail_title_text = models.CharField('Текст в деталях', max_length=100, null=True, blank=True)
    suitable_for_whom_1 = models.CharField('Кому подходит 1', max_length=100, null=True, blank=True, default='For beginners')
    suitable_for_whom_text_1 = models.CharField('Кому подходит текст 1', max_length=300, null=True, blank=True)
    suitable_for_whom_2 = models.CharField('Кому подходит 2', max_length=100, null=True, blank=True, default='For beginners')
    suitable_for_whom_text_2 = models.CharField('Кому подходит текст 2', max_length=300, null=True, blank=True)
    profits = models.CharField('Что дает', max_length=200, null=True, blank=True)

    person_1 = models.CharField('Первый человек', max_length=200, null=True, blank=True)
    earn_money_1 = models.CharField('сколько зарабатывает первый человек', max_length=200, null=True, blank=True)
    person_href_1 = models.CharField('ссылка на первого', max_length=200, null=True, blank=True)

    person_2 = models.CharField('второй человек', max_length=200, null=True, blank=True)
    earn_money_2 = models.CharField('сколько зарабатывает второй человек', max_length=200, null=True, blank=True)
    person_href_2 = models.CharField('ссылка на второго', max_length=200, null=True, blank=True)

    person_3 = models.CharField('Третий человек', max_length=200, null=True, blank=True)
    earn_money_3 = models.CharField('сколько зарабатывает третий человек', max_length=200, null=True, blank=True)
    person_href_3 = models.CharField('ссылка на третьего', max_length=200, null=True, blank=True)

    date = models.DateField('Дата', null=True)
    first_image = models.ImageField(upload_to='media/img/', blank=True, null=True)
    what_give_title = models.CharField('Что дает профессия', max_length=100, null=True, blank=True)
    text_1 = models.CharField('Что дает профессия 1', max_length=250, null=True, blank=True)
    text_2 = models.CharField('Что дает профессия 2', max_length=250, null=True, blank=True)
    text_3 = models.CharField('Что дает профессия 3', max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to='media/img/', blank=True, null=True)
    about_course = models.TextField('о курсе', null=True, blank=True)
    course_href = models.TextField('сслыка', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Aja_look(models.Model):
    image = models.ImageField(upload_to='media/img/', blank=True, null=True)
    title = models.CharField('текст', max_length=250, blank=True, null=True)



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'