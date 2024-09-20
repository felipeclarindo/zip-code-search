from customtkinter import CTk, CTkLabel, CTkButton

class CepGUI(CTk):
    """
    Classe principal da aplicação para busca de CEP.
    Herda a classe CTk para criar uma interface gráfica personalizada.
    """
    
    def __init__(self, informacoes_cep: dict) -> None:
        """
        Inicializa a interface gráfica, configura e define widgets da aplicação.

        Args:
            informacoes_cep (dict): Um dicionário contendo informações sobre o CEP.
                Espera-se que as chaves e valores incluam:
                - 'cep': O CEP associado.
                - 'logradouro': O logradouro associado ao CEP.
                - 'bairro': O bairro associado ao CEP.
                - 'cidade': A cidade correspondente ao CEP.
                - 'estado': O estado correspondente ao CEP.
                - 'ddd': O DDD associado ao número.

        Raises:
            ValueError: Se as informações do CEP não estiverem completas.
        """
        super().__init__()
        self.informacoes_cep = informacoes_cep
        self.configure_screen()
        self.create_widgets()

    def configure_screen(self) -> None:
        """
        Configura a tela da aplicação, definindo título, tamanho, 
        redimensionamento e tema de cores.
        """
        self.title("Informações do Cep")
        self.geometry("300x300")
        self.resizable(False, False)
        self._set_appearance_mode("dark")
        
    def create_widgets(self) -> None:
        """
        Cria e organiza os widgets da interface gráfica,
        incluindo labels e um botão de fechar.
        """
        # Usando a cor de fundo da janela para os labels
        self.bg_color = self.cget("bg")

        title_label = CTkLabel(self, text="Informações do Cep", font=("Arial", 17), bg_color=self.cget("bg"), text_color="white")
        title_label.pack(pady=15)

        cep_label = CTkLabel(self, text=f"CEP: {self.informacoes_cep.get('cep')}", bg_color=self.cget("bg"), text_color="white")
        cep_label.pack()

        rua_label = CTkLabel(self, text=f"Rua: {self.informacoes_cep.get('rua')}", bg_color=self.cget("bg"), text_color="white")
        rua_label.pack()

        bairro_label = CTkLabel(self, text=f"Bairro: {self.informacoes_cep.get('bairro')}", bg_color=self.cget("bg"), text_color="white")
        bairro_label.pack()

        cidade_label = CTkLabel(self, text=f"Cidade: {self.informacoes_cep.get('cidade')}", bg_color=self.cget("bg"), text_color="white")
        cidade_label.pack()

        ddd_label = CTkLabel(self, text=f"DDD: {self.informacoes_cep.get('ddd')}", bg_color=self.cget("bg"), text_color="white")
        ddd_label.pack()

        close_button = CTkButton(self, text="Fechar", command=self.destroy, bg_color=self.cget("bg"))
        close_button.pack(pady=20)
