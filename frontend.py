import customtkinter as ctk   # biblioteca para visual moderno
import tkinter as tk          # (neste caso) adaptar recursos para janela popup
import ctypes                 # acesso aos recursos do sistema operacional
import sys                    # acesso à variáveis do sistema
import os                     # acesso aos diretórios

ctk.set_appearance_mode("dark")  # definindo aparência

class GerenciadorIcone():
    @staticmethod
    def resource_path(relative_path):
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)

    ICON_ICO = resource_path.__func__(os.path.join("assets", "list.ico"))
    ICON_PNG = resource_path.__func__(os.path.join("assets", "list.png"))

    @staticmethod
    def apply_icon(window):
        # Tenta aplicar .ico, se falhar tenta .png
        if os.path.exists(GerenciadorIcone.ICON_ICO):
            try:
                window.iconbitmap(GerenciadorIcone.ICON_ICO)
                return
            except Exception as e:
                print("Falha ao aplicar .ico:", e)

        if os.path.exists(GerenciadorIcone.ICON_PNG):
            try:
                img = ctk.PhotoImage(file=GerenciadorIcone.ICON_PNG)
                window._icon_photoimage = img
                window.iconphoto(False, img)
            except Exception as e:
                print("Falha ao aplicar .png:", e)

class Popup(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

        # Configuração básica da janela popup:
        self.title("Sobre o app")
        self.attributes("-topmost", True)
        self.configure(bg="#2C2C2C")

        # Ativa barra de título escura (Windows):
        if sys.platform.startswith("win"):
            self.after(10, self.ativar_dark_titlebar)

        # Configuração para bloquear interface:
        self.transient(master)
        self.grab_set()
        self.focus_force()

        self.protocol("WM_DELETE_WINDOW", self.fecha_popup)  # devolve domínio para janela principal

        # Configuração de tamanho:
        popup_width, popup_height = 350, 180

        tela_width = self.winfo_screenwidth()
        tela_height = self.winfo_screenheight()
        x = (tela_width // 2) - (popup_width // 2)
        y = (tela_height // 2) - (popup_height // 2)

        self.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
        self.resizable(False, False)

        # Inserir ícone na barra de título:
        GerenciadorIcone.apply_icon(self)

        # Remove minimizar/maximizar (Windows)
        if sys.platform.startswith("win"):
            GWL_STYLE = -16
            WS_MINIMIZEBOX = 0x00020000
            WS_MAXIMIZEBOX = 0x00010000
            hwnd = ctypes.windll.user32.GetParent(self.winfo_id())
            style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)
            style &= ~WS_MINIMIZEBOX
            style &= ~WS_MAXIMIZEBOX
            ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style)
            ctypes.windll.user32.SetWindowPos(
                hwnd, 0, 0, 0, 0, 0,
                0x0002 | 0x0001 | 0x0040 | 0x0020
            )

        # Conteúdo da janela:
        info = (
            "CRUD de funcionamento básico\n\n"
            "Interface: Biblioteca CustomTkinter\n"
            "Arquivos: Este app usa arquivos .py e .txt\n"
            "Desenvolvedor: Danilo dos Santos Soares\n"
            "Contato: (11) 9 4138-3504\n\n"
            "© 2026 - Todos os direitos reservados."
        )

        label_info = ctk.CTkLabel(
            master=self,
            text=info,
            justify="left",
            text_color="#FFFFFF",
            font=ctk.CTkFont(size=14)
        )
        label_info.pack(padx=20, pady=20)

    # Função para alterar barra de título:
    def ativar_dark_titlebar(self):
        self.update()
        hwnd = ctypes.windll.user32.GetParent(self.winfo_id())

        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        valor = ctypes.c_int(1)

        ctypes.windll.dwmapi.DwmSetWindowAttribute(
            hwnd,
            DWMWA_USE_IMMERSIVE_DARK_MODE,
            ctypes.byref(valor),
            ctypes.sizeof(valor)
        )

    def fecha_popup(self):
        self.grab_release()
        self.destroy()

class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("700x450")
        self.title("CRUD BÁSICO")
        self.resizable(True, True)

        # Inserindo ícone:
        GerenciadorIcone.apply_icon(self)
        self._icon_photoimage = None

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
        self.info_sobre.bind("<Button-1>", lambda e: Popup(self))  # abre janela popup
        

if __name__ == "__main__":
    app = Interface()
    app.mainloop()