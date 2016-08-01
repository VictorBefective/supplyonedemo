# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from users.models import Document, Provider, Orden
from django.shortcuts import get_object_or_404


@user_passes_test(lambda user: user.is_authenticated())
def tablero(request):
	return render(request, 'tablero.html', locals())

@user_passes_test(lambda user: user.is_authenticated())
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/login')

@user_passes_test(lambda user: user.is_authenticated())
def ver_proveedor(request, id_proveedor):
	provider = get_object_or_404(Provider, id=id_proveedor)
	success = False
	print request.POST, request.FILES
	if request.method == "POST":
		if request.POST['password'] == request.POST['password_confirmation']:
			if request.POST['password'] != '' and request.POST['password_confirmation']:
				provider.password = request.POST['password']
			if request.FILES.get('logo'):
				provider.logo = request.FILES.get('logo')
			provider.name = request.POST.get('name')
			provider.lastname = request.POST.get('lastname')
			provider.company = request.POST.get('company')
			provider.emails = request.POST.get('emails')
			provider.street = request.POST.get('street')
			provider.exterior = request.POST.get('exterior')
			provider.interior = request.POST.get('interior')
			provider.colonia = request.POST.get('colonia')
			provider.municipio = request.POST.get('municipio')
			provider.cp = request.POST.get('cp')
			provider.estado = request.POST.get('estado')
			provider.rfc = request.POST.get('rfc')
			provider.phone = request.POST.get('phone')
			provider.riesgo = request.POST.get('riesgo')
			provider.observaciones = request.POST.get('observaciones')
			provider.servicios_productos = request.POST.get('servicios_productos')
			provider.puesto = request.POST.get('puesto')
			provider.save()
			success = True

		else:
			error = "Las contraseñas no coincide, por favor verifiquelas"

	return render(request, 'perfil.html', locals())


@user_passes_test(lambda user: user.is_authenticated())
def alta_proveedor(request):
	error = ""
	if request.method == "POST":
		if request.POST.get('password') == request.POST.get('password_confirmation'):
			provider = Provider()
			provider.name = request.POST.get('name')
			provider.lastname = request.POST.get('lastname')
			provider.company = request.POST.get('company')
			provider.emails = request.POST.get('emails')
			provider.street = request.POST.get('street')
			provider.exterior = request.POST.get('exterior')
			provider.interior = request.POST.get('interior')
			provider.colonia = request.POST.get('colonia')
			provider.municipio = request.POST.get('municipio')
			provider.cp = request.POST.get('cp')
			provider.estado = request.POST.get('estado')
			provider.rfc = request.POST.get('rfc')
			provider.password = request.POST.get('password')
			provider.phone = request.POST.get('phone')
			provider.observaciones = request.POST.get('observaciones')
			provider.servicios_productos = request.POST.get('servicios_productos')
			provider.riesgo = request.POST.get('riesgo')
			provider.puesto = request.POST.get('puesto')
			provider.logo = request.FILES.get('logo')
			provider.save()
			for document in request.FILES.getlist('attachment[]'):
				doc = Document()
				doc.document = document
				doc.provider = provider
				doc.save()
			return HttpResponseRedirect('/')
		else:
			error = "Las contraseñas no coinciden"
	return render(request, 'alta.html', locals())

@user_passes_test(lambda user: user.is_authenticated())
def ordenes(request):
	ordenes = Orden.objects.all()
	return render(request, 'solicitudes.html', locals())

@user_passes_test(lambda user: user.is_authenticated())
def orden(request, id_orden):
	orden = get_object_or_404(Orden, id=id_orden)
	return render(request, 'orden_compra.html', locals())


@user_passes_test(lambda user: user.is_authenticated())
def proveedores(request):
	provedores = Provider.objects.all()
	return render(request, 'proveedores.html', locals())

	

def login_view(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	error = ""
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=email, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')

			else:
				error = "Tu usuario no está activo, por favor contacta a tu supervisor o al centro de atenciónd de supplyone"

		else:
			error = "Login inválido  por favor valida el e-mail y contraseña"
	return render(request, 'login.html', locals())