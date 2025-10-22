from google import genai
import dspy
import requests
from MapsAPI import MapsAPI  # Importa o módulo de mapas
from Modulos import Treinador
from Otimizando import Otimizador
from camera_module import capturar_visao



Treinador = Treinador()
Otimizador = Otimizador()


# Função para obter localização aproximada via IP
def obter_posicao_atual():
    try:
        resposta = requests.get("https://ipinfo.io/json")
        dados = resposta.json()
        loc = dados.get("loc")  # formato "latitude,longitude"
        if loc:
            return loc
        else:
            return "0,0"  # fallback caso não obtenha localização
    except Exception as e:
        print(f"Erro ao obter localização: {e}")
        return "0,0"


# Configuração Gemini 2.5 Pro
API_KEY_GEMINI = "AIzaSyANpwNp7B1MoMq4QUP83dUQAyflxhEEj-E"
client = genai.Client(api_key=API_KEY_GEMINI)
dspy.configure(lm=dspy.LM("gemini-2.5-pro", api_key=API_KEY_GEMINI))


# Configuração Google Maps API
API_KEY_MAPS = "AIzaSyD3fAIwnI8xO_gWfTfbz0mExkey7S63qd8"  # Insira sua chave aqui
maps_api = MapsAPI(API_KEY_MAPS)


base_instruction = """
Você é um agente de IA assistiva para guiar uma pessoa cega. Cheque as imagens da câmera para identificar obstáculos como paredes e use dados do GPS/mapas para sugerir rotas seguras.
"""


def guiar_pessoa(visao_camara, posicao_gps, conhecimento_ambiente, endereco_destino):
    try:
        rota = maps_api.calcular_rota(posicao_gps, endereco_destino)
        instrucoes_mapa = " ".join(rota)
    except Exception as e:
        print(f"Erro ao consultar rota no Google Maps: {e}")
        instrucoes_mapa = "Não foi possível obter instruções de rota no momento."

    # Preparar exemplos para treinamento com DSPy
    exemplos = [
        dspy.Example(
            situation=visao_camara,
            solution="Prover orientação precisa e segura para evitar obstáculos detectados."
        ),
        # Você pode adicionar mais exemplos dinâmicos baseados em dados reais aqui
    ]
    # Treina/adapta o modelo com os exemplos coletados
    Treinador.treinar(exemplos)
    Otimizador.otimizar()

    prompt = f"""
    {base_instruction}
    Situação atual detectada pela câmera: {visao_camara}
    Posição GPS: {posicao_gps}
    Informações do ambiente armazenadas: {conhecimento_ambiente}
    Instruções da rota calculada pelo Google Maps: {instrucoes_mapa}
    Dê um comando textual claro para guiar a pessoa, evitando obstáculos e indicando o melhor caminho.
    """
    resposta = client.models.generate_content(
        model="gemini-2.5-pro",
        contents=prompt
    )
    return resposta.text


# Exemplo de uso
visao_atual = capturar_visao()
posicao_atual = obter_posicao_atual()
print(f"Posição atual obtida: {posicao_atual}")

conhecimento_salvo = "Mapa interno da casa com paredes e portas"
destino = "Praça da Sé, São Paulo"

comando = guiar_pessoa(visao_atual, posicao_atual, conhecimento_salvo, destino)
print("Comando para o usuário:", comando)
