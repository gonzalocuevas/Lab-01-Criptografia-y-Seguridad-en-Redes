import sys

def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            # El offset es 97 para minúsculas en la tabla ASCII
            ascii_offset = 97 if char.islower() else 65
            # Fórmula matemática del cifrado César
            nuevo_char = chr((ord(char) - ascii_offset + desplazamiento) % 26 + ascii_offset)
            resultado += nuevo_char
        else:
            # Los espacios y signos de puntuación se mantienen intactos
            resultado += char
    return resultado

if __name__ == "__main__":
    # Verificamos que se entreguen exactamente 2 argumentos (más el nombre del script)
    if len(sys.argv) != 3:
        print("Uso: python cesar.py \"<texto_a_cifrar>\" <desplazamiento>")
        sys.exit(1)

    texto_original = sys.argv[1]
    
    try:
        desplazamiento = int(sys.argv[2])
    except ValueError:
        print("Error: El desplazamiento debe ser un número entero.")
        sys.exit(1)

    texto_cifrado = cifrar_cesar(texto_original, desplazamiento)
    print(texto_cifrado)