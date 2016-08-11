# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from users.models import Document, Provider, Orden, ServicioOrden, PreCalificacionCuestionario, CalificacionOrden, Producto
from django.shortcuts import get_object_or_404
import os

@user_passes_test(lambda user: user.is_authenticated())
def tablero(request):
	return render(request, 'tablero.html', locals())

@user_passes_test(lambda user: user.is_authenticated())
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/login')

@user_passes_test(lambda user: user.is_authenticated())
def graficas(request):
	return render(request, 'grafica.html', locals())

@user_passes_test(lambda user: user.is_authenticated())
def evaluar_proveedor(request, id_proveedor):
	provider = get_object_or_404(Provider, id=id_proveedor)
	try:
		id_cuestionario = PreCalificacionCuestionario.objects.get(proveedor=provider)
	except:
		id_cuestionario = None
	if request.method == "POST":
		if not id_cuestionario:
			id_cuestionario = PreCalificacionCuestionario()
			id_cuestionario.proveedor = provider
		id_cuestionario.fecha_evaluacion = request.POST['fecha_evaluacion']
		id_cuestionario.auditor = request.POST['auditor']
		id_cuestionario.telefono = request.POST['telefono']
		id_cuestionario.email = request.POST['email']
		id_cuestionario.ins1 = request.POST['ins1']
		id_cuestionario.ins2 = request.POST['ins2']
		id_cuestionario.ins3 = request.POST['ins3']
		id_cuestionario.ins4 = request.POST['ins4']
		id_cuestionario.ins5 = request.POST['ins5']
		id_cuestionario.ins6 = request.POST['ins6']
		id_cuestionario.ins7 = request.POST['ins7']
		id_cuestionario.ins8 = request.POST['ins8']
		id_cuestionario.inp1 = request.POST['inp1']
		id_cuestionario.inp2 = request.POST['inp2']
		id_cuestionario.inp3 = request.POST['inp3']
		id_cuestionario.inp4 = request.POST['inp4']
		id_cuestionario.inp5 = request.POST['inp5']
		id_cuestionario.inp6 = request.POST['inp6']
		id_cuestionario.inp7 = request.POST['inp7']
		id_cuestionario.inp8 = request.POST['inp8']
		id_cuestionario.dpp1 = request.POST['dpp1']
		id_cuestionario.dpp2 = request.POST['dpp2']
		id_cuestionario.sg1 = request.POST['sg1']
		id_cuestionario.sg2 = request.POST['sg2']
		id_cuestionario.sg3 = request.POST['sg3']
		id_cuestionario.sg4 = request.POST['sg4']
		id_cuestionario.sg5 = request.POST['sg5']
		id_cuestionario.tec1 = request.POST['tec1']
		id_cuestionario.tec2 = request.POST['tec2']
		id_cuestionario.tec3 = request.POST['tec3']
		id_cuestionario.tec4 = request.POST['tec4']
		id_cuestionario.tec5 = request.POST['tec5']
		id_cuestionario.save()
		provider.status = request.POST['estatus']
		provider.calificacion = request.POST['calificacion']
		provider.save()
		return HttpResponseRedirect('/proveedores/ver/{0}/'.format(provider.id))

	return render(request, 'evaluar.html', locals())

@user_passes_test(lambda user: user.is_authenticated())
def orden_evaluacion(request, id_orden):
	orden = get_object_or_404(Orden, id=id_orden)
	try:
		id_cuestionario = CalificacionOrden.objects.get(orden=orden)
	except:
		id_cuestionario = None
	if request.method == "POST":
		oc = CalificacionOrden()
		oc.recibio = request.POST['recibio']
		oc.fecha_evaluacion = request.POST['fecha_evaluacion']
		oc.orden = orden
		oc.cp1 = True if request.POST.get('cp1', False) else False
		oc.cp2 = True if request.POST.get('cp2', False) else False
		oc.cc1 = True if request.POST.get('cc1', False) else False
		oc.sp1 = True if request.POST.get('sp1', False) else False
		oc.sp2 = True if request.POST.get('sp2', False) else False
		oc.sp3 = True if request.POST.get('sp3', False) else False
		oc.c1 = 0 if request.POST.get('c1') == '' else int(request.POST.get('c1'))
		oc.c2 = 0 if request.POST.get('c2') == '' else int(request.POST.get('c2'))
		oc.c3 = 0 if request.POST.get('c3') == '' else int(request.POST.get('c3'))
		oc.save()
		orden.provider.calificacion = ((orden.provider.calificacion or 0) + orden.calificacion_gral()) / 2.0
		orden.provider.save()
		orden.save()
		return HttpResponseRedirect('/orden/{0}/'.format(orden.id))
	return render(request, 'evaluacion_compras.html', locals())

