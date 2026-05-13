import requests
import urllib3
import sys

# Configuración de seguridad para entornos locales
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class LoLChampionApp:
    """Clase para gestionar la obtención de datos de League of Legends."""
    
    API_URL = "https://ddragon.leagueoflegends.com/cdn/13.18.1/data/es_ES/champion/Ahri.json"

    def __init__(self, champion_name="Ahri"):
        self.champion_name = champion_name

    def fetch_data(self):
        """Obtiene los datos crudos de la API."""
        try:
            # Usamos verify=False por los problemas de SSL en Windows que vimos antes
            response = requests.get(self.API_URL, timeout=10, verify=False)
            response.raise_for_status()
            return response.json()
        except Exception as err:
            print(f"Error al conectar con la API: {err}")
            return None

    def display_stats(self, data):
        """Muestra los datos usando caracteres estándar compatibles con Windows."""
        if not data or 'data' not in data:
            print("No se pudieron procesar los datos.")
            return

        champion = data['data'][self.champion_name]
        
        # Diseño compatible con CMD de Windows y Docker
        print("\n" + "+" + "-"*45 + "+")
        print(f"| PERFIL DE CAMPEON: {champion['name'].upper():<24} |")
        print(f"| Titulo: {champion['title'].capitalize():<35} |")
        print("+" + "-"*45 + "+")
        print(f"| ESTADISTICAS BASE:                         |")
        print(f"|  * Ataque: {champion['info']['attack']:<31} |")
        print(f"|  * Defensa: {champion['info']['defense']:<30} |")
        print(f"|  * Vida: {champion['stats']['hp']:<33} |")
        print("+" + "-"*45 + "+")
        print("\n*** DESPLIEGUE DE FRANCISCO SOLIS FINALIZADO CON EXITO ***\n")

def main():
    app = LoLChampionApp()
    data = app.fetch_data()
    app.display_stats(data)

if __name__ == "__main__":
    main()