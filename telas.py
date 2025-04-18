import customtkinter as e
import equacoes
def novaTela(janela):
    janela2 = e.CTkToplevel(janela, fg_color="darkblue")
    janela2.geometry("400x300")
    janela2.title("Janela 2")
    janela2.transient(janela)

    titulo = e.CTkLabel(janela2, text="Vamos Somar", text_color="White", font=("Arial", 20, "bold"))
    titulo.place(x=150, y=10)
    ipt1 = e.CTkEntry(janela2, placeholder_text="digite um numero")
    ipt1.place(x=10, y=80)
    ipt2 = e.CTkEntry(janela2, placeholder_text="digite outro numero")
    ipt2.place(x=10, y=130)
    bntIr = e.CTkButton(janela2, text="Somar", command=lambda:clique()).place(x=10, y=190)
    mostrar = e.CTkLabel(janela2, text=" ")
    mostrar.place(x=10, y=160)

    def clique():
        try:
            resultado = equacoes.soma(ipt1.get(), ipt2.get())
            mostrar.configure(text=f"Resultado: {resultado}", text_color="Lightgreen", font=("Arial", 20, "bold"))
        except Exception as ex:
            mostrar.configure(text=f"Erro: {ex}")

    btpegar = e.CTkButton(janela2, text="pegar", command=clique)
    btpegar.place(x=10, y=190)


    novaTela.lift()

def JanelaTroll(janela):
    janelaT = e.CTkToplevel(janela, fg_color="darkblue")
    janelaT.geometry("400x400")
    janelaT.title("Página para multiplicação")
    janelaT.transient(janela)

    titulo = e.CTkLabel(janelaT, text="Vamos Multiplicar", text_color="White", font=("Arial", 20, "bold"))
    titulo.place(x=150, y=10)
    field = e.CTkEntry(janelaT, placeholder_text="digite um numero")
    field.place(x=10, y=80)
    field2 = e.CTkEntry(janelaT, placeholder_text="digite outro numero")
    field2.place(x=10, y=130)
    bntIr = e.CTkButton(janelaT, text="Multiplicar", command=lambda:clique()).place(x=10, y=190)
    mostrar = e.CTkLabel(janelaT, text=" ")
    mostrar.place(x=10, y=160)
    
    def clique():

        try:
            resultado =equacoes.multiplicacao(field.get(), field2.get())
            mostrar.configure(text=f"Resultado: {resultado}", text_color="Lightgreen", font=("Arial", 20, "bold"))
        except Exception as ex:
            mostrar.configure(text=f"Erro: {ex}")


    janelaT.lift()

def janela3(janela):
    janela3 = e.CTkToplevel(janela, fg_color="darkblue")
    janela3.geometry("400x300")
    janela3.title("subtração")
    janela3.transient(janela)

    titulo = e.CTkLabel(janela3, text="Vamos Subtrair", text_color="White", font=("Arial", 20, "bold"))
    titulo.place(x=150, y=10)

    ipt1 = e.CTkEntry(janela3, placeholder_text="digite um numero")
    ipt1.place(x=10, y=80)

    ipt2 = e.CTkEntry(janela3, placeholder_text="digite outro numero")
    ipt2.place(x=10, y=130)

    bntIr = e.CTkButton(janela3, text="subtrair", command=lambda:clique()).place(x=10, y=190)

    mostrar = e.CTkLabel(janela3, text=" ")
    mostrar.place(x=10, y=160)

    def clique():
        try:
            resultado = equacoes.subtracao(ipt1.get(), ipt2.get())
            mostrar.configure(text=f"Resultado: {resultado}", text_color="Lightgreen", font=("Arial", 20, "bold"))
        except Exception as ex:
            mostrar.configure(text=f"Erro: {ex}")


def janela4(janela):
    janela_registro = e.CTkToplevel(janela, fg_color="darkblue")
    janela_registro.geometry("800x600")
    janela_registro.title("Registro")
    janela_registro.transient(janela)

    titulo = e.CTkLabel(janela_registro, text="Tela de registro", text_color="White", font=("Arial", 20, "bold"), bg_color="transparent").place(x=150, y=10)
    quadro = e.CTkFrame(janela_registro, width=600, height=400, bg_color="gray", border_color="darkgray", border_width=3).place(x=50, y=70)
    labelRegistro = e.CTkLabel(janela_registro, text="Nome", text_color="White", font=("Arial", 14, "bold")).place(x=50, y=90)
    ipt1 = e.CTkEntry(janela_registro, placeholder_text="Digite o nome do usuario")
    ipt1.place(x=50, y=110)
    labelRegistro2 = e.CTkLabel(janela_registro, text="Email", text_color="White", font=("Arial", 14, "bold")).place(x=50, y=130)
    ipt2 = e.CTkEntry(janela_registro, placeholder_text="Digite o email do usuario")
    ipt2.place(x=50, y=150)
    labelRegistro3 = e.CTkLabel(janela_registro, text="Senha", text_color="White", font=("Arial", 14, "bold")).place(x=50, y=170)
    ipt3 = e.CTkEntry(janela_registro, placeholder_text="Digite a senha do usuario", show="*")
    ipt3.place(x=50, y=190)
    btn = e.CTkButton(janela_registro, text="Cadastrar", command=lambda: criar_registro(ipt1, ipt2, ipt3, janela_registro)).place(x=50, y=220)
    registros = []

    def criar_registro(ipt1, ipt2, ipt3, janela_registro):
        nome = ipt1.get()
        email = ipt2.get()
        senha = ipt3.get()

        usuario = {
            "nome": nome,
            "email": email,
            "senha": senha
        }

        registros.append(usuario)
        mostrar_registros(janela_registro)

    def mostrar_registros(janela_registro):
        y = 250
        for registro in registros:
            label_nome = e.CTkLabel(janela_registro, text=f"Nome: {registro['nome']}", text_color="White", font=("Arial", 14, "bold")).place(x=50, y=y)
            label_email = e.CTkLabel(janela_registro, text=f"Email: {registro['email']}", text_color="White", font=("Arial", 14, "bold")).place(x=50, y=y+30)
            label_senha = e.CTkLabel(janela_registro, text=f"Senha: {registro['senha']}", text_color="White", font=("Arial", 14, "bold")).place(x=50, y=y+60)
            y += 90