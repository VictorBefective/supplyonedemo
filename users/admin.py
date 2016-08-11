from django.contrib import admin
from users.models import (Organization, Contact, DocumentType,
	Document, Provider, User, Orden, ServicioOrden, CalificacionOrden)
# Register your models here.

admin.site.register(Orden)
admin.site.register(ServicioOrden)
admin.site.register(Organization)
admin.site.register(Contact)
admin.site.register(DocumentType)
admin.site.register(Document)
admin.site.register(Provider)
admin.site.register(User)
admin.site.register(CalificacionOrden)