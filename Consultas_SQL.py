import pymysql

# ----------------------------------------------------Conexion a la Base de Datos-----------------------------------------------------------#


class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='gestion_de_alumyprof'
        )
        self.cursor = self.connection.cursor()

# -------------------------------------------------------SQL PROFESORES---------------------------------------------------------------------#


class Profesores(Database):
    # lista
    def obtener_profesores(self):
        sql = "SELECT profesores.*, asignaturas.nombre AS Asignatura FROM profesores LEFT JOIN asignaturas ON profesores.id = asignaturas.id_profesor ORDER BY profesores.id;"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
    # lista

    def insertar_profesor(self, nombre, documento_identidad):
        sql = f"INSERT INTO profesores (nombre, documento_identidad) VALUES ('{
            nombre}', '{documento_identidad}')"
        try:
            self.cursor.execute(sql)
            n = self.cursor.rowcount
            self.connection.commit()
            print("Datos Guardados Correctamente")
            return 1
        except Exception as ex:
            print(ex)
        return n

    def modificar_profesor(self, id, nombre, documento_identidad):
        sql = f'UPDATE `profesores` SET `nombre` = "{
            nombre}",`documento_identidad` = "{documento_identidad}" WHERE `id` = "{id}"'

        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(
                "Se modifico correctamente [Nombre, Numero de Documento] ....")
            return 1
        except Exception as e:
            raise e
    # LISTA

    def eliminar_profesor(self, nombre, documento_identidad):
        sql = f'DELETE FROM `profesores` WHERE `nombre`="{
            nombre}" AND `documento_identidad`="{documento_identidad}"'
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se elimino correctamente el Profesor")
            return 1
        except Exception as e:
            raise e
    # lista

    def Nombre_Profesor(self):
        sql = f'SELECT nombre FROM `profesores`'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()

        except Exception as ex:
            print(ex)
        return datos
    # lista

    def buscar_profesor(self, nombre):
        sql = f"SELECT profesores.*, asignaturas.nombre AS Asignatura FROM profesores LEFT JOIN asignaturas ON profesores.id = asignaturas.id_profesor WHERE profesores.nombre = '{
            nombre}' ORDER BY profesores.id"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos

    def id_Profesor(self, documento_identidad):
        sql = f'SELECT id FROM `profesores` WHERE documento_identidad = "{
            documento_identidad}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()

        except Exception as ex:
            print(ex)
        return datos[0]


# ----------------------------------------------------------SQL ALUMNOS------------------------------------------------------------------#


class Alumnos(Database):
    # LISTA
    def obtener_Alumnos(self):
        sql = "SELECT alumnos.id, alumnos.nombre, alumnos.documento_identidad, asignaturas.nombre AS asignatura FROM alumnos JOIN asignaturas_alumnos ON alumnos.id = asignaturas_alumnos.id_alumno JOIN asignaturas ON asignaturas_alumnos.id_asignatura = asignaturas.id LIMIT 20"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos

    # LISTA
    def buscar_Alumno(self, nombre):
        sql = f"SELECT alumnos.*, asignaturas.nombre AS Asignatura FROM alumnos LEFT JOIN asignaturas_alumnos ON alumnos.id = asignaturas_alumnos.id_alumno LEFT JOIN asignaturas ON asignaturas_alumnos.id_asignatura = asignaturas.id WHERE alumnos.nombre = '{
            nombre}' ORDER BY alumnos.id"

        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)

        return datos

    # LISTA PARA BUSQUEDA
    def Nombre_Alumno(self):
        sql = f'SELECT nombre FROM `alumnos`'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()

        except Exception as ex:
            print(ex)
        return datos
    # LISTO ARBOL NOTAS FRAME 1
    def Obtener_Alumno_Notas(self):
        sql = f"SELECT alumnos.id, alumnos.nombre AS alumno, asignaturas.nombre AS asignatura, notas.nota1, notas.nota2, notas.nota3, (notas.nota1 + notas.nota2 + notas.nota3) / 3.0 AS promedio_calculado FROM alumnos JOIN asignaturas_alumnos ON alumnos.id = asignaturas_alumnos.id_alumno JOIN asignaturas ON asignaturas_alumnos.id_asignatura = asignaturas.id JOIN notas ON asignaturas_alumnos.id = notas.id_asignatura_alumno LIMIT 100;"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos
    # LISTA 
    def Buscar_Alumno_NotasBuscar(self, nombre):
        sql = f"SELECT asignaturas.nombre AS asignatura, notas.nota1, notas.nota2, notas.nota3, (notas.nota1 + notas.nota2 + notas.nota3) / 3.0 AS promedio_calculado FROM alumnos LEFT JOIN asignaturas_alumnos ON alumnos.id = asignaturas_alumnos.id_alumno LEFT JOIN asignaturas ON asignaturas_alumnos.id_asignatura = asignaturas.id LEFT JOIN notas ON asignaturas_alumnos.id = notas.id_asignatura_alumno WHERE alumnos.nombre = '{nombre}' ORDER BY asignaturas.nombre"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos

    def insertar_alumno(self, nombre, documento_identidad):
        sql = f"INSERT INTO alumnos (nombre, documento_identidad) VALUES ('{
            nombre}', '{documento_identidad}')"
        try:
            self.cursor.execute(sql)
            n = self.cursor.rowcount
            self.connection.commit()
            print("Datos Guardados Correctamente")
            return 1
        except Exception as ex:
            print(ex)
        return n

    def modificar_alumno(self, alumno_id, nombre, documento_identidad):
        sql = f"UPDATE alumnos SET nombre='{nombre}', documento_identidad='{
            documento_identidad}' WHERE id={alumno_id}"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(
                "Se modifico correctamente [Nombre, Numero de Documento] ....")
            return 1
        except Exception as e:
            raise e

    def eliminar_alumno(self, alumno_id):
        sql = f"DELETE FROM alumnos WHERE id={alumno_id}"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se elimino correctamente el Alumno")
            return 1
        except Exception as e:
            raise e

