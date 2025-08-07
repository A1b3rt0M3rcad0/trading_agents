#!/bin/bash

# Script para exportar variáveis do arquivo .env para o terminal
# Uso: source export_env.sh

# Verificar se o arquivo .env existe
if [ ! -f .env ]; then
    echo "Erro: Arquivo .env não encontrado!"
    echo "Crie um arquivo .env na raiz do projeto com suas variáveis de ambiente."
    exit 1
fi

# Ler o arquivo .env e exportar cada variável
echo "Exportando variáveis do arquivo .env..."

while IFS= read -r line; do
    # Pular linhas vazias e comentários
    if [[ -n "$line" && ! "$line" =~ ^[[:space:]]*# ]]; then
        # Verificar se a linha contém um sinal de igual
        if [[ "$line" =~ = ]]; then
            # Exportar a variável
            export "$line"
            echo "Exportado: ${line%%=*}"
        fi
    fi
done < .env

echo "Todas as variáveis do .env foram exportadas para o terminal!"
echo ""
echo "Para verificar as variáveis exportadas, use:"
echo "  env | grep -E '^(DEEPSEEK|X)'"
echo ""
echo "Para usar este script em outras sessões, execute:"
echo "  source export_env.sh" 