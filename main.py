import os

list_compras = []

while True:
    print(f'{10*'*'} Lista de Compras {'*'*10}\n')
    print('Selecione uma opção:')
    acao_digit = input('[i]nseir [a]pagar [l]istar: ').lower()

    if len(acao_digit) > 1:
        print('Opção invalida')
        continue


    if acao_digit == 'i':
        os.system('cls')
        valor = input('Valor: ')
        list_compras.append(valor)
        os.system('cls')
        
        for indice, item in enumerate(list_compras):
            print(indice, item)

    elif acao_digit == 'a':
        if len(list_compras) == 0:
            print('Nada para deletar')

        else:
            os.system('cls')
            num_i = 0

            for i, n in enumerate(list_compras):
                print(i, n)
            
            deletar = input('Escolha um indice para deletar: ')

            try:
                num_i = int(deletar)
            except:
                print(f'{deletar} não é um numero')
                continue
            
            if num_i > len(list_compras) - 1 or num_i < 0:
                print('numero invalido')
                continue 
            else:
                print(f'item {list_compras[num_i]} foi deletado com sucesso!')
                list_compras.pop(num_i)

    elif acao_digit == 'l':
        if len(list_compras) == 0:
            print('Nada para listar')

        else:
            for indice, c in enumerate(list_compras):
                print(indice, c)
    else: 
        print('Opção invalida')

