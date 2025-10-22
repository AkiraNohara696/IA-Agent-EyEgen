import requests

class MapsAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://maps.googleapis.com/maps/api/directions/json"


    def calcular_rota(self, origem, destino):
        params = {
            "origin": origem,
            "destination": destino,
            "key": self.api_key
        }
        resposta = requests.get(self.base_url, params=params)
        dados = resposta.json()
        if dados['status'] == 'OK':
            passos = dados['routes'][0]['legs'][0]['steps']
            instrucoes = [passo['html_instructions'] for passo in passos]
            return instrucoes
        else:
            raise Exception(f"Erro ao calcular rota: {dados.get('status')}")

# Exemplo rápido de uso
if __name__ == "__main__":
    api_key_maps = "AIzaSyD3fAIwnI8xO_gWfTfbz0mExkey7S63qd8"
    mapa = MapsAPI(api_key_maps)
    rota = mapa.calcular_rota("Av. Paulista, São Paulo", "Praça da Sé, São Paulo")
    for passo in rota:
        print(passo)
