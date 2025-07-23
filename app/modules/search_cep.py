from requests import get


def search_cep(cep: int) -> dict:
    """
    Searches for the information of a given CEP (Postal Code) using an external API.

    Args:
        cep (int): The CEP to be searched. Must have exactly 8 numeric digits.

    Returns:
        dict: A dictionary with the information of the CEP, including the fields:
            - "Cep": The formatted CEP.
            - Address type (e.g., "Rua" or "Avenida"): The name of the street or avenue.
            - "Bairro": The neighborhood associated with the CEP.
            - "Cidade": The city corresponding to the CEP.
            - "DDD": The DDD associated with the number.

    Raises:
        ValueError: If the CEP does not have 8 numeric digits or is empty.
        Exception: For other errors during the API request.

    If an error occurs, the function returns a string with the error message.
    """
    try:
        if cep:
            if len(cep) == 8 and cep.isdigit():
                url = f"https://cep.awesomeapi.com.br/json/{cep}"

                request = get(url, verify=False).json()

                # Extracting relevant information from the API response
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
                    "Cep Invalido,\ninforme um cep com 8 digitos numéricos!"
                )
        else:
            raise ValueError("O cep não pode ser vazio!")

    except ValueError as v:
        return str(v)

    except Exception as e:
        return f"Error {e}"
