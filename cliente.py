import socket

# --- Configuración y Ciclo de Vida del Cliente ---
def iniciar_cliente():
    host = 'localhost'
    puerto = 5000

    print("--- Cliente de Chat Iniciado ---")
    print("Escribe tus mensajes. Para salir, escribe 'éxito'.")

    while True:
        mensaje = input("Tu mensaje: ")

        # Filtro para no enviar la palabra de salida al servidor
        if mensaje.lower() == 'éxito':
            print("Cerrando programa...")
            break

        try:
            # Configuración de conexión por cada mensaje
            cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente_socket.connect((host, puerto))
            
            # Serialización y envío
            cliente_socket.send(mensaje.encode('utf-8'))

            # Recepción de confirmación del servidor
            respuesta = cliente_socket.recv(1024).decode('utf-8')
            print(f"Respuesta del Servidor -> {respuesta}")

            cliente_socket.close()

        except ConnectionRefusedError:
            print("Error: Servidor no disponible.")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

if __name__ == "__main__":
    iniciar_cliente()