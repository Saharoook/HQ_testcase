from django.db import models


class Lesson(models.Model):
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    name = models.CharField(max_length=50,
                            verbose_name='Название урока',
                            )

    url = models.URLField(max_length=200,
                          verbose_name='Ссылка',
                          )

    duration = models.PositiveIntegerField(verbose_name='Длительность урока',
                                           )

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Проудкты'

    name = models.CharField(max_length=50,
                            verbose_name='Название курса',
                            default='Тестовый',
                            )

    owner = models.CharField(max_length=50,
                             verbose_name='Владелец',
                             )

    lessons = models.ManyToManyField(Lesson)

    def __str__(self):
        return self.name


class User(models.Model):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    data = models.CharField(max_length=200,
                            verbose_name='Имитация данных пользователя',
                            unique=True,
                            )

    products = models.ManyToManyField(Product,
                                      through='UsersToProducts',
                                      )

    lessons = models.ManyToManyField(Lesson,
                                     through='UsersToLessons',
                                     )

    def __str__(self):
        return self.data


class UsersToProducts(models.Model):

    # Сущность для связи доступа пользователей к продуктам

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             )

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                )

    def __str__(self):
        return f'{self.user.data} / {self.product}'


class UsersToLessons(models.Model):

    # Сущность для связи пользователей и уроков
    # Нужна, чтобы хранить время просмотра и статус (просмотрено/не просмотрено)

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             )

    lesson = models.ForeignKey(Lesson,
                               on_delete=models.CASCADE,
                               )

    viewing_time = models.PositiveIntegerField(default=0,
                                               verbose_name='Время просмотра',
                                               )

    status = models.BooleanField(default=False,
                                 verbose_name='Статус',
                                 )

    def __str__(self):
        return f'{self.user} / {self.lesson}'
