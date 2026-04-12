from src.app import adicionar_medicamento, listar_medicamentos

def test_adicionar_medicamento_sucesso():
    lista = []
    resultado = adicionar_medicamento(lista, "Aspirina", "10:00")
    assert len(lista) == 1
    assert "sucesso" in resultado

def test_adicionar_medicamento_vazio():
    lista = []
    resultado = adicionar_medicamento(lista, "", "")
    assert "Erro" in resultado

def test_listar_vazio():
    lista = []
    assert listar_medicamentos(lista) == "Nenhum medicamento agendado."
