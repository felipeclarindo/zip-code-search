# Importa a função get da biblioteca requests
from requests import get

# Define a função searchCep que recebe um CEP como argumento
def searchCep(cep:int)->dict:
    try:
        # Verifica se o CEP tem 8 dígitos e contém apenas números
        if len(cep) == 8 and cep.isdigit():
            # Monta a URL com o CEP fornecido
            url = f"https://cep.awesomeapi.com.br/json/{cep}"

            # Faz a requisição GET para a API de CEP e converte a resposta para JSON
            request = get(url).json()

            # Extrai as informações relevantes da resposta da API
            info_cep = {
                "Cep": request['cep'],
                request['address_type']: request['address_name'],
                "Bairro": request['district'],
                "Cidade": request['city'],
                "DDD": request['ddd']
            }
        
            return info_cep

        else:
            # Levanta um erro se o CEP não tiver 8 dígitos ou não contiver apenas números
            raise ValueError("Cep Invalido. \nDigite um CEP com 8 digitos numéricos!")
    
    except ValueError as ve:
        # Captura e retorna a mensagem de erro
        return str(ve) 

    except Exception as e:
        # Captura e retorna qualquer outro tipo de erro
        return f"Error {e}"
    

# Verifica se o script está sendo executado diretamente
if __name__ == "__main__":
    pass  # Não faz nada neste caso, apenas define a estrutura do script
