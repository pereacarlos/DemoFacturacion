import tkinter as tk
from tkinter import ttk, messagebox
from controllers.boletahonorario_controller import BoletaHonorarioController
from controllers.clientes_controller import ClientesController
from controllers.configuracion_controller import ConfiguracionController
from controllers.facturacion_controller import FacturacionController

class MainView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Demo Facturación SDK")
        self.root.geometry("800x600")

        # Crear tabs
        self.tab_control = ttk.Notebook(self.root)

        self.tab_boleta_honorario = ttk.Frame(self.tab_control)
        self.tab_clientes = ttk.Frame(self.tab_control)
        self.tab_configuracion = ttk.Frame(self.tab_control)
        self.tab_facturacion = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_boleta_honorario, text="Boleta Honorario")
        self.tab_control.add(self.tab_clientes, text="Clientes")
        self.tab_control.add(self.tab_configuracion, text="Configuración")
        self.tab_control.add(self.tab_facturacion, text="Facturación")

        self.tab_control.pack(expand=1, fill="both")

        # Crear botones para cada servicio
        self._create_boleta_honorario_buttons()
        self._create_clientes_buttons()
        self._create_configuracion_buttons()
        self._create_facturacion_buttons()

    def _create_boleta_honorario_buttons(self):
        controller = BoletaHonorarioController()
        ttk.Button(
            self.tab_boleta_honorario, text="Obtener PDF",
            command=controller.obtener_pdf
        ).pack(pady=10)
        ttk.Button(
            self.tab_boleta_honorario, text="Listado Emitidos",
            command=controller.listado_emitidos
        ).pack(pady=10)

    def _create_clientes_buttons(self):
        controller = ClientesController()
        ttk.Button(
            self.tab_clientes, text="Crear Cliente",
            command=controller.crear_cliente
        ).pack(pady=10)
        ttk.Button(
            self.tab_clientes, text="Listar Clientes",
            command=controller.listar_clientes
        ).pack(pady=10)

    def _create_configuracion_buttons(self):
        controller = ConfiguracionController()
        ttk.Button(
            self.tab_configuracion, text="Datos Empresa",
            command=controller.datos_empresa
        ).pack(pady=10)

    def _create_facturacion_buttons(self):
        controller = FacturacionController()
        ttk.Button(
            self.tab_facturacion, text="Obtener PDF",
            command=controller.obtener_pdf
        ).pack(pady=10)
        ttk.Button(
            self.tab_facturacion, text="Obtener Timbre",
            command=controller.obtener_timbre
        ).pack(pady=10)

    def run(self):
        self.root.mainloop()
