from django.db import models


class Client(models.Model):
    name = models.CharField('ФИО', max_length=200)
    birthday = models.DateField('День рождения', null=True)
    contact = models.CharField('Телефон', max_length=200)
    address = models.CharField('Адрес', max_length=200)


class Courier(models.Model):
    name = models.CharField('ФИО', max_length=200)
    contact = models.CharField('Телефон', max_length=200)


class Cake(models.Model):
    levels = (
        ('1 уровень', '1 уровень'),
        ('2 уровня', '2 уровня'),
        ('3 уровня', '3 уровня'),
    )
    number_of_levels = models.ChoiceField(choices=levels)
    forms = (
        ('Квадрат', 'Квадрат'),
        ('Круг', 'Круг'),
        ('Прямоугольник', 'Прямоугольник'),
    )
    form = models.ChoiceField(choices=forms)
    toppings = (
        ('Без топпинга', 'Без топпинга'),
        ('Белый соус', 'Белый соус'),
        ('Карамельный сироп', 'Карамельный сироп'),
        ('Кленовый сироп', 'Кленовый сироп'),
        ('Клубничный сироп', 'Клубничный сироп'),
        ('Черничный сироп', 'Черничный сироп'),
        ('Молочный шоколад', 'Молочный шоколад'),
    )
    topping = models.ChoiceField(choices=toppings)
    berry_variety = (
        ('Ежевика', 'Ежевика'),
        ('Малина', 'Малина'),
        ('Голубика', 'Голубика'),
        ('Клубника', 'Клубника'),
    )
    berries = models.ChoiceField(choices=berry_variety, null=True)
    decor_variety = (
        ('Фисташки', 'Фисташки'),
        ('Безе', 'Безе'),
        ('Фундук', 'Фундук'),
        ('Пекан', 'Пекан'),
        ('Маршмеллоу', 'Маршмеллоу'),
        ('Марципан', 'Марципан'),
    )
    decor = models.ChoiceField(choices=decor_variety, null=True)
    inscription = models.CharField('Введите поздравительную надпись', max_length=100, null=True)
    price


class Order(models.Model):
    client = models.ForeignKey(Client)
    date_time = models.DateTimeField(auto_now_add=True)
    cake = models.ForeignKey(Cake)
    comment = models.CharField('Комментарий к заказу', max_length=200)
    delivery_address = models.CharField('Адрес доставки', max_length=200,
                                        default=client__address)  # По умолчанию адрес клиента, не знаю как обратиться
    delivery_date = models.DateField('Дата доставки')
    delivery_time = models.TimeField('Желаемое время доставки')
    payment = models.BooleanField(default=True)


class Delivery(models.Model):
    order = models.ForeignKey(Order)
    courier = models.ForeignKey(Courier)
    delivery_time = models.DateTimeField('Предполагаемое время доставки')
