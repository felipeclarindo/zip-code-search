import requests

def searchCode(cep):
    request = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}").json()

    if "message" in request:
        return "Cep invalido!"
    else:
        
        info_cep = {
            "Cep": request['cep'],
            request['address_type']: request['address_name'] ,
            "Bairro": request['district'],
            "Cidade": request['city'],
            "Ddd": request['ddd']
        }
        return info_cep

