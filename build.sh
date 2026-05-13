#!/bin/bash
echo "Construyendo la imagen Docker..."
docker build -t api-lol-solis .

echo "Limpiando contenedor previo..."
# Esta línea elimina el contenedor si ya existe para evitar el error de conflicto
docker rm -f samplerunning 2>/dev/null

echo "Ejecutando el contenedor..."
# Se ejecuta la app y debe terminar con código 0
docker run --name samplerunning api-lol-solis