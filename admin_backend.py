import sqlite3

def connect():
    """Set up a connection with the database."""
    conn_obj = sqlite3.connect("admindb.db")
    cur_obj = conn_obj.cursor()
    cur_obj.execute("CREATE TABLE IF NOT EXISTS "
                    "datospersonas (id integer PRIMARY KEY, "
                            "nif NOT NULL UNIQUE, "
                            "nombre NOT NULL, "
                            "primerapellido NOT NULL, "
                            "segundoapellido)")
    conn_obj.commit()
    conn_obj.close()


def insert(nif, nombre, primerapellido, segundoapellido):
    """Insert entry into database."""

    conn_obj = sqlite3.connect("admindb.db")
    cur_obj = conn_obj.cursor()
    cur_obj.execute("INSERT INTO datospersonas "
                    "VALUES (NULL, ?, ?, ?, ?)", (nif, nombre, primerapellido, segundoapellido))
    conn_obj.commit()
    conn_obj.close()

def search(nif, nombre, primerapellido, segundoapellido, año,
            mes, día, hora):
    """Search for a database entry."""
    conn_obj = sqlite3.connect("registro.db")
    cur_obj = conn_obj.cursor()
    cur_obj.execute("SELECT * "
                    "FROM registro "
                    "WHERE nif = ? OR nombre = ? OR primerapellido = ? OR segundoapellido = ? OR (año = ? AND mes = ? AND día = ? AND hora = ?)",
                    (nif, nombre, primerapellido, segundoapellido, año, mes, día, hora))
    rows = cur_obj.fetchall()
    conn_obj.close()
    return rows

def nifcomprueba(nif):
    """Search for a database entry."""
    conn_obj = sqlite3.connect("admindb.db")
    cur_obj = conn_obj.cursor()
    cur_obj.execute("SELECT * "
                    "FROM datospersonas "
                    "WHERE nif = ? ", ([nif])) ##los corchetes son fundamentales para el where con variable string
    rows = cur_obj.fetchall()
    conn_obj.close()
    return rows

connect()
