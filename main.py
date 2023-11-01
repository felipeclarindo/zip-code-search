from tkinter import *
from customtkinter import *
from functions import searchCep

def print_cep():

    cep = searchCep(cep_input.get())
    if cep == "Cep invalido!":
        text['text'] = cep

    else:
        
        text['text'] = "Informações"

        text_cep['text'] = "Cep: {}".format(cep["Cep"])

        text_rua['text'] = "Rua: {}".format(cep["Rua"])

        text_bairro['text'] = "Bairro: {}".format(cep["Bairro"])

        text_cidade['text'] = "Cidade: {}".format(cep["Cidade"])

        text_ddd['text'] = "DDD: {}".format(cep["DDD"])

    
def clear():
    text['text'] = ""

    text_cep['text'] = ""
    text_rua['text'] = ""
    text_bairro['text'] = ""
    text_cidade['text'] = ""
    text_ddd['text'] = ""

tela = CTk()
tela.geometry("400x350")
tela.title("Buscar Cep")

text_orientation = CTkLabel(tela, text = "Buscar Cep")
text_orientation.pack(padx = 10, pady = 5)

cep_input = CTkEntry(tela)
cep_input.pack(padx = 10, pady = 5)

button_search_cep = CTkButton(tela, text = "Search", command= print_cep)
button_search_cep.pack(padx = 10, pady = 10)

button_clear = CTkButton(tela, text = "Clear", command=clear)
button_clear.pack()

text = Label(tela, text = "", fg = "white")
text.pack(pady = 20)

text['bg'] = tela['background']

text_cep = Label(tela, text = "", fg = "white")
text_cep.pack()

text_cep["bg"] = tela["background"]

text_rua = Label(tela, text = "", fg = "white")
text_rua.pack()

text_rua["bg"] = tela["background"]

text_bairro = Label(tela, text = "", fg = "white")
text_bairro.pack()

text_bairro["bg"] = tela["background"]

text_cidade = Label(tela, text = "", fg = "white")
text_cidade.pack()

text_cidade["bg"] = tela["background"]

text_ddd = Label(tela, text = "", fg = "white")
text_ddd.pack(padx = 50)

text_ddd["bg"] = tela["background"]

tela.mainloop()