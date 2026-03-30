# PFO 1: Chat Cliente-Servidor con Sockets y SQLite
Este proyecto implementa un sistema de mensajería básico siguiendo el modelo cliente-servidor, desarrollado para la materia **Programación sobre Redes**.

## Características
**Socket TCP/IP**: Configurado en `localhost:5000`.
**Persistencia**: Uso del módulo `sqlite3` para almacenar mensajes con `id`, `contenido`, `fecha_envio` e `ip_cliente`.
**Modularización**: Código organizado en funciones para inicializar sockets, manejar conexiones y gestionar la DB.
**Manejo de Errores**: Control de excepciones para puertos ocupados y accesibilidad de la base de datos.

**Programación Concurrente**: 
   El servidor utiliza la librería `threading` para gestionar múltiples conexiones en paralelo. Cada cliente que se conecta dispara un nuevo hilo, evitando que el proceso principal se bloquee durante las operaciones de Entrada/Salida (I/O).
**Sincronización**: 
   Se contempla la exclusión mutua mediante los mecanismos internos de `sqlite3`. Al realizar operaciones de `commit`, el motor gestiona el bloqueo del archivo para evitar condiciones de carrera cuando varios hilos intentan escribir simultáneamente.

## Instrucciones de Ejecución
**Preparar DB**: Ejecutar `python database.py` para crear la estructura de tablas.
**Lanzar Servidor**: Ejecutar `python servidor.py`.
**Lanzar Cliente**: Ejecutar `python cliente.py` en una o más terminales adicionales.
**Finalizar**: Escribir la palabra `éxito` en el cliente para cerrar el programa sin afectar la base de datos.

## Estructura del Proyecto
`servidor.py`: Lógica multihilo del socket servidor.
`cliente.py`: Interfaz de usuario para envío de mensajes.
`database.py`: Script de inicialización de SQLite.
`mensajes.db`: Archivo de base de datos.
