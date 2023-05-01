# ------------ Começo da função Dimensão Objeto ---------------------
def dimensaoobjeto():
    while True:
        altura = float(input('Qual a altura (em cm)? '))
        comprimento = float(input('Qual o comprimento (em cm)? '))
        largura = float(input('Qual a largura (em cm) do objeto? '))
        dimensao = altura * largura * comprimento

        limites_dimensoes = [(0, 1000, 10.00),
                             (1000, 10000, 20.00),
                             (10000, 30000, 30.00),
                             (30000, 100000, 50.00)]

        for limite in limites_dimensoes:
            if limite[0] < dimensao <= limite[1]:
                return limite[2]

        print('Este volume/dimensões não são aceitos. Tente novamente com um valor válido.')
# -------------- Fim da função Dimensão Objeto ---------------------
# ------------ Começo da função Peso Objeto ------------------------
def pesoobjeto():
    while True:
        try:
            peso = float(input('Digite o peso do objeto: '))
            if peso <= 0.1:
                return 1
            elif peso < 1:
                return 1.5
            elif peso < 10:
                return 2
            elif peso < 30:
                return 3
            else:
                print('Este peso não é aceito ou a informação não é válida. Tente novamente com um valor válido.')
        except ValueError:
            print('Este peso não é aceito ou a informação não é válida. Tente novamente com um valor válido.')
# -------------- Fim da função Peso Objeto ----------------------
# -------------- Começo da função Rota Objeto -------------------
def rotaobjeto():
    rotas_validas = {
        "RS - De Rio de Janeiro até São Paulo": 1,
        "SR - De São Paulo até Rio de Janeiro": 1,
        "BS - De Brasília até São Paulo": 1.2,
        "SB - De São Paulo até Brasília": 1.2,
        "BR - De Brasília até Rio de Janeiro": 1.5,
        "RB - Rio de Janeiro até Brasília": 1.5
    }

    while True:
        rota = input('Digite a rota do objeto: \n'
            'Rotas disponíveis: RS - De Rio de Janeiro até São Paulo; \n'
            'SR - De São Paulo até Rio de Janeiro \n'
            'BS - De Brasília até São Paulo \n'
            'SB - De São Paulo até Brasília \n'
            'BR - De Brasília até Rio de Janeiro \n'
            'RB - Rio de Janeiro até Brasília')
        if rota in rotas_validas:
            return rotas_validas[rota]
        else:
            print('Esta rota não é válida. Tente novamente.')

# -------------- Fim da função Rota Objeto ---------------------
# ------------ Começo da main ----------------------------------
print('Bem-vindo ao serviço de entrega da Daniela!')
dimensao2 = dimensaoobjeto()
peso = pesoobjeto()
rota = rotaobjeto()
total = dimensao2 * peso * rota
print("O valor total é de R$ {:.2f}.".format(total))
# -------------- Fim da main ---------------------