import yfinance as yf

def buscar_melhores_investimentos():
    try:
        # Ativos conservadores de verdade e que funcionam com yfinance
        ativos = {
            "BBAS3.SA": "Banco do Brasil",
            "IVVB11.SA": "ETF S&P 500",
            "HGLG11.SA": "FII CSHG Logística"
        }

        mensagem = "📈 Top 3 Investimentos Conservadores do Dia:\n\n"

        for codigo, nome in ativos.items():
            ativo = yf.Ticker(codigo)
            dados = ativo.history(period="1d")

            if dados.empty:
                mensagem += f"- {nome} ({codigo}): Dados não disponíveis\n"
                continue

            preco = dados["Close"].iloc[-1]
            preco_ant = dados["Open"].iloc[-1]
            variacao = ((preco - preco_ant) / preco_ant) * 100

            mensagem += f"- {nome}: R${preco:.2f} ({variacao:+.2f}%)\n"

        return mensagem

    except Exception as e:
        return f"Erro ao buscar dados com yfinance: {str(e)}"
