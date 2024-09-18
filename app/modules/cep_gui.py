from customtkinter import CTk, CTkLabel, CTkButton


class CepGUI(CTk):
    def __init__(self, informacoes_cep) -> None:
        super(CepGUI, self).__init__()
        self.informacoes_cep = informacoes_cep
        self.configure_screen()
        self.create_widgets()

    def configure_screen(self) -> None:
        self.geometry("300x300")
        self.resizable(False, False)
        self._set_appearance_mode("dark")

    def create_widgets(self) -> None:
        self.label_title = CTkLabel(self, width=200, height=30, text="Informações")
        self.label_title.pack()

        self.text_error = CTkLabel(self, text="")
        self.text_error.pack()

        self.text_cep = CTkLabel(self, text="")
        self.text_cep.pack()

        self.text_rua = CTkLabel(self, text="")
        self.text_rua.pack()

        self.text_bairro = CTkLabel(self, text="")
        self.text_bairro.pack()

        self.text_cidade = CTkLabel(self, text="")
        self.text_cidade.pack()

        self.text_ddd = CTkLabel(self, text="")
        self.text_ddd.pack()

        self.button_close = CTkButton(self, width=80, height=40, text="Close")
        self.button_close.pack()
