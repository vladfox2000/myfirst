from django.db import models

class adress(models.Model):
	first_name = models.CharField('Фамилия пользователя', max_length = 20)
	second_name = models.CharField('Имя пользователя', max_length = 20)
	l_country = models.CharField('Страна пользователя', max_length = 56)
	l_city = models.CharField('Город пользователя', max_length = 50)
	l_street = models.CharField('Улица пользователя', max_length = 50)
	phone_number = models.IntegerField('Телефон пользователя')

	class Meta:
		verbose_name = 'Адресная книга'
		verbose_name_plural = 'Адресные книги'

	def __str__(self):
		return self.first_name

class photo(models.Model):
	photo_id = models.ForeignKey(adress, on_delete = models.CASCADE, null=True)
	img = models.ImageField(upload_to='images', null=True, blank=True)
	photo_des = models.CharField('Описание', max_length = 50)

	class Meta:
		verbose_name = 'Фото пользователя'
		verbose_name_plural = 'Фотографии пользователя'