from customtkinter import CTk, CTkLabel, CTkButton


class CepGUI(CTk):
    """
    Class for displaying CEP information in a GUI.
    """

    def __init__(self, informacoes_cep: dict) -> None:
        """
        Initializes the graphical interface, configures and defines the application widgets.

        Args:
            informacoes_cep (dict): A dictionary containing information about the CEP.
            Expects keys and values to include:
            - 'cep': The associated CEP.
            - 'rua': The street associated with the CEP.
            - 'bairro': The neighborhood associated with the CEP.
            - 'cidade': The city corresponding to the CEP.
            - 'ddd': The DDD associated with the number.
        Raises:
            ValueError: If the CEP information is incomplete.

        Raises:
            ValueError: Se as informações do CEP não estiverem completas.
        """
        super().__init__()
        self.informacoes_cep = informacoes_cep
        self.configure_screen()
        self.create_widgets()

    def configure_screen(self) -> None:
        """
        Configures the application screen, setting the title, size, and appearance mode.
        """
        self.title("Informações do Cep")
        self.geometry("300x300")
        self.resizable(False, False)
        self._set_appearance_mode("dark")

    def create_widgets(self) -> None:
        """
        Creates and organizes the widgets of the graphical interface,
        including labels and a close button.
        """
        self.bg_color = self.cget("bg")

        title_label = CTkLabel(
            self,
            text="Informações do Cep",
            font=("Arial", 17),
            bg_color=self.cget("bg"),
            text_color="white",
        )
        title_label.pack(pady=15)

        cep_label = CTkLabel(
            self,
            text=f"CEP: {self.informacoes_cep.get('cep')}",
            bg_color=self.cget("bg"),
            text_color="white",
        )
        cep_label.pack()

        rua_label = CTkLabel(
            self,
            text=f"Rua: {self.informacoes_cep.get('rua')}",
            bg_color=self.cget("bg"),
            text_color="white",
        )
        rua_label.pack()

        bairro_label = CTkLabel(
            self,
            text=f"Bairro: {self.informacoes_cep.get('bairro')}",
            bg_color=self.cget("bg"),
            text_color="white",
        )
        bairro_label.pack()

        cidade_label = CTkLabel(
            self,
            text=f"Cidade: {self.informacoes_cep.get('cidade')}",
            bg_color=self.cget("bg"),
            text_color="white",
        )
        cidade_label.pack()

        ddd_label = CTkLabel(
            self,
            text=f"DDD: {self.informacoes_cep.get('ddd')}",
            bg_color=self.cget("bg"),
            text_color="white",
        )
        ddd_label.pack()

        close_button = CTkButton(
            self, text="Fechar", command=self.destroy, bg_color=self.cget("bg")
        )
        close_button.pack(pady=20)
