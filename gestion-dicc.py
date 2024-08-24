from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from Consultas_SQL import Profesores, Alumnos, Asignaturas, Notas
import re


class Application(Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión Académica DIICC")
        self.geometry("1000x650")
        self.create_widgets()

# ---------------------------------------------Barra despegable de Opciones----------------------------------------------------------#

    def create_widgets(self):
        opciones = tk.Menu(self)
        self.config(menu=opciones)

        file_menu = tk.Menu(opciones, tearoff=0)
        file_menu.add_command(
            label="Gestión de Personal Académico", command=self.Op_Gestion_Profesores)
        file_menu.add_command(label="Gestión de Alumnos",
                              command=self.Op_Gestion_Alumnos)
        file_menu.add_command(
            label="Gestión de Notas por Asignaturas", command=self.Op_Gestion_Notas)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.quit)
        opciones.add_cascade(label="Opciones", menu=file_menu)

        self.frame_actual = None
        self.Op_Gestion_Profesores()

    def Op_Gestion_Profesores(self):
        if self.frame_actual:
            self.frame_actual.destroy()
        self.frame_actual = Gestion_Profesores(self)
        self.frame_actual.pack()

    def Op_Gestion_Alumnos(self):
        if self.frame_actual:
            self.frame_actual.destroy()
        self.frame_actual = Gestion_Alumnos(self)
        self.frame_actual.pack()

    def Op_Gestion_Notas(self):
        if self.frame_actual:
            self.frame_actual.destroy()
        self.frame_actual = Gestion_Notas(self)
        self.frame_actual.pack()

# -------------------------------------------------VENTANA DE PROFESORES---------------------------------------------------------#


class Gestion_Profesores(Frame):
    Profesores = Profesores()
    Asignaturas = Asignaturas()

    def __init__(self, master=None, ):
        super().__init__(master, width=1000, height=650, bg='#6A5ACD')

        self.master = master
        self.pack()
        self.CrearFrames()
        self.llenardatosProfesores()
        self.habilitarCajas("disabled")
        self.habilitarBtnPrin("normal")
        self.habilitarBtnGuardar("disabled")
        self.id = -1


