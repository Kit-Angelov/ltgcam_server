from django.db import models
from django.utils import timezone


class Photo(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фото регистраторов'
        verbose_name_plural = "Фото регистраторов"


class VideoExample(models.Model):
    name = models.CharField(max_length=100)
    link = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пример видео'
        verbose_name_plural = "Примеры видео"


class Options(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:15]

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = "Характеристики"


class MainOptions(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:15]

    class Meta:
        verbose_name = 'Основные параметры'
        verbose_name_plural = "Основные параметры"


class Description(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:15]

    class Meta:
        verbose_name = 'Описание товара'
        verbose_name_plural = "Описания товаров"


class Mark(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Марка авто'
        verbose_name_plural = "Марки авто"


class AutoModel(models.Model):
    main_photo = models.ForeignKey('Photo', on_delete=models.DO_NOTHING, related_name='main_photo')
    description = models.ForeignKey('Description', on_delete=models.DO_NOTHING)
    galery_photo = models.ManyToManyField('Photo', related_name='galery_photo')
    options = models.ManyToManyField('Options')
    main_options = models.ManyToManyField('MainOptions')
    video = models.ForeignKey('VideoExample', on_delete=models.DO_NOTHING, blank=True, null=True)
    mark = models.ForeignKey('Mark', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return '{} {}; {}'.format(self.mark.name, self.name, str(self.price))

    class Meta:
        verbose_name = 'Модель авто'
        verbose_name_plural = "Модели авто"


class OrderCall(models.Model):
    time = models.DateTimeField(default=timezone.now())
    fio = models.TextField()
    phone = models.CharField(max_length=100)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{}; {}; {}'.format(str(self.time)[:19], self.fio, self.phone)

    class Meta:
        verbose_name = 'Заказ звонка'
        verbose_name_plural = "Заказы звонка"


class PartnersCall(models.Model):
    time = models.DateTimeField(default=timezone.now())
    fio = models.TextField()
    company = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{}; {}; {}; {}; {}'.format(str(self.time)[:19], self.fio, self.phone, self.email, self.company)

    class Meta:
        verbose_name = 'Заказ звонка партнера'
        verbose_name_plural = "Заказы звонка партнера"


class OrderBuy(models.Model):
    time = models.DateTimeField(default=timezone.now())
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=150)
    index = models.CharField(max_length=50)
    address = models.TextField()
    pay_var = models.CharField(choices=[('card', 'card'), ('cash', 'cash')], max_length=50, default='card')
    sum = models.IntegerField()
    basket = models.ManyToManyField('AutoModel')

    def __str__(self):
        return '{}; {}; {}'.format(str(self.time)[:19], self.name, self.phone, self.email, str(self.sum))

    class Meta:
        verbose_name = 'Оформление покупки'
        verbose_name_plural = "Оформления покупки"
