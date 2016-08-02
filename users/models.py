# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
import random

# Create your models here.

class CommonModel(models.Model):

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	activated = models.BooleanField(default=True)
	
	class Meta:
		abstract = True

def upload_logo_organization(instance, filename):
	return 'organization_{0}/{1}'.format(instance.id, filename)

class Organization(CommonModel):
	name = models.CharField(max_length=100)
	logo = models.ImageField(upload_to=upload_logo_organization, null=True)


class Contact(CommonModel):
	name = models.CharField(max_length=100)
	role = models.CharField(max_length=20)
	email = models.EmailField(max_length=254)
	phone = models.CharField(max_length=15)
	cellphone = models.CharField(max_length=15, null=True)
	provider = models.ForeignKey('Provider')


class DocumentType(CommonModel):
	name = models.CharField(max_length=100)




def save_document(instance, filename):
	return 'provider_{0}/{1}'.format(instance.provider.id, filename)

class Document(CommonModel):
	#document_type = models.ForeignKey('DocumentType')
	provider = models.ForeignKey('Provider')
	document = models.FileField(upload_to = save_document)
	

def upload_logo_provider(instance, filename):
	return 'provider_{0}/{1}'.format(instance.id, filename)


class Provider(CommonModel):
	name = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	puesto = models.CharField(max_length=100)
	company = models.CharField(max_length=100)
	emails = models.EmailField(max_length=100)
	street = models.CharField(max_length=100)
	exterior = models.CharField(max_length=100)
	interior = models.CharField(max_length=100, null=True)
	colonia = models.CharField(max_length=100, null=True)
	municipio = models.CharField(max_length=100, null=True)
	cp = models.CharField(max_length=100)
	estado = models.CharField(max_length=100)
	rfc = models.CharField(max_length=30, null=True)
	password = models.CharField(max_length=256)
	phone = models.CharField(max_length=100)
	observaciones = models.TextField(null=True)
	servicios_productos = models.TextField()
	riesgo = models.IntegerField()
	calificacion = models.IntegerField()
	logo = models.ImageField(upload_to=upload_logo_provider, null=True)

	def save(self, *args, **kwargs):
		self.calificacion = random.randint(1,5)
		super(Provider, self).save(*args, **kwargs)


	def get_name(self):
		return '{0} {1}'.format(self.name, self.lastname)

	def get_servicios(self):
		return self.servicios_productos.split(',')


	def get_calificacion(self):
		return range(0, self.calificacion)

	def get_riesgo(self):
		return range(0, int(self.riesgo))

	def get_activado(self):
		return "Sí" if self.activated else "No"

class CustomUserManager(BaseUserManager):


	def _create_user(self, email, full_name, password, is_staff, is_superuser, organization_id, user_type):
		if not email or not full_name or not password or not organization_id or not user_type:
			raise ValueError('All of the fields must be set')

		email = self.normalize_email(email)
		user = self.model(email=email, full_name=full_name, is_active=True, is_staff=is_staff,
			is_superuser=is_superuser, organization_id=organization_id, user_type=user_type)
		user.set_password(password)
		user.save()
		return user

	def create_user(self, email, full_name, is_staff, is_superuser, organization, user_type, password=None):
		return self._create_user(email, full_name, password, is_staff, is_superuser, organization, user_type)
	
	def create_superuser(self, email, full_name, organization, user_type, password=None):
		return self._create_user(email, full_name, password, True, True,
        						organization, user_type)

def upload_avatar(instance, filename):
	return 'avatars/{0}'.format(filename)


class User(AbstractBaseUser, CommonModel, PermissionsMixin):

	USER_TYPE_CHOICES = (
		('provider',  'Provider'),
		('internal', 'Internal')

		)
	organization = models.ForeignKey('Organization')
	user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
	full_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=254, unique=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	avatar = models.ImageField(upload_to=upload_avatar, null=True)


	objects = CustomUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['user_type', 'full_name', 'organization']

	def get_full_name(self):
		return self.full_name

	def get_short_name(self):
		return self.get_full_name()

	def get_name(self):
		return self.get_full_name()

class ServicioOrden(CommonModel):
	serivicio_producto = models.CharField(max_length=100)
	unidades = models.IntegerField(default=1)
	subtotal = models.DecimalField(max_digits=14, decimal_places=2, null=True, default=0)
	iva = models.DecimalField(max_digits=14, decimal_places=2, null=True, default=0)
	total = models.DecimalField(max_digits=14, decimal_places=2, null=True, default=0)
	descripcion = models.CharField(max_length=100, null=True)
	orden = models.ForeignKey('Orden')

	
class Orden(CommonModel):
	provider = models.ForeignKey('Provider')
	to_user = models.ForeignKey('User')
	fecha_de_pago = models.DateField(null=True)
	status = models.CharField(max_length=20, default="Activada")
	envio = models.DecimalField(max_digits=14, decimal_places=2, null=True, default=0)
	urgencia = models.CharField(max_length=20)
	observaciones = models.CharField(max_length=100, null=True)
	area = models.CharField(max_length=100)
	
	def active(self):
		if self.status == "Activada":
			return "active"
		if self.status == "Suspendida":
			return "suspended"
		if self.status == "Finalizada":
			return "disabled"

	def productos(self):
		s = self.servicioorden_set.all()
		m = ""
		for l in s:
			m += ' {0} {1}'.format(l.unidades, l.serivicio_producto)
		return m

	def subtotal(self):
		if None in self.servicioorden_set.values_list('subtotal', flat=True):
			return 0
		return sum(self.servicioorden_set.values_list('subtotal', flat=True))

	def iva(self):
		if None in self.servicioorden_set.values_list('iva', flat=True):
			return 0
		return sum(self.servicioorden_set.values_list('iva', flat=True))

	def total(self):
		return self.subtotal() + self.iva() + (self.envio or 0)