import sqlite3
def sql_connection():
        con = sqlite3.connect('DENTAPLUS.db')
        return con

def sql_table(con):
    CursorObj = con.cursor()
    CursorObj.execute("CREATE TABLE 'PACIENTES' (NOMBRE TEXT NOT NULL, APELLIDO TEXT NOT NULL, RUT_PAC TEXT NOT NULL PRIMARY KEY, EDAD NUMERIC NOT NULL)")
    CursorObj.execute("CREATE TABLE 'DENTISTAS' (NOMBRE TEXT NOT NULL, APELLIDO TEXT NOT NULL, RUT_DENT TEXT NOT NULL PRIMARY KEY, FECHA_INGRESO DATE)")
    CursorObj.execute("CREATE TABLE 'ATENCIONES' (ID NUMERIC NOT NULL PRIMARY KEY, RUT_PAC TEXT NOT NULL, RUT_DEN TEXT NOT NULL, DESCRIPCION TEXT NOT NULL, FECHA_ATENCION DATE)")

    CursorObj.execute("INSERT INTO 'PACIENTES' VALUES ('Soledad','Ferrada', '11111111-1', '65 años')")
    CursorObj.execute("INSERT INTO 'PACIENTES' VALUES ('Margarita','González', '22222222-2', '34 años')")
    CursorObj.execute("INSERT INTO 'PACIENTES' VALUES ('Claudio','Rifo', '33333333-3', '46 años')")
    CursorObj.execute("INSERT INTO 'PACIENTES' VALUES ('Maria','Perez', '44444444-4', '39 años')")
    CursorObj.execute("INSERT INTO 'PACIENTES' VALUES ('Cristian','López', '55555555-5', '18 años')")
    CursorObj.execute("INSERT INTO 'PACIENTES' VALUES ('Gladys','Olivares', '66666666-6', '45 años')")
    CursorObj.execute("INSERT INTO 'PACIENTES' VALUES ('Natalia','Fritz', '77777777-7', '46 años')")

    CursorObj.execute("INSERT INTO 'DENTISTAS' VALUES ('Javier', 'Miranda', '88888888-8', '2018-05-01')")
    CursorObj.execute("INSERT INTO 'DENTISTAS' VALUES ('Patricia', 'Manterola', '99999999-9', '2019-01-22')")
    CursorObj.execute("INSERT INTO 'DENTISTAS' VALUES ('Paula', 'Gallegos', '12121212-1', '2017-09-01')")
    CursorObj.execute("INSERT INTO 'DENTISTAS' VALUES ('Pablo', 'Pereira', '45454545-4', '2019-04-01')")

    CursorObj.execute("INSERT INTO 'ATENCIONES' VALUES ('1', '11111111-1', '88888888-8', 'Extracción pieza 20', '2019-10-01')")
    CursorObj.execute("INSERT INTO 'ATENCIONES' VALUES ('2', '22222222-2', '88888888-8', 'Limpieza completa', '2019-10-04')")
    CursorObj.execute("INSERT INTO 'ATENCIONES' VALUES ('3', '33333333-3', '99999999-9', 'Tapadura simple pieza 5', '2019-10-05')")
    CursorObj.execute("INSERT INTO 'ATENCIONES' VALUES ('4', '44444444-4', '99999999-9', 'Tapadura simple pieza 30', '2019-10-06')")
    CursorObj.execute("INSERT INTO 'ATENCIONES' VALUES ('5', '55555555-5', '12121212-1', ' Extracción pieza 20', '2019-10-07')")
    CursorObj.execute("INSERT INTO 'ATENCIONES' VALUES ('6', '66666666-6', '45454545-4', 'Tapadura compuesta pieza 30', '2019-10-10')")
    CursorObj.execute("INSERT INTO 'ATENCIONES' VALUES ('7', '77777777-7', '45454545-4', 'Tapadura simple pieza 30', '2019-10-15')")
    con.commit()
    
def sql_fetch(con):
    CursorObj = con.cursor()
    CursorObj.execute("SELECT * FROM PACIENTES WHERE EDAD > 30 ORDER BY NOMBRE ASC")
    respuesta = CursorObj.fetchall()
    print(respuesta)


def sql_fetch_2(con):
    CursorObj = con.cursor()
    CursorObj.execute("SELECT * FROM ATENCIONES WHERE RUT_DEN = '99999999-9'")
    respuesta = CursorObj.fetchall()
    print(respuesta)

def sql_update(con):
    CursorObj = con.cursor()
    CursorObj.execute("UPDATE PACIENTES SET APELLIDO = 'Riffo' WHERE RUT = '33333333-3'")
    con.commit()

def sql_delete(con):
    CursorObj = con.cursor()
    CursorObj.execute("DELETE FROM ATENCIONES WHERE FECHA_ATENCION < '2019-10-04'")
    con.commit()

conex = sql_connection()
sql_table(conex)
sql_fetch(conex)
sql_fetch_2(conex)