# --------------------------------------------------------SQL ASIGNATURAS---------------------------------------------------------------#


class Asignaturas(Database):
    def obtener_asignaturas(self):
        sql = "SELECT * FROM asignaturas"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos

    def obtener_nombre_asignatura(self, id):
        sql = 'SELECT nombre FROM asignaturas WHERE `id`="{id}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos

    def insertar_asignatura(self, nombre, id_profesor):
        sql = f"INSERT INTO asignaturas (nombre, id_profesor) VALUES ('{
            nombre}', '{id_profesor}')"
        try:
            self.cursor.execute(sql)
            n = self.cursor.rowcount
            self.connection.commit()
            print("Datos Guardados Correctamente")
            return 1
        except Exception as ex:
            print(ex)
        return n

    def modificar_asignatura(self, id, nombre):
        sql = f"UPDATE asignaturas SET nombre = '{nombre}' WHERE id = '{id}'"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Asignatura modificada correctamente")
            return 1
        except Exception as e:
            raise e

    def id_asignatura(self, nombre):
        sql = f'SELECT id FROM `asignaturas` WHERE nombre = "{nombre}"'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchone()

        except Exception as ex:
            print(ex)
        return datos

    # LISTA

    def eliminar_asignatura(self, nombre):
        sql = f'DELETE FROM `asignaturas` WHERE `nombre`="{nombre}"'
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se elimino correctamente la asignatura")
            return 1
        except Exception as e:
            raise e

# s
    # LISTA

    def buscar_Nombre_Asignatura(self):
        sql = f'SELECT nombre FROM `asignaturas`'
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()

        except Exception as ex:
            print(ex)
        return datos
# -----------------------------------------------------------SQL NOTAS------------------------------------------------------------------#


class Notas(Database):
    def obtener_notas(self):
        sql = "SELECT * FROM notas"
        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        return datos

    def insertar_nota(self, id_asignatura_alumno, nota1, nota2, nota3):
        sql = f"INSERT INTO notas (id_asignatura_alumno, nota1, nota2, nota3) VALUES ({
            id_asignatura_alumno}, {nota1}, {nota2}, {nota3})"
        try:
            self.cursor.execute(sql)
            n = self.cursor.rowcount
            self.connection.commit()
            print("Datos Guardados Correctamente")
            return 1
        except Exception as ex:
            print(ex)
        return n

    def modificar_nota(self, nota_id, nota1, nota2, nota3):
        sql = f"UPDATE notas SET nota1={nota1}, nota2={
            nota2}, nota3={nota3} WHERE id={nota_id}"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print(
                "Se modifico correctamente las notas del Alumno {nota_id}....")
            return 1
        except Exception as e:
            raise e

    def eliminar_nota(self, nota_id):
        sql = f"DELETE FROM notas WHERE id={nota_id}"
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Se elimino correctamente")
            return 1
        except Exception as e:
            raise e


# consulta = Alumnos()
# print(consulta.Nombre_Alumno_NotasBuscar("Marcelo Páez Aracena"))


