from customtkinter import *
from functions import searchCep

def print_cep():

    clear()

    cep = searchCep(cep_input.get())
    try:
        
        text.configure(text =  "Informações", pady = 15)
        text_cep.configure(text =  "Cep: {}".format(cep["Cep"]))
        text_rua.configure(text =  "Rua: {}".format(cep["Rua"]))
        text_bairro.configure(text =  "Bairro: {}".format(cep["Bairro"]))
        text_cidade.configure(text =  "Cidade: {}".format(cep["Cidade"]))
        text_ddd.configure(text = "DDD: {}".format(cep["DDD"]))
    
    except:    
        text.configure(text = cep, pady = 20);
    
def clear():
    text.configure(text = "")
    text_cep.configure(text = "")
    text_rua.configure(text = "")
    text_bairro.configure(text = "")
    text_cidade.configure(text = "")
    text_ddd.configure(text = "")
    
tela = CTk()
tela.title("Buscar Cep")

tela.geometry("300x400")
tela.resizable(width=False, height=False)
tela._set_appearance_mode("dark")

text_orientation = CTkLabel(tela, text = "Buscar Cep")
text_orientation.pack(padx = 10, pady = 5)

cep_input = CTkEntry(tela)
cep_input.pack(padx = 10, pady = 5)

button_search_cep = CTkButton(tela, text = "Search", command= print_cep)
button_search_cep.pack(padx = 10, pady = 10)

button_clear = CTkButton(tela, text = "Clear", command=clear)
button_clear.pack()

text = CTkLabel(tela, text = "")
text.pack(pady = 15)

text_cep = CTkLabel(tela, text = "")
text_cep.pack()

text_rua = CTkLabel(tela, text = "")
text_rua.pack()

text_bairro = CTkLabel(tela, text = "")
text_bairro.pack()

text_cidade = CTkLabel(tela, text = "")
text_cidade.pack()

text_ddd = CTkLabel(tela, text = "")
text_ddd.pack(padx = 50)

tela.mainloop()