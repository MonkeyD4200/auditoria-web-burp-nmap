import xml.etree.ElementTree as ET
import subprocess
from datetime import datetime

archivo_xml = "/home/kali/evidencias-test.xml"
archivo_reporte = "/home/kali/reporte_hallazgos.md"

# 1. Configuramos un objetivo fijo para probar (nuestro servidor local)
url_objetivo = "http://127.0.0.1:8000"

print(f"\n--- 🚀 Iniciando Fuzzing Web con Gobuster en {url_objetivo} ---")

# 2. Comando de Gobuster
comando = ["gobuster", "dir", "-u", url_objetivo, "-w", "/usr/share/wordlists/dirb/common.txt", "-q"]

try:
    resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
    salida_gobuster = resultado.stdout

    print("✅ Fuzzing completado. Analizando resultados...")

    # 3. Analizamos la salida buscando cosas peligrosas
    hallazgos_criticos = []
    if ".git/HEAD" in salida_gobuster or ".git/config" in salida_gobuster:
        hallazgos_criticos.append("⚠️ CRÍTICO: Repositorio .git expuesto. Riesgo de fuga de código fuente.")
    
    # (Aquí podrías agregar más reglas, como buscar /admin, /backup.zip, etc.)

    # 4. Escribimos el reporte
    with open(archivo_reporte, "a") as reporte: # Modo "a" para añadir al final, no sobrescribir
        reporte.write("\n## 🕸️ Análisis de Directorios Ocultos (Gobuster)\n\n")
        reporte.write(f"**Objetivo:** {url_objetivo}\n\n")
        
        if hallazgos_criticos:
            reporte.write("### 🚨 Hallazgos de Seguridad:\n")
            for hallazgo in hallazgos_criticos:
                reporte.write(f"- {hallazgo}\n")
        else:
            reporte.write("- No se encontraron directorios críticos expuestos en la lista básica.\n")

        reporte.write("\n<details>\n<summary>Ver salida completa de Gobuster</summary>\n\n")
        reporte.write("```text\n")
        reporte.write(salida_gobuster)
        reporte.write("```\n</details>\n")

    print(f"\n🎉 ¡Reporte actualizado con los hallazgos de Gobuster!")

except subprocess.CalledProcessError as e:
    print(f"❌ Error al ejecutar Gobuster: {e}")
