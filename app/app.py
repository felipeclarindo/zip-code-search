from customtkinter import CTk, CTkLabel, CTkButton, CTkEntry
from .modules.search_cep import (
    search_cep,
)
from time import sleep


class App(CTk):
    """
    Classe principal da aplicação para busca de CEP.
    Herda a classe CTk para criar uma interface gráfica personalizada.
    """

    def __init__(self) -> None:
        """
        Inicializa a interface gráfica e define os widgets da aplicação.
        """
        super(App, self).__init__()

        self.configure_screen()
        self.create_widgets()

    def configure_screen(self) -> None:
        """
        Configurações da interface gráfica (titulo, resoluçãoo e etc)
        """
        self.title("Buscar Cep")
        self.geometry("300x350")
        self.resizable(width=False, height=False)
        self._set_appearance_mode("dark")

    def create_widgets(self) -> None:
        """
        Cria e posiciona os widgets (elementos da interface) na janela.
        """
        self.text_orientation = CTkLabel(self, text="Buscar Cep")
        self.text_orientation.pack(padx=10, pady=5)

        self.cep_input = CTkEntry(self)
        self.cep_input.pack(padx=10, pady=5)

        self.button_search_cep = CTkButton(self, text="Search", command=self.print_cep)
        self.button_search_cep.pack(padx=10, pady=5)

        self.button_clear = CTkButton(self, text="Clear", command=self.clear)
        self.button_clear.pack(pady=5)

        self.loading = CTkLabel(self, text="")
        self.loading.pack()

    def print_cep(self) -> None:
        """
        Busca e exibe as informações do CEP inserido pelo usuário. Se o CEP for inválido,
        exibe uma mensagem de erro.
        """
        self.clear()

        # Exibe mensagem de carregamento durante a busca
        self.loading.configure(text="Carregando....")
        self.loading.place(x=115, y=165)
        self.update()

        sleep(1)

        cep_data = search_cep(self.cep_input.get())

        # Verifica se o resultado é um dicionário válido com as informações do CEP
        if isinstance(cep_data, dict):
            self.text_cep.configure(text=f"Cep: {cep_data['Cep']}")
            self.text_rua.configure(text=f"Rua: {cep_data['Rua']}")
            self.text_bairro.configure(text=f"Bairro: {cep_data['Bairro']}")
            self.text_cidade.configure(text=f"Cidade: {cep_data['Cidade']}")
            self.text_ddd.configure(text=f"DDD: {cep_data['DDD']}")

            self.text_error.place_forget()
            self.text_cep.pack()
            self.text_rua.pack()
            self.text_bairro.pack()
            self.text_cidade.pack()
            self.text_ddd.pack()
        else:
            self.text_error.configure(text=cep_data, pady=4)
            self.text_error.pack(pady=18)

        self.loading.place_forget()
        self.update()
