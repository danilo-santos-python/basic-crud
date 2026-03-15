# Funções dos botões:

class InserirDado():  # inserir = btn_1
    @staticmethod
    def inserir(entrada_dados, area_dados):

        texto = entrada_dados.get().strip()  # captura e remove espaços extras

        if not texto:
            print("Nada inserido no campo.")
            return  # evita inserir vazio

        # Libera temporariamente para inserção:
        area_dados.configure(state="normal")

        area_dados.insert("end", texto + "\n")  # insere no final

        # Bloqueia novamente após inserir:
        area_dados.configure(state="disabled")

        # Limpa o campo de entrada:
        entrada_dados.delete(0, "end")

        print(f"Inserido: {texto}")

class SelecionarLinha():  # selecionar dado inserido
    @staticmethod
    def selecionar(event, area_dados):
        index = area_dados.index(f"@{event.x},{event.y}")
        linha = index.split(".")[0]

        area_dados.tag_remove("selecionado", "1.0", "end")

        inicio = f"{linha}.0"
        fim_visual = f"{linha}.0 lineend +1c"
        fim_texto = f"{linha}.0 lineend"

        texto_linha = area_dados.get(inicio, fim_texto)

        if not texto_linha.strip():
            return

        area_dados.tag_add("selecionado", inicio, fim_visual)
        area_dados.tag_config(
            "selecionado",
            background="#2258CC",  # marcação da seleção
            foreground="#FFFFFF"
        )

        print("Selecionado:", texto_linha)
        return texto_linha

    @staticmethod
    def limpar_selecao(area_dados):
        area_dados.tag_remove("selecionado", "1.0", "end")

class EditarDado(): # editar = btn_3
    @staticmethod
    def editar(area_dados, inicio, fim, novo_texto):

        if not novo_texto.strip():
            print("Novo valor vazio.")
            return

        # Habilita edição:
        area_dados.configure(state="normal")

        # Remove texto antigo:
        area_dados.delete(inicio, fim)

        # Insere novo texto:
        area_dados.insert(inicio, novo_texto + "\n")

        # Bloqueia novamente:
        area_dados.configure(state="disabled")

        # Remove seleção:
        area_dados.tag_remove("selecionado", "1.0", "end")

        print(f"Editado para: {novo_texto}")

class ExcluirDado():  # excluir = btn_4
    @staticmethod
    def excluir(area_dados):

        ranges = area_dados.tag_ranges("selecionado")

        if not ranges:
            print("Nenhuma linha selecionada.")
            return

        inicio = ranges[0]
        linha = str(inicio).split(".")[0]

        inicio_linha = f"{linha}.0"
        fim_texto = f"{linha}.0 lineend"
        fim_linha = f"{linha}.0 lineend +1c"

        # Captura o texto antes de excluir:
        texto_excluido = area_dados.get(inicio_linha, fim_texto).strip()

        # Habilita temporariamente:
        area_dados.configure(state="normal")

        # Remove a linha inteira:
        area_dados.delete(inicio_linha, fim_linha)

        # Remove tag:
        area_dados.tag_remove("selecionado", "1.0", "end")

        # Desabilita novamente:
        area_dados.configure(state="disabled")

        print(f"Excluído: {texto_excluido}")