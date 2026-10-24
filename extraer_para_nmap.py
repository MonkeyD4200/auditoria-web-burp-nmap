import xml.etree.ElementTree as ET
import subprocess
from datetime import datetime

archivo_xml = "/home/kali/evidencias-test.xml"
archivo_reporte = "/home/kali/reporte_hallazgos.md"
url_objetivo = "http://127.0.0.1:8000"

# Variables para guardar la info
resultado_nmap = ""
salida_gobuster = ""
hallazgos = []

print("\n--- 🚀 Iniciando Auditoría Completa ---")

# 1. ESCANEO DE RED (Nmap)
print("[+] Ejecutando Nmap...")
try:
    raiz = ET.parse(archivo_xml).getroot()
    ips = {item.find("host").get("ip") for item in raiz.findall("item") if item.find("host") is not None}
    
    for ip in ips:
        comando_nmap = ["nmap", "-p-", "--open", "-sV", "-T4", ip]
        res = subprocess.run(comando_nmap, capture_output=True, text=True, check=True)
        resultado_nmap += res.stdout + "\n"
except Exception as e:
    print(f"Error en Nmap: {e}")

# 2. FUZZING WEB (Gobuster) y EXPLOTACIÓN
print("[+] Ejecutando Gobuster y buscando vulnerabilidades...")
try:
    comando_gobuster = ["gobuster", "dir", "-u", url_objetivo, "-w", "/usr/share/wordlists/dirb/common.txt", "-q"]
    res = subprocess.run(comando_gobuster, capture_output=True, text=True, check=True)
    salida_gobuster = res.stdout

    if ".git/HEAD" in salida_gobuster:
        hallazgos.append("⚠️ CRÍTICO: Repositorio .git expuesto. Riesgo de fuga de código fuente.")
        print("[!] ¡Vulnerabilidad .git detectada! Iniciando descarga automática...")
        
        subprocess.run(["rm", "-rf", "/tmp/dump_auto"]) 
        comando_wget = ["wget", "-r", "-q", "-P", "/tmp/dump_auto", f"{url_objetivo}/.git/"]
        
        try:
            subprocess.run(comando_wget, check=True)
            hallazgos.append("✅ EXPLOTACIÓN EXITOSA: Se descargó el código fuente de la aplicación.")
            print("[+] Código fuente descargado en /tmp/dump_auto")
        except subprocess.CalledProcessError:
            print("[-] Falló la descarga automática.")
except Exception as e:
    print(f"Error en Gobuster: {e}")

# 3. GENERAR REPORTE (Modo "w" para sobrescribir limpio)
print("\n[+] Generando reporte final...")
with open(archivo_reporte, "w") as reporte:
    reporte.write("# 📋 Reporte de Auditoría Web Completa\n\n")
    reporte.write(f"**Fecha de ejecución:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    reporte.write("## 🔍 Resultados del Escaneo Profundo (Nmap)\n")
    reporte.write("```text\n" + (resultado_nmap if resultado_nmap else "No se realizaron escaneos.") + "```\n\n")
    
    reporte.write("## 🕸️ Análisis de Directorios (Gobuster)\n")
    reporte.write(f"**Objetivo:** {url_objetivo}\n\n")
    
    if hallazgos:
        reporte.write("### 🚨 Hallazgos de Seguridad:\n")
        for h in hallazgos:
            reporte.write(f"- {h}\n")
    else:
        reporte.write("- No se encontraron vulnerabilidades en la lista básica.\n")

    reporte.write("\n<details>\n<summary>Ver salida completa de Gobuster</summary>\n\n")
    reporte.write("```text\n" + salida_gobuster + "```\n</details>\n")

print(f"\n🎉 ¡Reporte generado con éxito en {archivo_reporte}!")
