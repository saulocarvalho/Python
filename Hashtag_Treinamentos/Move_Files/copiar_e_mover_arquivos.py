import os

#Lista diretório
#arquivos = os.listdir()
#print(arquivos)

#caminho da pasta onde está sendo trabalhado
#caminho = os.getcwd()
#print(caminho)

#Renomear arquivos
# Apenas renomeia o arquivo 
#os.rename('Vendas 1.xlsx','Vendas - 1.xlsx')
# Renomeia e muda o local
#os.rename('Vendas - 1.xlsx', 'vendas\Vendas - 1.xlsx')

#copiar arquivos
import shutil

#shutil.copy2('Vendas - 1.xlsx', 'vendas\Vendas - 1.xlsx')

lista_arquivos = os.listdir()

for arquivo in lista_arquivos:
    if 'xlsx' in arquivo:
        if 'Compras' in arquivo:
            os.rename(arquivo, f'Compras\{arquivo}')
        elif 'Vendas' in arquivo: 
            os.rename(arquivo, f'Vendas\{arquivo}')
