#import mysql.connector
import pymysql

def get_db_connection():
    conn = pymysql.connect(
        host='localhost',      # Cambia por tu host de MySQL
        user='root',           # Cambia por tu usuario de MySQL
        password='root',       # Cambia por tu contraseña de MySQL
        database='unida',    # Cambia por tu base de datos
        port=3307,            # Puerto correcto
        auth_plugin_map={
            "caching_sha2_password": "pymysql.auth.caching_sha2_password"
        }
    )
    return conn

# Prueba de conexión
if __name__ == "__main__":
    try:
        conn = get_db_connection()
        print("Conexión exitosa a la base de datos")
        conn.close()
    except pymysql.Error as err:
        print(f"Error: {err}")
