months = 1

deposito = float(input('Qual o depósito inicial: '))
juros = float(input('Qual a taxa de juros mensal: '))
month_value = float(input('Qual a quantidade irá ser investido mensalmente: '))
mensal = int(input('Qual vai ser o período investido em meses: '))

montante = deposito

while months <= mensal:
    montante = montante + (montante * (juros / 100)) + month_value
    print(f'No mês {months} o total de saldo é de R${montante:.2f}')
    months = months + 1
    
print(f'O montante é de R${montante:.2f}, o total de juros foi de R${montante - deposito - (month_value*mensal):.2f}')
