import sys
import requests
import json

def banner():
    print("""
    ###      #      # #  #              ### 
      # # # ### ### # # ##      ### # #   # 
     ##  #   #  #   ###  #  ### #   # #  ## 
      # # #  ## #     #  #      ###  #    # 
    ###               # ###             ### 

       _   _     _   _   _   _   _   _   _   _     _     _   _   _   _   _   
      / \ / \   / \ / \ / \ / \ / \ / \ / \ / \   / \   / \ / \ / \ / \ / \  
     ( B | y ) ( B | l | 4 | d | s | c | 4 | n ) ( - ) ( V | . | 0 | . | 1 ) 
      \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/   \_/ \_/ \_/ \_/ \_/  
    """)

def main():
    if len(sys.argv) < 2:
        print("Uso: python script.py <keywords>")
        sys.exit(1)

    keyword = " ".join(sys.argv[1:])
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={keyword}"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao fazer a requisição HTTP: {e}")
        sys.exit(1)

    try:
        data = response.json()
    except json.JSONDecodeError:
        print("Erro ao processar a resposta JSON.")
        sys.exit(1)

    vulnerabilities = data.get('vulnerabilities', [])
    if not vulnerabilities:
        print("Nenhuma vulnerabilidade encontrada.")
        sys.exit(0)

    # Extraindo e invertendo a ordem das CVEs
    cves = [
        f"{vuln['cve']['id']}: {vuln['cve']['descriptions'][0]['value']}"
        for vuln in vulnerabilities
    ]
    cves.reverse()

    # Exibindo os CVEs
    for cve in cves:
        print(f"{cve}\n")

if __name__ == "__main__":
    banner()
    main()
