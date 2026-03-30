import sqlite3

# --- Inicialización de la Base de Datos ---
def crear_db():
    try:
        # Conexión y creación del archivo local .db
        conexion = sqlite3.connect('mensajes.db')
        cursor = conexion.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mensajes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contenido TEXT,
                fecha_envio TEXT,
                ip_cliente TEXT
            )
        ''')
        
        conexion.commit()
        conexion.close()
        print("Base de datos lista para multihilo.")
    except sqlite3.Error as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    crear_db()