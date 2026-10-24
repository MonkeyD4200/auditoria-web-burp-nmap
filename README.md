# 🛡️ Pipeline de Auditoría Web: Burp Suite ➡️ Nmap ➡️ Gobuster

Este repositorio contiene un conjunto de herramientas automatizadas en Python, diseñadas para agilizar el reconocimiento y la fase de explotación inicial en auditorías web y pruebas de penetración (Pentesting).

## 🛠️ Herramientas Incluidas

*   **`analizar_burp.py`**: Script básico que parsea evidencias exportadas de Burp Suite en formato XML. Clasifica los códigos de estado HTTP (2xx, 3xx, 4xx, 5xx) y resalta visualmente los errores encontrados (⚠️ para errores de cliente y 💥 para errores de servidor).
*   **`extraer_para_nmap.py`**: Script avanzado (Pipeline) que automatiza las siguientes tareas:
    1.  Extrae las IPs únicas de las evidencias de Burp Suite.
    2.  Ejecuta un escaneo profundo de puertos con **Nmap** (`-p- --open -sV -T4`).
    3.  Ejecuta **Gobuster** para buscar directorios ocultos en el servidor web.
    4.  Detecta vulnerabilidades críticas (como la exposición de la carpeta `.git`).
    5.  **Explotación automática:** Si detecta un `.git` expuesto, descarga automáticamente el código fuente (Git Dump) usando `wget`.
    6.  Genera un reporte formal en formato **Markdown** (`reporte_hallazgos.md`) con los resultados y hallazgos de seguridad.

## 💻 Requisitos Previos

Para que los scripts funcionen correctamente en tu entorno (probado en Kali Linux), necesitas tener instaladas las siguientes herramientas:
# 🛡️ Pipeline de Auditoría Web: Burp Suite ➡️ Nmap ➡️ Gobuster

Este repositorio contiene un conjunto de herramientas automatizadas en Python, diseñadas para agilizar el reconocimiento y la fase de explotación inicial en auditorías web y pruebas de penetración (Pentesting).

## 🛠️ Herramientas Incluidas

*   **`analizar_burp.py`**: Script básico que parsea evidencias exportadas de Burp Suite en formato XML. Clasifica los códigos de estado HTTP (2xx, 3xx, 4xx, 5xx) y resalta visualmente los errores encontrados (⚠️ para errores de cliente y 💥 para errores de servidor).
*   **`extraer_para_nmap.py`**: Script avanzado (Pipeline) que automatiza las siguientes tareas:
    1.  Extrae las IPs únicas de las evidencias de Burp Suite.
    2.  Ejecuta un escaneo profundo de puertos con **Nmap** (`-p- --open -sV -T4`).
    3.  Ejecuta **Gobuster** para buscar directorios ocultos en el servidor web.
    4.  Detecta vulnerabilidades críticas (como la exposición de la carpeta `.git`).
    5.  **Explotación automática:** Si detecta un `.git` expuesto, descarga automáticamente el código fuente (Git Dump) usando `wget`.
    6.  Genera un reporte formal en formato **Markdown** (`reporte_hallazgos.md`) con los resultados y hallazgos de seguridad.

## 💻 Requisitos Previos

Para que los scripts funcionen correctamente en tu entorno (probado en Kali Linux), necesitas tener instaladas las siguientes herramientas:

*   [Python 3](https://www.python.org/)
*   [Nmap](https://nmap.org/)
*   [Gobuster](https://github.com/OJ/gobuster)
*   Burp Suite (para generar los archivos XML de evidencia)

## 🚀 Ejemplo de Uso

1.  Exporta tu historial de Burp Suite en formato XML y guárdalo (ej: `evidencias-test.xml`).
2.  Ejecuta el pipeline de auditoría:

```bash
python3 extraer_para_nmap.py
*   [Python 3](https://www.python.org/)
*   [Nmap](https://nmap.org/)
*   [Gobuster](https://github.com/OJ/gobuster)
*   Burp Suite (para generar los archivos XML de evidencia)

## 🚀 Ejemplo de Uso

1.  Exporta tu historial de Burp Suite en formato XML y guárdalo (ej: `evidencias-test.xml`).
2.  Ejecuta el pipeline de auditoría:

```bash
python3 extraer_para_nmap.py