@user_passes_test(lambda user: user.is_authenticated())
def ver_proveedor(request, id_proveedor):
	provider = get_object_or_404(Provider, id=id_proveedor)
	success = False
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
			#provider.servicios_productos = request.POST.get('servicios_productos')
			provider.puesto = request.POST.get('puesto')
			provider.save()
			success = True
			to_not_delete = []
			if success:
				products_names = request.POST.getlist('producto_nombres[]')
				logos = request.POST.getlist('original_images_names[]')
				for n in enumerate(products_names):
					pr = Producto.objects.get(provider=provider, deleted=False, nombre=n[1])
					to_not_delete.append(pr.id)
					pr.descripcion = request.POST.getlist('descripcion_original[]')[n[0]]
					if logos[n[0]] != pr.logo.name:
						logos_files = request.FILES.getlist('productos_original[]')
						for l in logos_files:
							if l.name == logos[n[0]]:
								pr.logo = l
					pr.save()
				Producto.objects.filter(provider=provider).exclude(id__in=to_not_delete).update(deleted=True)
				productos_nuevos = request.POST.getlist('producto_nuevo[]')
				for p in enumerate(productos_nuevos):
					o = Producto()
					o.nombre = p[1]
					o.logo = request.FILES.getlist('productos_nuevos[]')[p[0]]
					o.provider = provider
					o.descripcion = request.POST.getlist('descripcion_nuevo[]')[p[0]]
					o.save()

		else:
			error = "Las contraseñas no coincide, por favor verifiquelas"

	return render(request, 'perfil.html', locals())


# u'productos_original[]': [u'', u''], u'colonia': [u'k'],
# u'descripcion_original[]': [u'Soy el producto 1', u'soy 2']
# u'original_images_names[]': [u'provider_8/kkkkkk.jpg', u'provider_8/zelonka.jpg']
# u'producto_nombres[]': [u'Producto 1', u'2']

@user_passes_test(lambda user: user.is_authenticated())
def desempeno(request):
	provedores = Provider.objects.all()
	return render(request, 'desempeno.html', locals())

@user_passes_test(lambda user: user.is_authenticated())
def desempeno_ver(request, id_proveedor):
	provedor = get_object_or_404(Provider, id=id_proveedor)
	ordenes = Orden.objects.filter(provider=provedor)
	id_ordenes = map( lambda x: int(x), ordenes.values_list('id', flat=True))
	data_1 = map(lambda x: int(x), CalificacionOrden.objects.filter(orden__in=id_ordenes).values_list('c1', flat=True))
	data_2 = map(lambda x: int(x), CalificacionOrden.objects.filter(orden__in=id_ordenes).values_list('c2', flat=True))
	data_3 = map(lambda x: int(x), CalificacionOrden.objects.filter(orden__in=id_ordenes).values_list('c3', flat=True))
	return render(request, 'grafica2.html', locals())

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
			for p in request.POST.getlist('producto[]'):
				pro = Producto()
				pro.nombre = p
				pro.descripcion = request.POST.getlist('descripcion[]')[request.POST.getlist('producto[]').index(p)]
				pro.logo = request.FILES.getlist('productos[]')[request.POST.getlist('producto[]').index(p)]
				pro.provider = provider
				pro.save()
			return HttpResponseRedirect('/proveedores/{0}/evaluar/'.format(provider.id))
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
	if request.method == "POST":
		estatus = request.POST['status']
		orden.status = estatus
		orden.save()
		if estatus == "Finalizada":
			return HttpResponseRedirect('/orden/{0}/evaluar/'.format(orden.id))
	return render(request, 'orden_compra.html', locals())


@user_passes_test(lambda user: user.is_authenticated())
def proveedores(request):
	provedores = Provider.objects.all()
	return render(request, 'proveedores.html', locals())

@user_passes_test(lambda user: user.is_authenticated())
def crear_orden(request):
	provedores = Provider.objects.all()
	if request.method == "POST":
		orden = Orden()
		orden.urgencia = request.POST.get('urgencia')
		orden.area = request.POST.get('area_solicitante')
		orden.to_user = request.user
		orden.provider_id = request.POST.get('provedor')
		orden.observaciones = request.POST.get('observaciones')
		orden.save()
		q1,s1 = request.POST.get('q1'), request.POST.get('s1')
		q2,s2 = request.POST.get('q2'), request.POST.get('s2')
		q3,s3 = request.POST.get('q3'), request.POST.get('s3')
		q4,s4 = request.POST.get('q4'), request.POST.get('s4')
		q5,s5 = request.POST.get('q5'), request.POST.get('s5')
		if q1 and s1:
			ServicioOrden.objects.create(serivicio_producto =s1, unidades=q1, orden=orden)
		if q2 and s2:
			ServicioOrden.objects.create(serivicio_producto =s2, unidades=q2, orden=orden)
		if q3 and s3:
			ServicioOrden.objects.create(serivicio_producto =s3, unidades=q3, orden=orden)
		if q4 and s4:
			ServicioOrden.objects.create(serivicio_producto =s4, unidades=q4, orden=orden)
		if q5 and s5:
			ServicioOrden.objects.create(serivicio_producto =s5, unidades=q5, orden=orden)
		return HttpResponseRedirect('/orden/{0}/'.format(orden.id))
	return render(request, 'alta_orden.html', locals())
	

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