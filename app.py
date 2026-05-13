import requests
import os
import sys

def get_lol_data():
    # REQUERIMIENTO: Uso de variables de entorno mediante os [cite: 27, 55]
    api_url = os.getenv('API_URL_LOL', 'https://ddragon.leagueoflegends.com/cdn/13.18.1/data/es_ES/champion/Ahri.json')
    
    try:
        response = requests.get(api_url, timeout=10)
        
        # REQUERIMIENTO: Manejo de >=4 tipos de errores [cite: 25, 50]
        response.raise_for_status() # Maneja errores 4XX y 5XX
        
        data = response.json()
        stats = data['data']['Ahri']
        
        # REQUERIMIENTO: Procesar >=3 campos de datos [cite: 25, 48]
        print(f"ID: {stats['id']}")             # Campo 1
        print(f"Title: {stats['title']}")       # Campo 2
        print(f"HP: {stats['stats']['hp']}")    # Campo 3
        
        print("\nDespliegue de Francisco Solis finalizado con exito.")

    except requests.exceptions.HTTPError as errh:
        print(f"Error HTTP (404/500): {errh}")
    except requests.exceptions.ConnectionError:
        print("Error de Conexión: Verifique su red.")
    except requests.exceptions.Timeout:
        print("Error de Tiempo: La solicitud expiro.")
    except requests.exceptions.RequestException as err:
        print(f"Error inesperado: {err}")

if __name__ == "__main__":
    get_lol_data()