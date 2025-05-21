from investimentos import buscar_melhores_investimentos
from whatsapp import enviar_whatsapp

def main():
    print("🔍 Buscando os melhores investimentos conservadores...")
    mensagem = buscar_melhores_investimentos()

    if mensagem.startswith("Erro"):
        print("❌ Ocorreu um erro ao tentar gerar a mensagem:")
        print(mensagem)
    else:
        print("📤 Enviando mensagem via WhatsApp...")
        enviar_whatsapp(mensagem)

if __name__ == "__main__":
    main()
