#!/bin/bash
# Script de automatización para examen DRY7122 [cite: 31]

echo "Construyendo la imagen Docker..."
docker build -t api-lol-solis .

echo "Ejecutando el contenedor..."
# El contenedor debe terminar con estado Exited 0 [cite: 33, 50]
docker run --name samplerunning api-lol-solis