import pytest
import requests
from src.app import obter_frase_motivacional

def test_obter_frase_motivacional_sucesso():
    """Testa se a função consegue se conectar à API externa e retornar uma string válida."""
    frase = obter_frase_motivacional()
    
    # O teste valida se o retorno não é vazio
    assert frase is not None
    assert isinstance(frase, str)
    assert len(frase) > 0

def test_estrutura_api_externa():
    """Testa diretamente a resposta da API para garantir que o formato não mudou."""
    url = 'https://api.allorigins.win/raw?url=https://zenquotes.io/api/random'
    response = requests.get(url, timeout=5)
    
    assert response.status_code == 200
    dados = response.json()
    
    # Valida se a API retorna uma lista e se o primeiro item tem a chave da frase 'q' e do autor 'a'
    assert isinstance(dados, list)
    assert 'q' in dados[0]
    assert 'a' in dados[0]
