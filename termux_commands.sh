#!/bin/bash

# Termux Command Info
# Autor: Dentinho
# Versão: 1.1
# Descrição: Um menu interativo para mostrar comandos úteis no Termux e Node.js.

# Definir cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # Sem cor

# Função para mostrar o menu principal
show_main_menu() {
  clear
  echo -e "${CYAN}╔═══════════════════════════════════════════════════════╗${NC}"
  echo -e "${CYAN}║             ${BLUE}Termux Command Info${CYAN}                      ║${NC}"
  echo -e "${CYAN}║                   ${YELLOW}por Dentinho${CYAN}                        ║${NC}"
  echo -e "${CYAN}╠═══════════════════════════════════════════════════════╣${NC}"
  echo -e "${CYAN}║${NC} ${GREEN}1)${NC} ${YELLOW}Comandos Termux${NC}                               ${CYAN}║${NC}"
  echo -e "${CYAN}║${NC} ${GREEN}2)${NC} ${YELLOW}Comandos Node.js${NC}                             ${CYAN}║${NC}"
  echo -e "${CYAN}║${NC} ${GREEN}3)${NC} ${YELLOW}Sair${NC}                                        ${CYAN}║${NC}"
  echo -e "${CYAN}╚═══════════════════════════════════════════════════════╝${NC}"
  echo -e "${GREEN}Escolha uma opção (1-3):${NC} "
}

# Função para mostrar comandos Termux
show_termux_commands() {
  clear
  echo -e "${CYAN}╔═══════════════════════════════════════════════╗${NC}"
  echo -e "${CYAN}║         ${BLUE}Comandos Termux${CYAN}                       ║${NC}"
  echo -e "${CYAN}╠═══════════════════════════════════════════════╣${NC}"
  echo -e "${GREEN}1)${NC} pkg update      # Atualiza a lista de pacotes"
  echo -e "${GREEN}2)${NC} pkg upgrade     # Atualiza os pacotes instalados"
  echo -e "${GREEN}3)${NC} pkg install <package_name> # Instala um pacote"
  echo -e "${GREEN}4)${NC} pkg search <package_name>  # Busca um pacote"
  echo -e "${GREEN}5)${NC} df -h          # Verifica espaço em disco"
  echo -e "${GREEN}6)${NC} ls -la         # Lista arquivos e diretórios"
  echo -e "${GREEN}7)${NC} cd <directory> # Muda para o diretório especificado"
  echo -e "${GREEN}8)${NC} mkdir <name>   # Cria um novo diretório"
  echo -e "${GREEN}9)${NC} rm -rf <name>  # Remove arquivos ou diretórios"
  echo -e "${GREEN}10)${NC} touch <file>   # Cria um novo arquivo"
  echo -e "${CYAN}╚═══════════════════════════════════════════════╝${NC}"
  echo -e "${YELLOW}Pressione qualquer tecla para voltar...${NC}"
  read -n 1 -s
}

# Função para mostrar comandos Node.js
show_nodejs_commands() {
  clear
  echo -e "${CYAN}╔═══════════════════════════════════════════════╗${NC}"
  echo -e "${CYAN}║         ${BLUE}Comandos Node.js${CYAN}                        ║${NC}"
  echo -e "${CYAN}╠═══════════════════════════════════════════════╣${NC}"
  echo -e "${GREEN}1)${NC} node .          # Inicia o bot"
  echo -e "${GREEN}2)${NC} npm install      # Instala dependências do projeto"
  echo -e "${GREEN}3)${NC} npm start        # Inicia o script definido em package.json"
  echo -e "${GREEN}4)${NC} npm run <script> # Executa um script definido em package.json"
  echo -e "${GREEN}5)${NC} npm update       # Atualiza dependências para a última versão"
  echo -e "${GREEN}6)${NC} npm uninstall <package_name> # Remove um pacote"
  echo -e "${GREEN}7)${NC} npm list        # Lista todas as dependências instaladas"
  echo -e "${GREEN}8)${NC} node -v         # Verifica a versão do Node.js instalada"
  echo -e "${GREEN}9)${NC} npm -v          # Verifica a versão do npm instalada"
  echo -e "${CYAN}╚═══════════════════════════════════════════════╝${NC}"
  echo -e "${YELLOW}Pressione qualquer tecla para voltar...${NC}"
  read -n 1 -s
}

# Loop principal do menu
while true; do
  show_main_menu
  read -p "Selecione uma opção (1-3): " choice

  case $choice in
    1)
      show_termux_commands
      ;;
    2)
      show_nodejs_commands
      ;;
    3)
      echo -e "${RED}Saindo do menu...${NC}"
      exit 0
      ;;
    *)
      echo -e "${RED}Opção inválida! Tente novamente.${NC}"
      sleep 2
      ;;
  esac
done
