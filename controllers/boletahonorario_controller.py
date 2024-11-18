from SimpleFacturaSDK.services.BoletaHonorarioService import BoletaHonorarioService
from SimpleFacturaSDK.models.BoletaHonorarios.BHERequest import BHERequest
from SimpleFacturaSDK.ClientSimpleFactura import ClientSimpleFactura
import os
from dotenv import load_dotenv
load_dotenv()

class BoletaHonorarioController:
    def setUp(self):
        username = os.getenv("USERNAME")
        password = os.getenv("PASSWORD")
        
        self.client_api = ClientSimpleFactura(username, password)
        self.service = self.client_api.BoletaHonorarioService

    def obtener_pdf(self):
        try:
            solicitud = BHERequest(
                solicitud= BHERequest(
                    credenciales=Credenciales(
                        rut_emisor="76269769-6"
                    ),
                    Folio=15
                )
            )
            response = self.service.ObtenerPdf(solicitud)
            if response.status == 200:
                with open("boleta.pdf", "wb") as file:
                    file.write(response.data)
                print("PDF guardado con éxito.")
            else:
                print(f"Error: {response.message}")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def listado_emitidos(self):
        try:
            solicitud = BHERequest(
                solicitud= ListaBHERequest(
                    credenciales=Credenciales(
                        rut_emisor="76269769-6",
                        nombre_sucursal="Casa Matriz"
                    ),
                    Folio=None,
                    Desde=fecha_desde,
                    Hasta=fecha_hasta
                )
            )
            response = self.service.ListadoBHEEmitidos(solicitud)
            if response.status == 200:
                print("Listado obtenido:", response.data)
            else:
                print(f"Error: {response.message}")
        except Exception as e:
            print(f"Error inesperado: {e}")
