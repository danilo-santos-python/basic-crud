import customtkinter as ctk

ctk.set_appearance_mode("dark")


class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("700x450")
        self.title("CRUD BÁSICO v1")
        self.resizable(True, True)

        # Contruindo o frame principal:
        self.frame_principal = ctk.CTkFrame(master=self)
        self.frame_principal.place(
            relx=0.5,
            rely=0.5,
            anchor=ctk.CENTER,
            relwidth=0.94,
            relheight=0.94
        )

        # Construindo a grid horizontal:
        self.frame_principal.grid_columnconfigure(0, weight=1)  # espaço esquerdo
        self.frame_principal.grid_columnconfigure(1, weight=3)  # conteúdo
        self.frame_principal.grid_columnconfigure(2, weight=1)  # botões

        # Configurando expansão vertical da área de texto:
        self.frame_principal.grid_rowconfigure(2, weight=1)

        # Título:
        self.titulo = ctk.CTkLabel(
            master=self.frame_principal,
            text="Gravação de Dados:",
            text_color="#FFFFFF",
            font=ctk.CTkFont(size=25, weight="bold")
        )
        self.titulo.grid(row=0, column=1, pady=(20, 0), sticky="n")  # colado no topo

        # Entrada de dados:
        self.entrada_dados = ctk.CTkEntry(
            master=self.frame_principal,
            height=28,
            placeholder_text="Entre com os dados aqui...",
            text_color="#000000",
            fg_color="#FFFFFF"
        )
        self.entrada_dados.grid(row=1, column=1, padx=10, pady=(18, 0), sticky="ew")  # expande horizontalmente

        # Área para visualizar dados:
        self.area_dados = ctk.CTkTextbox(
            master=self.frame_principal,
            border_color="#575151",
            border_width=2
        )
        self.area_dados.grid(row=2, column=1, padx=10, pady=(18, 20), sticky="nsew")  # todas as direções

        # Criando um frame lateral para os botões:
        self.frame_botoes = ctk.CTkFrame(
            master=self.frame_principal,
            fg_color="transparent"
        )
        self.frame_botoes.grid(row=1, column=2, rowspan=2, padx=(0, 40), pady=(15, 0), sticky="n")  # colado no topo

        # Configurando grid interna dos botões:
        self.frame_botoes.grid_columnconfigure(0, weight=1)  # expande horizontalmente dentro do frame

        # Criando botão 1:
        self.btn_1 = ctk.CTkButton(
            master=self.frame_botoes,
            text="Inserir",
            width=100,
            height=28
        )
        self.btn_1.grid(row=0, column=0, pady=5, sticky="ew")  # expande horizontalmente

        # Criando botão 2:
        self.btn_2 = ctk.CTkButton(
            master=self.frame_botoes,
            text="Ler/Carregar",
            width=100,
            height=28
        )
        self.btn_2.grid(row=1, column=0, pady=5, sticky="ew")  # expande horizontalmente

        # Criando botão 3:
        self.btn_3 = ctk.CTkButton(
            master=self.frame_botoes,
            text="Editar",
            width=100,
            height=28
        )
        self.btn_3.grid(row=2, column=0, pady=5, sticky="ew")  #  "            "

        # Criando botão 4:
        self.btn_4 = ctk.CTkButton(
            master=self.frame_botoes,
            text="Excluir",
            width=100,
            height=28
        )
        self.btn_4.grid(row=3, column=0, pady=5, sticky="ew")  #  "            "

        # Criando um frame para link:
        self.frame_link = ctk.CTkFrame(
            master=self.frame_principal,
            fg_color="transparent"
        )
        self.frame_link.grid(row=2, column=2, rowspan=2, sticky="se", padx=15, pady=5)

        # Configurando grid interna do frame do link:
        self.frame_link.grid_columnconfigure(0, weight=1)

        
        # Link para janela de informação
        self.info_sobre = ctk.CTkLabel(
            master=self.frame_link,
            text="Sobre",
            text_color="#999292",
            cursor="hand2",
            font=ctk.CTkFont(size=13)
        )
        self.info_sobre.grid(row=3, column=3, sticky="se", padx=15, pady=5)
        

if __name__ == "__main__":
    app = Interface()
    app.mainloop()