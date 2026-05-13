import requests

def consultar_lol():
    # Usamos a Ahri para variar un poco, o cambia por "Aatrox"
    campeon = "Ahri"
    url = f"https://ddragon.leagueoflegends.com/cdn/14.1.1/data/es_ES/champion/{campeon}.json"
    
    print(f"--- Consultando datos de la Grieta para: {campeon} ---")
    
    try:
        r = requests.get(url)
        if r.status_code == 200:
            res = r.json()
            datos = res['data'][campeon]
            print(f"Campeon: {datos['name']} - {datos['title']}")
            print(f"Ataque: {datos['info']['attack']}")
            print(f"Vida: {datos['stats']['hp']}")
            print("--------------------------------------------------")
            print("Despliege de Francisco Solis finalisado con exito.")
        else:
            print("Error: No se encontro el campeon.")
    except Exception as e:
        print(f"Error de coneccion: {e}")

if __name__ == "__main__":
    consultar_lol()