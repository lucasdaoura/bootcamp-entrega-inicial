import requests

def obter_frase_motivacional():
    """Busca uma frase motivacional em uma API pública."""
    try:
        # Requisição HTTP GET para a API pública de citações
        response = requests.get('https://api.allorigins.win/raw?url=https://zenquotes.io/api/random', timeout=5)
        if response.status_code == 200:
            dados = response.json()
            if dados and len(dados) > 0:
                return f'"{dados[0]["q"]}" — {dados[0]["a"]}'
        return "Foque nos seus objetivos e faça acontecer!"
    except Exception:
        # Fallback caso a internet falhe, garantindo que a aplicação não quebre
        return "Tenha um excelente dia de produtividade!"

def exibir_menu():
    tarefas = []
    
    # Consome a API e exibe o resultado logo na inicialização do app
    frase = obter_frase_motivacional()
    
    while True:
        print("\n=========================================")
        print("🌟 INSPIRAÇÃO DO DIA:")
        print(frase)
        print("=========================================")
        print("     GERENCIADOR DE TAREFAS (CLI)     ")
        print("=========================================")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Sair")
        print("=========================================")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            tarefa = input("Digite a nova tarefa: ")
            tarefas.append(tarefa)
            print("✔️ Tarefa adicionada com sucesso!")
        elif opcao == "2":
            if not tarefas:
                print("📋 Nenhuma tarefa cadastrada.")
            else:
                print("\n📋 SUAS TAREFAS:")
                for i, t in enumerate(tarefas, 1):
                    print(f"{i}. {t}")
        elif opcao == "3":
            print("Saindo... Tenha um ótimo dia!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    exibir_menu()
