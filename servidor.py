import socket
import sqlite3
import threading # Librería para concurrencia
from datetime import datetime

# Función para guardar en la base de datos
def guardar_mensaje(contenido, ip):
    try:
        conexion = sqlite3.connect('mensajes.db')
        cursor = conexion.cursor()
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute('''
            INSERT INTO mensajes (contenido, fecha_envio, ip_cliente) 
            VALUES (?, ?, ?)
        ''', (contenido, fecha_actual, ip))
        
        conexion.commit()
        conexion.close()
        return fecha_actual
    except sqlite3.Error as e:
        print(f"Error en DB: {e}")
        return "Error en DB"

# Función que ejecutará cada hilo de forma independiente (Worker Thread)
def manejar_cliente(cliente_socket, ip_cliente):
    try:
        # Recibir datos del cliente
        mensaje_recibido = cliente_socket.recv(1024).decode('utf-8')
        
        if mensaje_recibido:
            print(f"Mensaje de {ip_cliente}: {mensaje_recibido}")
            
            # Guardar en DB y responder
            timestamp = guardar_mensaje(mensaje_recibido, ip_cliente)
            respuesta = f"Mensaje recibido: <{timestamp}>"
            cliente_socket.send(respuesta.encode('utf-8'))
            
    except Exception as e:
        print(f"Error procesando cliente {ip_cliente}: {e}")
    finally:
        cliente_socket.close()
        print(f"Conexión con {ip_cliente} finalizada.")

# --- Configuración del Socket TCP/IP y Loop Principal ---
def iniciar_servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server_socket.bind(('localhost', 5000))
        server_socket.listen(10) # Aumento del límite de cola de espera
        print("Servidor CONCURRENTE iniciado en localhost:5000...")
        
        while True:
            # El servidor se queda esperando una conexión
            cliente_socket, direccion = server_socket.accept()
            ip_cliente = direccion[0]
            print(f"Nueva conexión desde: {ip_cliente}")
            
            # --- CONCURRENCIA ---
            # Se crea un hilo para que atienda a este cliente
            # Esto evita que el servidor se bloquee mientras guarda en la DB
            hilo = threading.Thread(target=manejar_cliente, args=(cliente_socket, ip_cliente))
            hilo.start()
            
    except socket.error as e:
        print(f"Error de socket: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    iniciar_servidor()