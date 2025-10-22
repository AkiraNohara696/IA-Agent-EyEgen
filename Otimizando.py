from Modulos import gerar_prompt_auto, treinamento

def melhorar_codigo(feedback_usuario, logs_decisoes, base_prompts):
    """
    Analisa feedback e logs, sugere melhorias nos prompts para clareza e eficácia.
    """
    ajustes = []
    for prompt in base_prompts:
        if "confuso" in feedback_usuario.lower():
            ajuste = prompt.replace("Dê uma orientação detalhada", "Dê uma orientação clara e passo a passo")
            ajustes.append(ajuste)
        else:
            ajustes.append(prompt)
    return ajustes

# Exemplo de execução
feedback = "Algumas vezes as instruções ficaram confusas quando perto da parede."
logs = ["Parede detectada", "Orientar para a direita"]
prompts_atual = gerar_prompt_auto(treinamento)
prompts_melhorados = melhorar_codigo(feedback, logs, prompts_atual)

print("Prompts melhorados:")
for pm in prompts_melhorados:
    print(pm)

class Otimizador:
    def __init__(self):
        pass

    def otimizar(self):
        print("Otimização realizada.")
