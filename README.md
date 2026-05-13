# Solución Profesional: Extractor de Estadísticas LoL
**Estudiante:** Francisco Solis  
**Asignatura:** Programación y Redes Virtualizadas (DRY7122)

## 1. Definición del Contexto (Narrativa)
* **Stakeholder:** Analista Técnico de eSports / Coach de equipo profesional.
* **Propuesta de Valor:** Esta herramienta automatiza la extracción de estadísticas base de campeones desde la API de Riot Games. Resuelve el problema de la búsqueda manual de datos durante la fase de "Draft" en torneos, permitiendo al analista obtener información técnica (HP, Título, ID) de forma instantánea y centralizada.

## 2. Guía de Configuración
* **Tecnologías:** Python 3.9, Docker, Jenkins.
* **Variables de Entorno:** El script utiliza `API_URL_LOL` para definir el endpoint de la API, cumpliendo con los estándares de seguridad (no hardcoding).

## 3. Instrucciones de Ejecución
1. **Construir la imagen:** `bash build.sh` (o `docker build -t api-lol-solis .`)
2. **Ejecutar contenedor:** `docker run --name samplerunning api-lol-solis`
3. **Ver resultados:** Los datos se desplegarán en la consola.