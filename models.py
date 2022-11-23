from django.db import models

class Client(models.Model):
    name =  models.CharField('ФИО', max_length=200)
    birthday = models.DateField('День рождения', null=True)
    contact = models.CharField('Телефон', max_length=200)
    address = models.CharField('Адрес', max_length=200)


class Courier(models.Model):
    name =  models.CharField('ФИО', max_length=200)
    contact = models.CharField('Телефон', max_length=200)


class Order(models.Model):
    client = models.ForeignKey(Client)
    date_time = models.DateField('Дата заказа') #Автоподстановка
    cake = models.ForeignKey(Cake)
    comment = models.CharField('Комментарий к заказу', max_length=200)
    delivery_address = models.CharField('Адрес доставки', max_length=200) #По умолчанию адрес клиента
    delivery_date = models.DateField('Дата доставки')
    delivery_time = models.DateField('Желаемое время доставки')
    payment # Заглушка


class Cake(models.Model):
    number_of_levels = models.MultipleChoiceField(choices=['1 уровень', '2 уровня', '3 уровня'])
    form = models.MultipleChoiceField(choices=['Квадрат', 'Круг', 'Прямоугольник'])
    topping
    berries
    decor
    inscription
    price


class Delivery(models.Model):
    order = models.ForeignKey(Order)
    courier = models.ForeignKey (Сourier)
    delivery_time = models.DateField('Предполагаемое время доставки')
