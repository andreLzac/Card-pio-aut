nome = input('Digite seu nome')
print (f'Ola {nome}')
peso = float(input('Agora digite seu peso').replace(",", "."))
print (f'Otimo!')
altura = float(input('Digite sua altura').replace(",", "."))

imc = peso / (altura ** 2)

# Classificações
if imc < 18.5:
    classificacao = "abaixo do peso"
elif imc < 25:
    classificacao = "peso normal"
elif imc < 30:
    classificacao = "sobre peso"
elif imc < 35:
    classificacao = "obesidade grau 1"
elif imc < 40:
    classificacao = "obesidade grau 2"
else:
    classificacao = "obesidade grau 3"

print(f'sr. {nome} seu imc é {imc:.2f} em base do seu imc você esta na categoria {classificacao}, obrigado!')