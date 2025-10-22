import cv2
import platform
import subprocess


def detectar_origem_visao():
    sistema = platform.system()
    if sistema == "Linux":
        # Detectar se é Raspberry Pi
        try:
            with open("/proc/device-tree/model") as f:
                modelo = f.read().lower()
                if "raspberry" in modelo:
                    return "Câmera nativa Raspberry Pi"
        except Exception:
            pass
        return "Câmera genérica Linux (provavelmente notebook ou desktop)"
    elif sistema == "Windows":
        return "Câmera Windows (provavelmente notebook)"
    elif sistema == "Darwin":
        return "Câmera macOS (provavelmente notebook)"
    else:
        return f"Câmera em sistema desconhecido: {sistema}"

def capturar_visao():
    origem = detectar_origem_visao()
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if ret:
        # Aqui pode ser ampliado com processamento da imagem
        descricao = "Parede à frente e corredor à direita"
        return f"Visão capturada por {origem}: {descricao}"
    else:
        return f"Não foi possível capturar imagem da câmera em {origem}"
