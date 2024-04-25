nome = input('Nome do herói: ')
quant_xp = int(input('Quantidade de XP: '))
classificacao = 0

if quant_xp < 1000:
    classificacao = 'Ferro'
elif quant_xp > 1001 and quant_xp < 2000:
    classificacao = 'Bronze'
elif quant_xp > 2001 and quant_xp < 5000:
    classificacao = 'Prata'
elif quant_xp > 5001 and quant_xp < 7000:
    classificacao = 'Ouro'
elif quant_xp > 7001 and quant_xp < 8000:
    classificacao = 'Platina'
elif quant_xp > 8001 and quant_xp < 9000:
    classificacao = 'Ascendente'
elif quant_xp > 9001 and quant_xp < 10000:
    classificacao = 'Imortal'
elif quant_xp >= 10000:
    classificacao = 'Radiante'

print(f'O Herói de nome {nome} está no nível de {classificacao}')