import xml.etree.ElementTree as ET
from collections import Counter
import argparse

# 1. Configuramos los argumentos de la línea de comandos
parser = argparse.ArgumentParser(description="Analizador de evidencias de Burp Suite")
parser.add_argument("-e", "--errores", action="store_true", help="Mostrar solo errores (4xx y 5xx)")
parser.add_argument("-f", "--file", default="/home/kali/evidencias-varias.xml", help="Ruta del archivo XML")
args = parser.parse_args()

# Usamos el archivo que pase el usuario, o el de por defecto
archivo = args.file

try:
    raiz = ET.parse(archivo).getroot()
except FileNotFoundError:
    print(f"❌ Error: No se encontró el archivo {archivo}")
    exit(1)

estados = [item.findtext("status") for item in raiz.findall("item")]

# Si NO se pide el modo errores, mostramos los resúmenes
if not args.errores:
    print("\n--- Resumen de estados HTTP ---")
    for estado, cantidad in sorted(Counter(estados).items()):
        print(f"Estado {estado}: {cantidad} respuesta(s)")

    familias = {
        "2xx (éxito)": 0, "3xx (redirección)": 0,
        "4xx (error cliente)": 0, "5xx (error servidor)": 0,
    }

    for estado in estados:
        try:
            codigo = int(estado)
        except (TypeError, ValueError):
            continue
        if 200 <= codigo < 300: familias["2xx (éxito)"] += 1
        elif 300 <= codigo < 400: familias["3xx (redirección)"] += 1
        elif 400 <= codigo < 500: familias["4xx (error cliente)"] += 1
        elif 500 <= codigo < 600: familias["5xx (error servidor)"] += 1

    print("\n--- Clasificación por familia ---")
    for fam, cant in familias.items():
        print(f"{fam}: {cant}")

print("\n--- Detalle de evidencias ---")
for item in raiz.findall("item"):
    estado = item.findtext("status")
    try:
        codigo = int(estado)
    except (TypeError, ValueError):
        codigo = 0

    # EL FILTRO MÁGICO: Si pidió solo errores y no es 4xx/5xx, nos lo saltamos
    if args.errores and not (400 <= codigo < 600):
        continue

    print("\n" + "-"*40)
    print("URL:", item.findtext("url"))
    # Protección por si el XML no tiene IP en el host
    host_elem = item.find("host")
    ip = host_elem.get("ip") if host_elem is not None else "N/A"
    
    print("IP:", ip)
    print("Puerto:", item.findtext("port"))
    print("Método:", item.findtext("method"))
    print("Ruta:", item.findtext("path"))
    print("Estado HTTP:", estado)
    print("Tamaño respuesta:", item.findtext("responselength"))
    print("Tipo de contenido:", item.findtext("mimetype"))

    if 400 <= codigo < 500:
        print("⚠️  ERROR DEL CLIENTE (4xx) — revisar ruta o parámetros")
    elif 500 <= codigo < 600:
        print("💥 ERROR DEL SERVIDOR (5xx) — la aplicación falló")
