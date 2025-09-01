# atividade_1.py
#Esse vai ser usadoo, comparar com o primeiro codigo


from graphviz import Digraph
import random


# Classe para os nós da árvore

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


# Função para avaliar a árvore

def avaliar(no):
    if no is None:
        return 0
    # Se for folha (número)
    if no.esquerda is None and no.direita is None:
        return float(no.valor)
    # Avaliar subárvores
    valor_esq = avaliar(no.esquerda)
    valor_dir = avaliar(no.direita)
    # Aplicar operador
    if no.valor == '+':
        return valor_esq + valor_dir
    elif no.valor == '-':
        return valor_esq - valor_dir
    elif no.valor == '*':
        return valor_esq * valor_dir
    elif no.valor == '/':
        return valor_esq / valor_dir
    else:
        raise ValueError(f"Operador desconhecido: {no.valor}")


# Função para gerar imagem da árvore com graphviz

def gerar_imagem(root, filename):
    dot = Digraph()

    def adicionar_nos(no):
        if no is None:
            return
        # Diferencia operadores e números com cores
        if str(no.valor) in '+-*/':
            dot.node(str(id(no)), str(no.valor), shape='circle', style='filled', color='lightblue')
        else:
            dot.node(str(id(no)), str(no.valor), shape='box', style='filled', color='lightgreen')
        if no.esquerda:
            adicionar_nos(no.esquerda)
            dot.edge(str(id(no)), str(id(no.esquerda)))
        if no.direita:
            adicionar_nos(no.direita)
            dot.edge(str(id(no)), str(id(no.direita)))

    adicionar_nos(root)
    dot.render(filename, format='png', view=True)
    print(f"Imagem da árvore salva em {filename}.png")


# Função para gerar árvore aleatória

def gerar_arvore_aleatoria():
    operadores = ['+', '-', '*', '/']
    numeros = [str(random.randint(1, 10)) for _ in range(3)]
    ops = random.choices(operadores, k=2)

    # Construir árvore: (num1 op1 num2) op2 num3
    raiz = No(ops[1])
    raiz.esquerda = No(ops[0])
    raiz.esquerda.esquerda = No(numeros[0])
    raiz.esquerda.direita = No(numeros[1])
    raiz.direita = No(numeros[2])

    return raiz


# MAIN

if __name__ == "__main__":
    # Árvore fixa
    raiz_fixa = No('*')
    raiz_fixa.esquerda = No('+')
    raiz_fixa.esquerda.esquerda = No('7')
    raiz_fixa.esquerda.direita = No('3')
    raiz_fixa.direita = No('-')
    raiz_fixa.direita.esquerda = No('5')
    raiz_fixa.direita.direita = No('2')

    print("Árvore fixa:")
    resultado_fixa = avaliar(raiz_fixa)
    print(f"Resultado da expressão fixa: {resultado_fixa}")
    gerar_imagem(raiz_fixa, "arvore_fixa")

    # Árvore aleatória
    raiz_aleatoria = gerar_arvore_aleatoria()
    print("\nÁrvore aleatória:")
    resultado_aleatoria = avaliar(raiz_aleatoria)
    print(f"Resultado da expressão aleatória: {resultado_aleatoria}")
    gerar_imagem(raiz_aleatoria, "arvore_aleatoria")
