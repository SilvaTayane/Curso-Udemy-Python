import json

from exerc1poo import CAMINHO_ARQUIVO, Pessoa

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    
    for pessoa in pessoas:
        p1 = Pessoa(**pessoa[0])
        r