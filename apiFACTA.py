import requests
import base64


homologacao = "https://webservice-homol.facta.com.br/"
producao = "https://webservice.facta.com.br/"

token_endpoint = "gera-token"

usuario     = "92504"
senha_velha = "87qx0s0qaye1jos1me9c"
senha       = "Novaprom12*"
financeira  = "92504_01623409071"

credentials1 = f"{usuario}:{senha}"

encoded_credentials = base64.b64encode(credentials1.encode()).decode()
print(encoded_credentials)

url = homologacao + token_endpoint
print(url)

headers = {
    "Authorization": f"Basic {encoded_credentials}"
}

# url = f"{homologacao}{token_endpoint}"  # Usar o ambiente de homologação
options = {
    "url": url,
    "headers": headers,
    "timeout": 10,
    "allow_redirects": True,
    "verify": True,  # Verificar certificado SSL (defina como False para ignorar)
    "cookies": {"session_id": "seu_valor_de_sessao"}
}

# response = requests.get(url, headers=headers)
response = requests.get(**options)

if response.status_code == 200:
    data = response.json()
    if not data.get("erro"):
        token = data.get("token")
        print("Token gerado com sucesso:", token)
    else:
        print("Erro ao gerar token:", data.get("mensagem"))
else:
    print("Erro na requisição:", response.status_code, response.text)