# ----------------------------------------------------FUNCIONES DE FRAME 1---------------------------------------------------------#


    def habilitarCajas(self, estado):
        self.etNombre.configure(state=estado)
        self.Documento.configure(state=estado)
        self.selec_asignatura.configure(state=estado)

    def habilitarBtnPrin(self, estado):
        self.btnNuevo.configure(state=estado)
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)

    def habilitarBtnGuardar(self, estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar.configure(state=estado)

    def limpiarArbol(self):
        for item in self.treeprofesores.get_children():
            self.treeprofesores.delete(item)

    def limpiarCajas(self):
        self.etNombre.delete(0, END)
        self.Documento.delete(0, END)
        self.selec_asignatura.delete(0, END)

    def validar_valores_profesores(self):

        if not self.etNombre.get() or not self.Documento.get() or not self.selec_asignatura.get():
            return False
        return True

    def validar_nombre(self, nombre):
        patron = r'^[a-zA-Z\s]+$'
        if re.match(patron, nombre):
            return True
        else:
            return False

# ---------------------------------------------------FUNCIONES DE BOTONES-----------------------------------------------------------------#
    # LISTO

    def Nuevo(self):
        self.limpiarCajas()
        self.habilitarCajas("normal")
        self.habilitarBtnPrin("disabled")
        self.habilitarBtnGuardar("normal")
        self.selec_asignatura.configure(state="readonly")
        self.limpiarCajas()

    # LISTO
    def Modificar(self):
        selected = self.treeprofesores.focus()
        clave = self.treeprofesores.item(selected, 'text')
        if clave == '':
            messagebox.showwarning(
                "Modificar", 'Debes seleccionar un elemento de la tabla.')
        else:
            self.id = clave
            self.habilitarCajas("normal")
            valores = self.treeprofesores.item(selected, 'values')
            print(valores)
            self.limpiarCajas()
            self.etNombre.insert(0, valores[0])
            self.Documento.insert(0, valores[1])
            self.selec_asignatura.insert(0, valores[2])

            self.etNombre.configure(state="normal")
            self.Documento.configure(state="normal")
            self.selec_asignatura.configure(state="readonly")

            self.habilitarBtnPrin("disabled")
            self.habilitarBtnGuardar("normal")

    # LISTO SOLO QUE NO ACTUALIZA EL ARBOL
    def Eliminar(self):
        selected = self.treeprofesores.focus()
        clave = self.treeprofesores.item(selected, 'text')
        if clave == '':
            messagebox.showwarning(
                "Eliminar", 'Debes seleccionar un elemento.')
        else:
            valores = self.treeprofesores.item(selected, 'values')
            print(valores[0])
            data = str(clave) + ", " + \
                valores[0] + ", " + valores[1] + ", " + valores[2]
            respuesta = messagebox.askquestion(
                "Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)
            if respuesta == messagebox.YES:
                x = self.Profesores.eliminar_profesor(valores[0], valores[1])
                n = self.Asignaturas.eliminar_asignatura(valores[2])
                print(valores[1])
                print(valores[2])
                
                if n == 1:
                    messagebox.showinfo(
                        "Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiarArbol()
                    self.llenardatosProfesores()
                else:
                    messagebox.showwarning(
                        "Eliminar", 'No fue posible eliminar el elemento.')
                    self.limpiarArbol()
                    self.llenardatosProfesores()
                if x == 1:
                    messagebox.showinfo(
                        "Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiarArbol()
                    self.llenardatosProfesores()
                else:
                    messagebox.showwarning(
                        "Eliminar", 'No fue posible eliminar el elemento.')
                    self.limpiarArbol()
                    self.llenardatosProfesores()



    def Guardar(self):
        pass

        # if (self.validar_valores_profesores()):
        #     if self.id == -1:
        #         if (self.validar_nombre(self.etNombre.get())):
        #             if (self.Profesores.insertar_profesor(self.etNombre.get(), self.Documento.get()) == 1):
        #                 if (self.Asignaturas.insertar_asignatura(self.selec_asignatura.get().replace("{", "").replace("}", ""), self.Profesores.id_Profesor(self.Documento.get())) == 1):
        #                     messagebox.showinfo(
        #                         "Guardar", 'Elemento guardado correctamente.')
        #                     self.etNombre.configure(state="normal")
        #                     self.Documento.configure(state="normal")
        #                     self.selec_asignatura.configure(state="readonly")
        #                     self.limpiarArbol()
        #                     self.llenardatosProfesores()
        #                     self.limpiarCajas()
        #                     self.habilitarBtnGuardar("normal")
        #                     self.habilitarBtnPrin("disabled")
        #                     self.habilitarCajas("disabled")
        #                     self.limpiarArbol()
        #                     self.llenardatosProfesores()

        #                 else:
        #                     messagebox.showinfo(
        #                         "Guardar", "No fue posible guardar el registro.")
        #             else:
        #                 messagebox.showinfo(
        #                     "ERROR", "Ingrese un profesor nuevamente.")
        #         else:
        #             messagebox.showinfo(
        #                 "ERROR", "Ingrese un nombre alfabético.")
        #     else:
        #         if (self.validar_valores_profesores()):
        #             if (self.validar_nombre(self.etNombre.get())):
        #                 if (self.Profesores.modificar_profesor(self.Profesores.id_Profesor(self.Documento.get()), self.etNombre.get(), self.Documento.get()) == 1):
        #                     if (self.Asignaturas.modificar_asignatura(self.Asignaturas.id_asignatura(self.selec_asignatura.get().replace("{", "").replace("}", "")), self.selec_asignatura.get().replace("{", "").replace("}", "")) == 1):
        #                         messagebox.showinfo(
        #                             "Modificar", 'Elemento modificado correctamente.')
        #                         self.id = -1
        #                         self.etNombre.configure(state="normal")
        #                         self.Documento.configure(state="normal")
        #                         self.selec_asignatura.configure(
        #                             state="readonly")
        #                         self.limpiarArbol()
        #                         self.llenardatosProfesores()
        #                         self.limpiarCajas()
        #                         self.habilitarBtnGuardar("normal")
        #                         self.habilitarBtnPrin("disabled")
        #                         self.habilitarCajas("disabled")
        #                         self.limpiarArbol()
        #                         self.llenardatosProfesores()

        #                     else:
        #                         messagebox.showinfo(
        #                             "ERROR", 'No fue posible modificar.')
        #                 else:
        #                     messagebox.showinfo(
        #                         "ERROR", "Ingrese un profesor nuevamente.")
        #             else:
        #                 messagebox.showinfo(
        #                     "ERROR", "Ingrese un nombre alfabético.")
        #         else:
        #             messagebox.showinfo(
        #                 "ERROR", "Ingrese todos los valores.")
        # else:
        #     messagebox.showinfo(
        #         "ERROR", "Ingrese todos los valores.")

    # LISTO

    def Cancelar(self):
        r = messagebox.askquestion(
            "Cancelar", "Esta seguro que desea cancelar la operación actual.")
        if r == messagebox.YES:

            self.etNombre.configure(state="normal")
            self.Documento.configure(state="normal")
            self.selec_asignatura.configure(state="normal")
            self.limpiarCajas()
            self.habilitarBtnGuardar("disabled")
            self.habilitarBtnPrin("normal")
            self.habilitarCajas("disabled")
# ---------------------------------------------FUNCIONES COMBOBOX FRAME BUSQUEDA----------------------------------------------------------------#

    def llenardatosProfesores(self):
        self.limpiarArbol()
        datos = self.Profesores.obtener_profesores()
        for row in datos:
            self.treeprofesores.insert(
                "", END, text=row[0], values=(row[1], row[2], row[3]))

    def vaciararbolbuscarprofesores(self):
        for item in self.treebuscar.get_children():
            self.treebuscar.delete(item)

    def llenardatosBuscarProfesor(self):
        self.vaciararbolbuscarprofesores()
        datos = self.Profesores.buscar_profesor(
            self.etBuscar.get().replace("{", "").replace("}", ""))
        for row in datos:
            self.treebuscar.insert(
                "", END, text=row[0], values=(row[1], row[2], row[3]))


# ----------------------------------------------------FRAME DE PROFESORES------------------------------------------------------------------#

    def CrearFrames(self):
        # Frame 1
        frame1 = Frame(self, bg="sky blue")
        frame1.place(x=0, y=0, width=1000, height=650)
# -----------------------------------------------------TITULO------------------------------------------------------------------------------#
        titulo2 = Label(frame1, text="Gestión de Personal Académico",
                        bg="#C0C0C0", fg="black", font=("Times New Roman", 20, "bold"))
        titulo2.place(x=300, y=0, width=380, height=50)


# ------------------------------------------------------BOTONES FRAME 1--------------------------------------------------------------------#
        self.btnNuevo = Button(frame1, text="Nuevo", command=self.Nuevo,
                               bg="#B22222", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnNuevo.place(x=250, y=350, width=80, height=30)

        self.btnModificar = Button(frame1, text="Modificar", command=self.Modificar,
                                   bg="#B22222", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnModificar.place(x=350, y=350, width=80, height=30)

        self.btnEliminar = Button(frame1, text="Eliminar", command=self.Eliminar,
                                  bg="#B22222", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnEliminar.place(x=450, y=350, width=80, height=30)

        self.btnGuardar = Button(frame1, text="Guardar", command=self.Guardar,
                                 bg="#228B22", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnGuardar.place(x=550, y=350, width=80, height=30)

        self.btnCancelar = Button(frame1, text="Cancelar", command=self.Cancelar,
                                  bg="#FF0000", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnCancelar.place(x=650, y=350, width=80, height=30)
# ----------------------------------------------------------------------------------------------------------------------------------------------#

        labelNombre = Label(frame1, text="Nombre",
                            font=("Berlin Sans FB Demi", 14))

        labelNombre.place(x=10, y=100, width=150, height=25)
        self.etNombre = Entry(frame1)
        self.etNombre.place(x=180, y=100, width=200, height=25)

        labelDocumento = Label(frame1, text="N° Documento",
                               font=("Berlin Sans FB Demi", 14))
        labelDocumento.place(x=10, y=160, width=150, height=25)
        self.Documento = Entry(frame1)
        self.Documento.place(x=180, y=160, width=200, height=25)

        labelAsignatura = Label(
            frame1, text="Asignatura", font=("Berlin Sans FB Demi", 14))
        labelAsignatura.place(x=10, y=220, width=150, height=25)
        # Combobox para elegir Asignatura
        datos = self.Asignaturas.buscar_Nombre_Asignatura()
        self.selec_asignatura = ttk.Combobox(frame1, values=datos)
        self.selec_asignatura.place(x=180, y=220, width=200, height=25)
        self.selec_asignatura.configure(state="readonly")

# ---------------------------------------------------------ARBOL FRAME 1---------------------------------------------------------------------#
        self.treeprofesores = ttk.Treeview(frame1, columns=(
            "col2", "col3", "col4"), height=10)
        self.treeprofesores.column("#0", width=60, anchor=CENTER)
        self.treeprofesores.column("col2", width=250, anchor=CENTER)
        self.treeprofesores.column("col3", width=250, anchor=CENTER)
        self.treeprofesores.column("col4", width=250, anchor=CENTER)

        self.treeprofesores.heading("#0", text="id", anchor=CENTER)
        self.treeprofesores.heading("col2", text="Nombre", anchor=CENTER)
        self.treeprofesores.heading("col3", text="N° Documento", anchor=CENTER)
        self.treeprofesores.heading("col4", text="Asignatura", anchor=CENTER)

        self.treeprofesores.place(x=100, y=400)
# ---------------------------------------------------------FRAME DE BUSQUEDA PROFESORES----------------------------------------------------------------#
        frameBuscar = Frame(self, bg="silver")
        frameBuscar.place(x=400, y=70, width=600, height=250)
        # Boton de buscar
        self.btnbuscar = Button(frameBuscar, text="Buscar", command=self.llenardatosBuscarProfesor,
                                bg="#000080", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnbuscar.place(x=100, y=10, width=100, height=30)
        # Buscar por Nombre de Profesor
        datos = self.Profesores.Nombre_Profesor()
        self.etBuscar = ttk.Combobox(frameBuscar, values=datos)
        self.etBuscar.place(x=220, y=10, width=150, height=30)
        self.etBuscar.configure(state="readonly")  # Restringe escribir

        # AGREGAR BOTON DE MODIFICAR, ELIMINAR, GUARDAR Y CANCELAR 
# ---------------------------------------------------------ARBOL FRAME BUSQUEDA PROFESORES-------------------------------------------------------------#
        self.treebuscar = ttk.Treeview(frameBuscar, columns=(
            "col2", "col3", "col4"), height=5)
        self.treebuscar.column("#0", width=60, anchor=CENTER)
        self.treebuscar.column("col2", width=150, anchor=CENTER)
        self.treebuscar.column("col3", width=150, anchor=CENTER)
        self.treebuscar.column("col4", width=200, anchor=CENTER)

        self.treebuscar.heading("#0", text="id", anchor=CENTER)
        self.treebuscar.heading("col2", text="Nombre", anchor=CENTER)
        self.treebuscar.heading("col3", text="N° Documento", anchor=CENTER)
        self.treebuscar.heading("col4", text="Asignatura", anchor=CENTER)

        self.treebuscar.place(x=25, y=100)

# --------------------------------------------------------------VENTANA DE ALUMNOS-----------------------------------------------------------------------#


class Gestion_Alumnos(Frame):
    Asignaturas = Asignaturas()
    Alumnos = Alumnos()
    Notas = Notas()

    def __init__(self, master=None):
        super().__init__(master, width=1000, height=650, bg='#6A5ACD')
        self.master = master
        self.pack()
        self.CrearFrames()
        self.llenardatosAlumnos()
        self.habilitarCajas("disabled")
        self.habilitarBtnPrin("normal")
        self.habilitarBtnGuardar("disabled")
        self.id = -1
# --------------------------------------------------------------FUNCIONES DE FRAME 1----------------------------------------------------------------------#

    def habilitarCajas(self, estado):
        self.Nombre_al.configure(state=estado)
        self.Documento_al.configure(state=estado)
        self.selec_asignatura_al.configure(state=estado)

    def habilitarBtnPrin(self, estado):
        self.btnNuevo_al.configure(state=estado)
        self.btnModificar_al.configure(state=estado)
        self.btnEliminar_al.configure(state=estado)

    def habilitarBtnGuardar(self, estado):
        self.btnGuardar_al.configure(state=estado)
        self.btnCancelar_al.configure(state=estado)

    def limpiarArbolAlumnos(self):
        for item in self.treeAlumnos.get_children():
            self.treeAlumnos.delete(item)

    def limpiarCajas(self):
        self.Nombre_al.delete(0, END)
        self.Documento_al.delete(0, END)
        self.selec_asignatura_al.delete(0, END)

    def validar_valores_Alumnos(self):

        if not self.Nombre_al.get() or not self.Documento_al.get() or not self.selec_asignatura_al.get():
            return False
        return True

    def validar_nombre(self, nombre):
        patron = r'^[a-zA-Z\s]+$'
        if re.match(patron, nombre):
            return True
        else:
            return False


# -------------------------------------------------------------FUNCIONES DE BOTONES FRAME ALUMNOS----------------------------------------------------------------------#
    # LISTO

    def Nuevo_al(self):
        self.limpiarCajas()
        self.habilitarCajas("normal")
        self.habilitarBtnPrin("disabled")
        self.habilitarBtnGuardar("normal")
        self.selec_asignatura_al.configure(state="readonly")
        self.limpiarCajas()
    # LISTO

    def Modificar_al(self):
        selected = self.treeAlumnos.focus()
        clave = self.treeAlumnos.item(selected, 'text')
        if clave == '':
            messagebox.showwarning(
                "Modificar", 'Debes seleccionar un elemento de la tabla.')
        else:
            self.id = clave
            self.habilitarCajas("normal")
            valores = self.treeAlumnos.item(selected, 'values')
            print(valores)
            self.limpiarCajas()
            self.Nombre_al.insert(0, valores[0])
            self.Documento_al.insert(0, valores[1])
            self.selec_asignatura_al.insert(0, valores[2])

            self.Nombre_al.configure(state="normal")
            self.Documento_al.configure(state="normal")
            self.selec_asignatura_al.configure(state="readonly")

            self.habilitarBtnPrin("disabled")
            self.habilitarBtnGuardar("normal")

    def Eliminar_al(self):
        pass

    def Guardar_al(self):
        pass

    def Cancelar_al(self):
        pass
# ---------------------------------------------------FUNCIONES COMBOBOX BUSQUEDA ALUMNOS---------------------------------------------------------#

    def llenardatosAlumnos(self):
        self.limpiarArbolAlumnos()
        datos = self.Alumnos.obtener_Alumnos()
        for row in datos:
            self.treeAlumnos.insert(
                "", END, text=row[0], values=(row[1], row[2], row[3]))

    def vaciararbolbuscarAlumnos(self):
        for item in self.treebuscar_al.get_children():
            self.treebuscar_al.delete(item)

    def llenardatosBuscarAlumnos(self):
        self.vaciararbolbuscarAlumnos()
        datos = self.Alumnos.buscar_Alumno(
            self.etBuscar_al.get().replace("{", "").replace("}", ""))
        for row in datos:
            self.treebuscar_al.insert(
                "", END, text=row[0], values=(row[1], row[2], row[3]))
# ---------------------------------------------------------------FRAME DE ALUMNOS-----------------------------------------------------------------------#

    def CrearFrames(self):
        # Frame 1
        frame_al = Frame(self, bg="#bcd79a")
        frame_al.place(x=0, y=0, width=1000, height=650)
# -----------------------------------------------------TITULO------------------------------------------------------------------------------#
        titulo3 = Label(frame_al, text="Gestión de Alumnos",
                        bg="#8e903c", fg="white", font=("Times New Roman", 22, "bold"))
        titulo3.place(x=320, y=0, width=350, height=50)

# ------------------------------------------------------BOTONES FRAME 1--------------------------------------------------------------------#
        self.btnNuevo_al = Button(frame_al, text="Nuevo", command=self.Nuevo_al,
                                  bg="#B22222", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnNuevo_al.place(x=250, y=350, width=80, height=30)

        self.btnModificar_al = Button(frame_al, text="Modificar", command=self.Modificar_al,
                                      bg="#B22222", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnModificar_al.place(x=350, y=350, width=80, height=30)

        self.btnEliminar_al = Button(frame_al, text="Eliminar", command=self.Eliminar_al,
                                     bg="#B22222", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnEliminar_al.place(x=450, y=350, width=80, height=30)

        self.btnGuardar_al = Button(frame_al, text="Guardar", command=self.Guardar_al,
                                    bg="#228B22", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnGuardar_al.place(x=550, y=350, width=80, height=30)

        self.btnCancelar_al = Button(frame_al, text="Cancelar", command=self.Cancelar_al,
                                     bg="#FF0000", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnCancelar_al.place(x=650, y=350, width=80, height=30)
# ----------------------------------------------------------------------------------------------------------------------------------------------#

        labelNombre_al = Label(frame_al, text="Nombre",
                               font=("Berlin Sans FB Demi", 14))

        labelNombre_al.place(x=10, y=100, width=150, height=25)
        self.Nombre_al = Entry(frame_al)
        self.Nombre_al.place(x=180, y=100, width=200, height=25)

        labelDocumento_al = Label(frame_al, text="N° Documento",
                                  font=("Berlin Sans FB Demi", 14))
        labelDocumento_al.place(x=10, y=160, width=150, height=25)
        self.Documento_al = Entry(frame_al)
        self.Documento_al.place(x=180, y=160, width=200, height=25)

        labelAsignatura_al = Label(
            frame_al, text="Asignatura", font=("Berlin Sans FB Demi", 14))
        labelAsignatura_al.place(x=10, y=220, width=150, height=25)

        # Combobox para elegir Asignatura
        datos = self.Asignaturas.buscar_Nombre_Asignatura()
        self.selec_asignatura_al = ttk.Combobox(frame_al, values=datos)
        self.selec_asignatura_al.place(x=180, y=220, width=200, height=25)
        self.selec_asignatura_al.configure(state="readonly")

# ---------------------------------------------------------ARBOL FRAME 1---------------------------------------------------------------------#
        self.treeAlumnos = ttk.Treeview(frame_al, columns=(
            "col2", "col3", "col4"), height=10)
        self.treeAlumnos.column("#0", width=60, anchor=CENTER)
        self.treeAlumnos.column("col2", width=250, anchor=CENTER)
        self.treeAlumnos.column("col3", width=250, anchor=CENTER)
        self.treeAlumnos.column("col4", width=250, anchor=CENTER)

        self.treeAlumnos.heading("#0", text="id", anchor=CENTER)
        self.treeAlumnos.heading("col2", text="Nombre", anchor=CENTER)
        self.treeAlumnos.heading("col3", text="N° Documento", anchor=CENTER)
        self.treeAlumnos.heading("col4", text="Asignatura", anchor=CENTER)

        self.treeAlumnos.place(x=100, y=400)

# ---------------------------------------------------------FRAME DE BUSQUEDA ALUMNOS----------------------------------------------------------------#
        frameBuscar_al = Frame(self, bg="#8e903c")
        frameBuscar_al.place(x=400, y=70, width=600, height=250)
        # Boton de buscar
        self.btnbuscar = Button(frameBuscar_al, text="Buscar", command=self.llenardatosBuscarAlumnos,
                                bg="#000080", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnbuscar.place(x=100, y=10, width=100, height=30)
        # Buscar por Nombre de Alumno
        datos = self.Alumnos.Nombre_Alumno()
        self.etBuscar_al = ttk.Combobox(frameBuscar_al, values=datos)
        self.etBuscar_al.place(x=220, y=10, width=150, height=30)
        self.etBuscar_al.configure(state="readonly")  # Restringe escribir

        # AGREGAR BOTONES MODIFICAR, ELIMINAR, GUARDAR Y CANCELAR
# ---------------------------------------------------------ARBOL FRAME BUSQUEDA ALUMNOS-------------------------------------------------------------#
        self.treebuscar_al = ttk.Treeview(frameBuscar_al, columns=(
            "col2", "col3", "col4"), height=5)
        self.treebuscar_al.column("#0", width=60, anchor=CENTER)
        self.treebuscar_al.column("col2", width=150, anchor=CENTER)
        self.treebuscar_al.column("col3", width=150, anchor=CENTER)
        self.treebuscar_al.column("col4", width=200, anchor=CENTER)

        self.treebuscar_al.heading("#0", text="id", anchor=CENTER)
        self.treebuscar_al.heading("col2", text="Nombre", anchor=CENTER)
        self.treebuscar_al.heading("col3", text="N° Documento", anchor=CENTER)
        self.treebuscar_al.heading("col4", text="Asignatura", anchor=CENTER)

        self.treebuscar_al.place(x=25, y=100)

# --------------------------------------------------------------VENTANA DE NOTAS--------------------------------------------------------------------#


class Gestion_Notas(Frame):
    Notas = Notas()
    Alumnos = Alumnos()
    Asignaturas = Asignaturas()

    def __init__(self, master=None):
        super().__init__(master, width=1000, height=650, bg='#FF00FF')
        self.master = master
        self.pack()
        self.CrearFrames()
        self.llenardatosNotas()
        self.habilitarCajas("disabled")
        self.habilitarBtnPrin("normal")
        self.habilitarBtnGuardar("disabled")
        self.id = -1

# --------------------------------------------------------------FUNCIONES DE FRAME 1----------------------------------------------------------------------#

    def habilitarCajas(self, estado):
        self.Nota1.configure(state=estado)
        self.Nota2.configure(state=estado)
        self.Nota3.configure(state=estado)

    def habilitarBtnPrin(self, estado):
        self.btnNuevo_notas.configure(state=estado)
        self.btnModificar_notas.configure(state=estado)
        self.btnEliminar_notas.configure(state=estado)

    def habilitarBtnGuardar(self, estado):
        self.btnGuardar_notas.configure(state=estado)
        self.btnCancelar_notas.configure(state=estado)

    def limpiarArbolNotas(self):
        for item in self.treeNotas.get_children():
            self.treeNotas.delete(item)

    def limpiarCajas(self):
        self.Nota1.delete(0, END)
        self.Nota2.delete(0, END)
        self.Nota3.delete(0, END)

    def validar_valores_Notas(self):

        if not self.Nota1.get() or not self.Nota2.get() or not self.Nota3.get():
            return False
        return True



# --------------------------------------------------------------FUNCIONES DE BOTONES-----------------------------------------------------------------#
    def Nuevo_Notas(self):
        pass

    def Modificar_Notas(self):
        pass

    def Eliminar_Notas(self):
        pass

    def Guardar_Notas(self):
        pass

    def Cancelar_Notas(self):
        pass
# ---------------------------------------------------FUNCIONES COMBOBOX BUSQUEDA NOTAS---------------------------------------------------------#

    def llenardatosNotas(self):
        self.limpiarArbolNotas()
        datos = self.Alumnos.Obtener_Alumno_Notas()
        for row in datos:
            self.treeNotas.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6]))

    def vaciararbolbuscarNotas(self):
        for item in self.treebuscar_Notas.get_children():
            self.treebuscar_Notas.delete(item)

    def llenardatosBuscarNotas(self):
        self.vaciararbolbuscarNotas()
        datos = self.Alumnos.Buscar_Alumno_NotasBuscar(
            self.etBuscar_Notas.get().replace("{", "").replace("}", ""))
        for row in datos:
            self.treebuscar_Notas.insert(
                "", END, text=row[0], values=(row[1], row[2], row[3], row[4]))

# --------------------------------------------------------------FRAME DE NOTAS-----------------------------------------------------------------------#

    def CrearFrames(self):
        frame_Notas = Frame(self, bg="#7898a4")
        frame_Notas.place(x=0, y=0, width=1000, height=650)
# -----------------------------------------------------TITULO------------------------------------------------------------------------------#
        titulo3 = Label(frame_Notas, text="Gestión de Notas",
                        bg="#4cacdc", fg="black", font=("Times New Roman", 22, "bold"))
        titulo3.place(x=320, y=0, width=350, height=50)

# ------------------------------------------------------BOTONES FRAME 1--------------------------------------------------------------------#
        self.btnNuevo_notas = Button(frame_Notas, text="Nuevo", command=self.Nuevo_Notas,
                                     bg="#B22222", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnNuevo_notas.place(x=250, y=350, width=80, height=30)

        self.btnModificar_notas = Button(frame_Notas, text="Modificar", command=self.Modificar_Notas,
                                         bg="#B22222", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnModificar_notas.place(x=350, y=350, width=80, height=30)

        self.btnEliminar_notas = Button(frame_Notas, text="Eliminar", command=self.Eliminar_Notas,
                                        bg="#B22222", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnEliminar_notas.place(x=450, y=350, width=80, height=30)

        self.btnGuardar_notas = Button(frame_Notas, text="Guardar", command=self.Guardar_Notas,
                                       bg="#228B22", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnGuardar_notas.place(x=550, y=350, width=80, height=30)

        self.btnCancelar_notas = Button(frame_Notas, text="Cancelar", command=self.Cancelar_Notas,
                                        bg="#FF0000", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnCancelar_notas.place(x=650, y=350, width=80, height=30)
# ----------------------------------------------------------------------------------------------------------------------------------------------#

        labelNota1 = Label(frame_Notas, text="Nota 1",
                           font=("Berlin Sans FB Demi", 15))

        labelNota1.place(x=10, y=100, width=150, height=25)
        self.Nota1 = Entry(frame_Notas)
        self.Nota1.place(x=180, y=100, width=125, height=25)

        labelNota2 = Label(frame_Notas, text="Nota 2",
                           font=("Berlin Sans FB Demi", 15))
        labelNota2.place(x=10, y=160, width=150, height=25)
        self.Nota2 = Entry(frame_Notas)
        self.Nota2.place(x=180, y=160, width=125, height=25)

        labelNota3 = Label(
            frame_Notas, text="Nota 3", font=("Berlin Sans FB Demi", 15))
        labelNota3.place(x=10, y=220, width=150, height=25)
        self.Nota3 = Entry(frame_Notas)
        self.Nota3.place(x=180, y=220, width=125, height=25)


# ---------------------------------------------------------ARBOL FRAME 1---------------------------------------------------------------------#
        self.treeNotas = ttk.Treeview(frame_Notas, columns=(
            "col2", "col3", "col4", "col5", "col6", "col7"), height=10)
        self.treeNotas.column("#0", width=50, anchor=CENTER)
        self.treeNotas.column("col2", width=190, anchor=CENTER)
        self.treeNotas.column("col3", width=190, anchor=CENTER)
        self.treeNotas.column("col4", width=120, anchor=CENTER)
        self.treeNotas.column("col5", width=120, anchor=CENTER)
        self.treeNotas.column("col6", width=120, anchor=CENTER)
        self.treeNotas.column("col7", width=120, anchor=CENTER)

        self.treeNotas.heading("#0", text="id", anchor=CENTER)
        self.treeNotas.heading("col2", text="Nombre", anchor=CENTER)
        self.treeNotas.heading("col3", text="Asignatura", anchor=CENTER)
        self.treeNotas.heading("col4", text="Nota 1", anchor=CENTER)
        self.treeNotas.heading("col5", text="Nota 2", anchor=CENTER)
        self.treeNotas.heading("col6", text="Nota 3", anchor=CENTER)
        self.treeNotas.heading("col7", text="Promedio", anchor=CENTER)

        self.treeNotas.place(x=45, y=400)

# ---------------------------------------------------------FRAME DE BUSQUEDA NOTAS----------------------------------------------------------------#
        frameBuscar_Notas = Frame(self, bg="#4cacdc")
        frameBuscar_Notas.place(x=350, y=70, width=900, height=250)
        # Boton de buscar
        self.btnbuscar = Button(frameBuscar_Notas, text="Buscar", command=self.llenardatosBuscarNotas,
                                bg="#000080", fg="white", font=("Blue Fonte", 12, "bold"))
        self.btnbuscar.place(x=100, y=10, width=100, height=30)
        # Buscar por Nombre de Alumno
        
        datos = self.Alumnos.Nombre_Alumno() 
        self.etBuscar_Notas = ttk.Combobox(frameBuscar_Notas, values=datos)
        self.etBuscar_Notas.place(x=220, y=10, width=150, height=30)
        self.etBuscar_Notas.configure(state="readonly")  

        # AGREGAR BOTONES MODIFICAR, ELIMINAR, GUARDAR Y CANCELAR

# ---------------------------------------------------------ARBOL FRAME BUSQUEDA NOTAS-------------------------------------------------------------#
        self.treebuscar_Notas = ttk.Treeview(frameBuscar_Notas, columns=(
            "col2", "col3", "col4", "col5"), height=5)
        self.treebuscar_Notas.column("#0", width=200, anchor=CENTER)
        self.treebuscar_Notas.column("col2", width=100, anchor=CENTER)
        self.treebuscar_Notas.column("col3", width=100, anchor=CENTER)
        self.treebuscar_Notas.column("col4", width=100, anchor=CENTER)
        self.treebuscar_Notas.column("col5", width=100, anchor=CENTER)

        self.treebuscar_Notas.heading("#0", text="Asignatura", anchor=CENTER)
        self.treebuscar_Notas.heading("col2", text="Nota 1", anchor=CENTER)
        self.treebuscar_Notas.heading("col3", text="Nota 2", anchor=CENTER)
        self.treebuscar_Notas.heading("col4", text="Nota 3", anchor=CENTER)
        self.treebuscar_Notas.heading("col5", text="Promedio", anchor=CENTER)

        self.treebuscar_Notas.place(x=25, y=100)
# --------------------------------------------------------------FUNCION PRINCIPAL------------------------------------------------------------------#


def main():

    app = Application()
    app.iconbitmap('logo-gestion.ico')
    app.mainloop()


if __name__ == "__main__":
    main()
