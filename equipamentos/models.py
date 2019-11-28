from django.conf import settings
from django.db import models
from django.utils import timezone

class Equipamentos(models.Model):
	autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	patrimonio = models.CharField(max_length=50)
	marca = models.CharField(max_length=50)
	modelo = models.CharField(max_length=50)
	serial = models.CharField(max_length=50)
	descricao = models.TextField()
	data_cadastro = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.data_cadastro = timezone.now()
		self.save()

	def __str__(self):
		return self.patrimonio