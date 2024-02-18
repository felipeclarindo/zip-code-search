# Importa a função get da biblioteca requests
from requests import get

# Define a função searchCep que recebe um CEP como argumento
def searchCep(cep):
    try:
        # Faz uma requisição GET para a API de CEP com o CEP fornecido
        request = get(f"https://cep.awesomeapi.com.br/json/{cep}").json()
        
        # Extrai as informações relevantes da resposta da API
        info_cep = {
            "Cep": request['cep'],  # Obtém o CEP
            request['address_type']: request['address_name'],  # Obtém o tipo e nome do endereço (ex: Rua, Avenida)
            "Bairro": request['district'],  # Obtém o bairro
            "Cidade": request['city'],  # Obtém a cidade
            "DDD": request['ddd']  # Obtém o DDD da cidade
        }
        return info_cep  # Retorna as informações do CEP em um dicionário
    
    except:
        return "Cep ínvalido!"  # Retorna uma mensagem de erro se o CEP for inválido

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    pass  # Não faz nada neste caso, apenas define a estrutura do script
