from decimal import Decimal

from django.contrib.admin.sites import AdminSite
from django.test import SimpleTestCase

from .admin import AtencionAdmin, ClienteAdmin
from .models import Atencion, Cliente


class MontoCLPTests(SimpleTestCase):
	def test_cliente_monto_se_muestra_en_pesos_chilenos(self):
		cliente = Cliente(monto_costo=Decimal('12990.00'))
		cliente_admin = ClienteAdmin(Cliente, AdminSite())

		self.assertEqual(cliente_admin.monto_costo_formateado(cliente), '$12.990')

	def test_atencion_monto_se_muestra_en_pesos_chilenos(self):
		atencion = Atencion(monto_costo=Decimal('12990.00'))
		atencion_admin = AtencionAdmin(Atencion, AdminSite())

		self.assertEqual(atencion_admin.monto_costo_formateado(atencion), '$12.990')
