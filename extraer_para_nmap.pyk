import xml.etree.ElementTree as ET
import subprocess
from datetime import datetime

# Archivos de trabajo
archivo_xml = "/home/kali/evidencias-test.xml"
archivo_reporte = "/home/kali/reporte_hallazgos.md"

raiz = ET.parse(archivo_xml).getroot()
ips = set()

for item in raiz.findall("item"):
    host_elem = item.find("host")
    if host_elem is not None:
        ip = host_elem.get("ip")
        if ip:
            ips.add(ip)

if not ips:
    print("❌ No se encontraron IPs en el XML.")
    exit()

print(f"\n--- 🚀 Iniciando escaneo y creando reporte ---")

# Abrimos el archivo en modo escritura ("w")
with open(archivo_reporte, "w") as reporte:
    # Escribimos la cabecera del reporte en Markdown
    reporte.write("# 📋 Reporte de Auditoría de Red\n\n")
    reporte.write(f"**Fecha de ejecución:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    reporte.write(f"**Objetivos detectados:** {', '.join(ips)}\n\n")
    reporte.write("## 🔍 Resultados del Escaneo Profundo (Nmap)\n\n")

    for ip in ips:
        print(f"[+] Escaneando TODOS los puertos de {ip}...")
        
        comando = ["nmap", "-p-", "--open", "-sV", "-T4", ip]
        
        try:
            resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
            
            # Escribimos el resultado de Nmap en el reporte usando un bloque de código
            reporte.write(f"### Host: {ip}\n")
            reporte.write("```text\n")
            reporte.write(resultado.stdout)
            reporte.write("```\n\n")
            
            print(f"✅ Escaneo de {ip} completado y guardado.")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error al ejecutar Nmap: {e}")
            reporte.write(f"❌ Error al escanear {ip}\n\n")

print(f"\n🎉 ¡Reporte generado con éxito! Guárdalo en tu portafolio: {archivo_reporte}")
