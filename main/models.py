from django.db import models

class Service(models.Model):
    name = models.CharField('Название услуги', max_length=200)
    description = models.TextField('Описание', blank=True)
    icon = models.CharField('Иконка', max_length=50, default='🔧')
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активна', default=True)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['order']

    def __str__(self):
        return self.name

class Price(models.Model):
    CATEGORY_CHOICES = [
        ('repair', 'Ремонтные работы'),
        ('tire', 'Шиномонтаж'),
    ]
    
    category = models.CharField('Категория', max_length=20, choices=CATEGORY_CHOICES, default='repair')
    service_name = models.CharField('Название', max_length=200)
    price = models.CharField('Цена', max_length=100)
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активна', default=True)

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
        ordering = ['category', 'order']

    def __str__(self):
        return f'{self.service_name} - {self.price}'

class Contact(models.Model):
    CONTACT_TYPE_CHOICES = [
        ('phone', 'Телефон'),
        ('email', 'Email'),
        ('address', 'Адрес'),
        ('hours', 'Режим работы'),
    ]
    
    contact_type = models.CharField('Тип', max_length=20, choices=CONTACT_TYPE_CHOICES)
    title = models.CharField('Заголовок', max_length=100, blank=True)
    value = models.TextField('Значение')
    link = models.CharField('Ссылка', max_length=200, blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активен', default=True)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['order']

    def __str__(self):
        return f'{self.title} - {self.value}'

class AboutSection(models.Model):
    SECTION_TYPE_CHOICES = [
        ('mission', 'Миссия'),
        ('advantage', 'Преимущество'),
        ('statistic', 'Статистика'),
    ]
    
    section_type = models.CharField('Тип', max_length=20, choices=SECTION_TYPE_CHOICES)
    title = models.CharField('Заголовок', max_length=200, blank=True)
    description = models.TextField('Описание', blank=True)
    value = models.CharField('Значение', max_length=100, blank=True)
    icon = models.CharField('Иконка', max_length=50, blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)
    is_active = models.BooleanField('Активен', default=True)

    class Meta:
        verbose_name = 'Секция О нас'
        verbose_name_plural = 'Секции О нас'
        ordering = ['order']

    def __str__(self):
        return self.title