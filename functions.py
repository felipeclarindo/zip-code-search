from requests import get

def searchCep(cep):

    try:
        request = get(f"https://cep.awesomeapi.com.br/json/{cep}").json()

        print(request)

        info_cep = {
            "Cep": request['cep'],
            request['address_type']: request['address_name'] ,
            "Bairro": request['district'],
            "Cidade": request['city'],
            "DDD": request['ddd']
        }
        return info_cep
   
    except:
        return "Cep ínvalido!"
    
if __name__ == "__main__":
    pass
    
