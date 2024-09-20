# - Imports -
import os  # Usado para obter o tamanho da tela e limpar o console
from time import sleep  # Usado para a função de pausa (sleep)
import json  # Usado para formatar as respostas das requisições em JSON
from requests import get, post  # Usado para fazer as requisições HTTP
import platform
import base64
import re

# - Variáveis reutilizáveis -
options = [
    "localizar IP",
    "localizar DDD",
    "Consultar CNPJ",
    "localizar CEP",
    "Consulta WhoIS",
    "Verificar Telefone",
    "Consultar CPF"
]
_options = [0, 1, 2, 3, 4, 5, 6, 99]

R="\033[1;31m"; G="\033[1;32m"; B="\033[1;34m"; Y="\033[1;33m"; r="\033[0m"; n="\033[1m"
C='\033[1;37m'

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# ☇ "[+]" colorido
start = f"{n}[{B}+{r}{n}] "

# Função para limpar a tela
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    else:
        os.system("clear")

# ☇ Adicionar a opção de consulta de CPF ao menu
class metodos:
    def whois():
        domain = input(f"{start}{B}Digite o domínio que deseja consultar: {r}")
        cls()
        headers = {"apikey": "2nY2gxtScwH6mPVmOSYstS8oVmF4ltbb"}
        rsp = get(url=f"https://api.apilayer.com/whois/query?domain={domain}", headers=headers)
        rspj = rsp.json()
        match rsp.status_code:
            case 200:
                metodos.ndict(rspj)
                print(f"{start}{Y}Peço desculpas por não traduzir as respostas. Veja mais em: https://github.com/kvgnx54/ghostpanel{r}")
                input(f"\n{start}{B}Aperte Enter para voltar.{r}")
            case _:
                print(f"{n}[{R}!{r}{n}] {R}{rspj['message']}{r}")
                print(f"{start}Se o site começa com https:// remova essa parte.{r}")
                input(f"\n{start}{B}Aperte Enter para voltar.{r}")

    def cep():
        _cep = input(f"{start}{B}Digite o CEP que deseja localizar: {r}")
        cls()
        cep = ''.join(filter(str.isnumeric, _cep))
        if cep == "":
            input(f"\n{start}{B}Aperte Enter para voltar.{r}")
        else:
            rsp = get(f"https://cep.awesomeapi.com.br/{cep}")
            rspj = rsp.json()
            match rsp.status_code:
                case 200:
                    print(f"{start}CEP: {rspj['cep']}{r}")
                    print(f"{start}Endereço: {rspj['address']}{r}")
                    print(f"{start}Estado: {rspj['state']}{r}")
                    print(f"{start}Cidade: {rspj['city']}{r}")
                    print(f"{start}DDD: {rspj['ddd']}{r}")
                    input(f"\n{start}{B}Aperte Enter para voltar.{r}")
                case _:
                    print(f"{n}[{R}!{r}{n}] {R}{rspj['message']}{r}")
                    input(f"\n{start}{B}Aperte Enter para voltar.{r}")

    def consultar_cpf():
        a='aHR0cDovL3d3dy5qdXZlbnR1ZGV3ZWIubXRlLmdvdi5ici9wbnBlcGVzcXVpc2FzLmFzcA=='
        a=base64.b64decode(a.encode('ascii')).decode('ascii')

        cpf = input(f"{start}{B}Informe o CPF a ser consultado (sem pontos ou traços): {r}")
        cls()
        try:
            h = {
                'Content-Type': "text/xml, application/x-www-form-urlencoded;charset=ISO-8859-1, text/xml; charset=ISO-8859-1",
                'Cookie': "ASPSESSIONIDSCCRRTSA=NGOIJMMDEIMAPDACNIEDFBID; FGTServer=2A56DE837DA99704910F47A454B42D1A8CCF150E0874FDE491A399A5EF5657BC0CF03A1EEB1C685B4C118A83F971F6198A78",
                'Host': "www.juventudeweb.mte.gov.br"
            }
            r = post(a, headers=h, data=f'acao=consultar%20cpf&cpf={cpf}&nocache=0.7636039437638835').text

            print(f'''
{C}CPF: {B}{re.search('NRCPF="(.*?)"', r).group(1)}
{C}Nome: {B}{re.search('NOPESSOAFISICA="(.*?)"', r).group(1).title()}
{C}Nascimento: {B}{re.search('DTNASCIMENTO="(.*?)"', r).group(1)}
{C}Nome da Mãe: {B}{re.search('NOMAE="(.*?)"', r).group(1).title()}
{C}Endereço: {B}{re.search('NOLOGRADOURO="(.*?)"', r).group(1).title()}, {re.search('NRLOGRADOURO="(.*?)"', r).group(1)}
{C}Bairro: {B}{re.search('NOBAIRRO="(.*?)"', r).group(1).title()}
{C}Cidade: {B}{re.search('NOMUNICIPIO="(.*?)"', r).group(1).title()}-{re.search('SGUF="(.*?)"', r).group(1)}
{C}CEP: {B}{re.search('NRCEP="(.*?)"', r).group(1)}
''')
            input(f"{start}{B}Aperte Enter para voltar.{r}")
        except AttributeError:
            print(f"{R}CPF inexistente{r}")
            input(f"\n{start}{B}Aperte Enter para voltar.{r}")

# Função principal para exibir o menu
def menu():
    while True:
        cls()
        print(f"{start}{B}Menu de Consultas{r}")
        print(f"{n}0. Localizar IP")
        print(f"1. Localizar DDD")
        print(f"2. Consultar CNPJ")
        print(f"3. Localizar CEP")
        print(f"4. Consulta WhoIS")
        print(f"5. Verificar Telefone")
        print(f"6. Consultar CPF")
        print(f"99. Sair")
        choice = int(input(f"{start}{B}Escolha uma opção: {r}"))
        cls()

        if choice == 0:
            metodos.localizar_ip()
        elif choice == 1:
            metodos.localizar_ddd()
        elif choice == 2:
            metodos.consultar_cnpj()
        elif choice == 3:
            metodos.cep()
        elif choice == 4:
            metodos.whois()
        elif choice == 5:
            metodos.verificar_telefone()
        elif choice == 6:
            metodos.consultar_cpf()
        elif choice == 99:
            break
        else:
            print(f"{start}{R}Opção inválida!{r}")
            sleep(2)

menu()
