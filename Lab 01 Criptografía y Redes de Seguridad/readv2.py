import sys
from scapy.all import rdpcap, ICMP
from colorama import init, Fore, Style

init(autoreset=True)

def extraer_mensaje_y_atacar(pcap_file):
    print(f"[*] Leyendo archivo de captura: {pcap_file}...")
    try:
        paquetes = rdpcap(pcap_file)
    except Exception as e:
        print(f"[-] Error al leer el archivo pcapng: {e}")
        sys.exit(1)

    caracteres = []
    
    # Recorremos los paquetes buscando ICMP Echo Requests (type == 8)
    # AÑADIMOS EL FILTRO: Solo leemos los paquetes con el ID 1234 de nuestro script stealth
    for pkt in paquetes:
        if pkt.haslayer(ICMP) and pkt[ICMP].type == 8 and pkt[ICMP].id == 1234:
            payload = bytes(pkt[ICMP].payload)
            if len(payload) > 0:
                char_oculto = chr(payload[0])
                caracteres.append(char_oculto)

    mensaje_cifrado = "".join(caracteres)
    print(f"[*] Mensaje cifrado extraído del tráfico: {mensaje_cifrado}\n")
    print("--- INICIANDO FUERZA BRUTA (CIFRADO CESAR) ---")

    for i in range(1, 26):
        texto_descifrado = ""
        for char in mensaje_cifrado:
            if char.isalpha():
                ascii_offset = 97 if char.islower() else 65
                nuevo_char = chr((ord(char) - ascii_offset - i) % 26 + ascii_offset)
                texto_descifrado += nuevo_char
            else:
                texto_descifrado += char

        if i == 9:
            print(f"{Fore.GREEN}{i:2d}  {texto_descifrado}{Style.RESET_ALL}")
        else:
            print(f"{i:2d}  {texto_descifrado}")

if __name__ == "__main__":
    archivo_pcap = sys.argv[1] if len(sys.argv) > 1 else "cesar.pcapng"
    extraer_mensaje_y_atacar(archivo_pcap)