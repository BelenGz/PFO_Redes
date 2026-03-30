import socket

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
            cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente_socket.connect((host, puerto))

            cliente_socket.send(mensaje.encode('utf-8'))

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