class Treinador:
    def __init__(self):
        pass

    def treinar(self, exemplos):
        print("Treinando com exemplos:", exemplos)

import dspy
import cv2
from ultralytics import YOLO

# Função YOLO: detecta objetos e cria situação descritiva
def detectar_situacao_yolo(imagem_path='captura.jpg'):
    model = YOLO('yolov8n.pt')  # Use um modelo leve para testes rápidos
    resultados = model(imagem_path)
    objetos_detectados = set()
    for resultado in resultados:
        for box in resultado.boxes:
            nome = model.names[int(box.cls)]
            objetos_detectados.add(nome)
    if not objetos_detectados:
        return "Nenhum objeto detectado"
    # Monta descrição da situação
    objs_txt = ", ".join(objetos_detectados)
    return f"Objetos detectados à frente: {objs_txt}"

# Função para capturar imagem da câmera e salvar temporariamente
def capturar_imagem(frame_path='captura.jpg'):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if ret:
        cv2.imwrite(frame_path, frame)
        return frame_path
    else:
        return None

# Função DSPy para criar prompts de orientação baseados nas situações YOLO ou manuais
def gerar_prompt_auto(exemplos):
    prompts = []
    for ex in exemplos:
        prompt = (
            f"Situação: {ex.situation}\n"
            f"Solução: {ex.solution}\n"
            "Dê uma orientação detalhada para ajudar na navegação."
        )
        prompts.append(prompt)
    return prompts

# Exemplos manuais DSPy
exemplo1 = dspy.Example(
    situation="Parede detectada à frente",
    solution="Oriente a pessoa a ir para o lado direito, onde há espaço livre."
)
exemplo2 = dspy.Example(
    situation="Pessoa dentro de casa, corredor bloqueado",
    solution="Buscar uma saída alternativa utilizando mapa interno e visão da câmera."
)

# Realiza captura e detecção automática com YOLO
imagem = capturar_imagem()
if imagem:
    situacao_yolo = detectar_situacao_yolo(imagem)
    exemplo3 = dspy.Example(
        situation=situacao_yolo,
        solution="Forneça instruções seguras para navegação considerando a posição dos objetos detectados."
    )
    treinamento = [exemplo1, exemplo2, exemplo3]
else:
    print("Não foi possível capturar imagem da câmera, usando apenas exemplos manuais.")
    treinamento = [exemplo1, exemplo2]

# Gera prompts de treinamento/adaptação
prompts_gerados = gerar_prompt_auto(treinamento)
for p in prompts_gerados:
    print("="*40)
    print(p)
