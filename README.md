# IA Agent com DSPy Framework

## Descrição

Este projeto implementa um agente inteligente programável para orientação e navegação assistiva, focado em usuários com deficiência visual. O agente integra visão computacional, APIs de mapas e aprendizado programável para guiar o usuário de forma segura em ambientes internos e externos.

---

## Tecnologias e Bibliotecas

- **DSPy**: Framework open-source para criação de agentes IA programáveis.
- **Google Gemini API**: Modelo generativo para processamento avançado de linguagem.
- **Ultralytics YOLO**: Detecção e reconhecimento de objetos em imagens e vídeos.
- **OpenCV-Python**: Processamento de imagens e manipulação de vídeos.
- **Requests**: Realização de requisições HTTP para APIs externas (ex: ipinfo.io, Maps API).
- **Python 3.x**

---

## Instalação

Instale as bibliotecas necessárias com:

pip install google-genai dspy-ai ultralytics opencv-python requests


---

## Componentes Principais

- **Assinatura**: Base do agente, definindo seu "contrato" ou missão, incluindo contexto, modelo de IA (ex: Gemini 2.5 Pro), instruções e estratégias.
- **Módulos**: Funções responsáveis por captura da câmera, reconhecimento via YOLO, geração de prompts para o treinamento da IA e armazenamento de dados em cache.
- **Otimizador**: Ajusta o comportamento do agente baseado no feedback do usuário, permitindo autoaperfeiçoamento constante.
- **CameraModule**: Detecta e gerencia dispositivos de câmera para reconhecimento em tempo real.
- **Funções de Navegação**: Cálculo de rotas, triangulação de localização via Wi-Fi/Bluetooth e geração de orientações baseadas na localização atual e destinos.

---

## Como usar

### Exemplo básico de uso:

from assinatura import Assinatura

Criação do agente com modelo Gemini 2.5 Pro
ia = Assinatura(modelo="gemini-2.5-pro", chave_api="SUA_CHAVE_API")

Calcular rota passo a passo para o destino
rota = ia.calcular_rota(origem="Local Atual", destino="Rua Exemplo, 100")
for passo in rota:
print(passo)

Orientar usuário com base em visão, posição e informações do ambiente
ia.guiar_pessoa(visao_atual, posicao_atual, conhecimento_ambiente, destino)


---

## Funcionalidades

- Reconhecimento de objetos e obstáculos em tempo real usando visão computacional.
- Cálculo dinâmico de rotas seguras dentro e fora de ambientes fechados.
- Integração com API de mapas para direções detalhadas.
- Feedback contínuo do usuário para otimização do agente.
- Suporte a múltiplas câmeras e dispositivos.
- Manejo de situações onde a câmera não está disponível.

---

## Avisos importantes

- O agente precisa de acesso à câmera para detecção precisa de obstáculos.
- Em casos de falta de câmera ativa ou falhas na localização, o agente fornece orientações alternativas.
- O uso das APIs externas pode gerar custos dependendo do plano contratado.
- A triangulação da posição depende da disponibilidade de Wi-Fi ou Bluetooth.

---

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar Issues e Pull Requests para ajudar a melhorar a solução.

---

## Contato

Para dúvidas ou sugestões, entre em contato: seu.email@email.com

---

## Licença

Este projeto está licenciado sob a Licença MIT.

