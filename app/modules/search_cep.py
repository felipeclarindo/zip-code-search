from requests import get


def search_cep(cep: int) -> dict:
    """
    Busca informações de endereço de um CEP usando a API AwesomeAPI.

    Args:
        cep (int): O CEP a ser buscado. Deve ter exatamente 8 dígitos numéricos.

    Returns:
        dict: Um dicionário com as informações do CEP, incluindo os campos:
            - "Cep": O CEP formatado.
            - Tipo de logradouro (ex: "Rua" ou "Avenida"): O nome da rua ou avenida.
            - "Bairro": O bairro correspondente ao CEP.
            - "Cidade": A cidade correspondente ao CEP.
            - "DDD": O código DDD da área do CEP.

    Raises:
        ValueError: Se o CEP não tiver 8 dígitos numéricos ou estiver vazio.
        Exception: Para outros erros durante a solicitação à API.

    Se ocorrer um erro, a função retorna uma string com a mensagem de erro.
    """
    try:
        if cep:
            if len(cep) == 8 and cep.isdigit():
                url = f"https://cep.awesomeapi.com.br/json/{cep}"

                request = get(url).json()

                # Extraindo as informações relevantes da resposta da API
                info_cep = {
                    "cep": request["cep"],
                    request["address_type"].lower(): request["address_name"],
                    "bairro": request["district"],
                    "cidade": request["city"],
                    "ddd": request["ddd"],
                }

                return info_cep

            else:
                raise ValueError(
                    "Cep Invalido. \nDigite um CEP com 8 digitos numéricos!"
                )
        else:
            raise ValueError("O Cep não pode ser vazio!")

    except ValueError as v:
        return str(v)

    except Exception as e:
        return f"Error {e}"
