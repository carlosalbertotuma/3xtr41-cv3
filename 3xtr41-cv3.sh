#!/bin/bash

banner()
{
echo -e "\e[1;32m
                                             
###      #      # #  #              ### 
  # # # ### ### # # ##      ### # #   # 
 ##  #   #  #   ###  #  ### #   # #  ## 
  # # #  ## #     #  #      ###  #    # 
###               # ###             ### 

   _   _     _   _   _   _   _   _   _   _     _     _   _   _   _   _   
  / \ / \   / \ / \ / \ / \ / \ / \ / \ / \   / \   / \ / \ / \ / \ / \  
 ( B | y ) ( B | l | 4 | d | s | c | 4 | n ) ( - ) ( V | . | 0 | . | 1 ) 
  \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/   \_/ \_/ \_/ \_/ \_/  \e[0m"

}
banner
echo ""
URL="https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=$1&keywordExactMatch"

response=$(curl -s "$URL")

if [ $? -ne 0 ]; then
  echo "Erro ao fazer a requisição HTTP."
  exit 1
fi

# Verifique se 'jq' está instalado
if ! command -v jq &> /dev/null; then
  echo "'jq' não está instalado. Por favor, instale 'jq' para continuar."
  exit 1
fi

# Processar o JSON retornado para extrair os CVEs
echo "$response" | jq -r '.vulnerabilities[].cve | "\(.id): \(.descriptions[0].value)"'
