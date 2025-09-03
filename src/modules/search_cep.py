from requests import get # Importa a função get da biblioteca requests

# Define a função searchCep que recebe um CEP como argumento
def search_cep(cep:int)->dict:
    """
    Function to make a request to cep api and return.
    
    Args:
        cep(int): The cep to search
        
    Return:
        dict: The details of the cep.
        
    Raises:
        ValueError: When have an error in format.
        Exception: When have other error type.
"""
    try:
        # Verifica se o cep é um valor vazio
        if cep:
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
        else:
            # Levanta um erro se o input estiver vazio.
            raise ValueError("O Cep não pode ser vazio!")
    
    except ValueError as v:
        # Captura e retorna a mensagem de erro
        return str(v) 

    except Exception as e:
        # Captura e retorna qualquer outro tipo de erro
        return f"Error {e}"
