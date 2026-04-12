def adicionar_medicamento(lista, nome, horario):
    if not nome or not horario:
        return "Erro: Nome e horário são obrigatórios."
    medicamento = {"nome": nome, "horario": horario}
    lista.append(medicamento)
    return f"Medicamento {nome} adicionado com sucesso!"

def listar_medicamentos(lista):
    if not lista:
        return "Nenhum medicamento agendado."
    return "\n".join([f"- {m['nome']}: {m['horario']}" for m in lista])

if __name__ == "__main__":
    banco_dados = []
    print("--- Bem-vindo ao MedControl ---")
    # Exemplo de uso simples (Interface CLI)
    print(adicionar_medicamento(banco_dados, "Dipirona", "08:00"))
    print(listar_medicamentos(banco_dados))
