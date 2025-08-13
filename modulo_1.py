def lin():
    print('='*41)


def cabeçalho(var):
    print('='*41)
    print(var.center(41))
    print('='*41)


def varrerdic(var):
    for a,b in var.items():
        print(f'{a} - {b}')


def intperson(var):
    while True:
        try:
            a = int(input(var))
        except (ValueError, TypeError):
            print('ERRO: Por favor digite um valor inteiro.!')
            continue
        except KeyboardInterrupt:
            print('Não é possível encerrar o programa logo que executado.')
        else:
            return a


def criarArquivo(var):
    try:
        a = open(var, 'w+')
    except:
        print('Não foi possível criar o arquivo')
    else:
        print(f'Arquivo {var} criado com sucesso!')
        a.close
