import customtkinter as e
import equacoes
def novaTela(janela):
    janela2 = e.CTkToplevel(janela, fg_color="darkblue")
    janela2.geometry("400x300")
    janela2.title("Janela 2")
    janela2.transient(janela)
    ipt1 = e.CTkEntry(janela2, placeholder_text="digite um numero")
    ipt1.place(x=10, y=10)

    ipt2 = e.CTkEntry(janela2, placeholder_text="digite outro numero")
    ipt2.place(x=10, y=40)

    mostrar = e.CTkLabel(janela2, text=" ")
    mostrar.place(x=10, y=100)

    def clique():
        try:
            resultado = equacoes.soma(ipt1.get(), ipt2.get())
            mostrar.configure(text=f"Resultado: {resultado}", text_color="Lightgreen", font=("Arial", 20, "bold"))
        except Exception as ex:
            mostrar.configure(text=f"Erro: {ex}")

    btpegar = e.CTkButton(janela2, text="pegar", command=clique)
    btpegar.place(x=10, y=70)


    janela2.lift()

def JanelaTroll(janela):
    janelaT = e.CTkToplevel(janela, fg_color="darkblue")
    janelaT.geometry("400x400")
    janelaT.title("Página para multiplicação")
    janelaT.transient(janela)

    titulo = e.CTkLabel(janelaT, text="Vamos Multiplicar", text_color="White", font=("Arial", 20, "bold"))
    titulo.place(x=100, y=10)
    field = e.CTkEntry(janelaT, placeholder_text="digite um numero")
    field.place(x=10, y=50)
    field2 = e.CTkEntry(janelaT, placeholder_text="digite outro numero")
    field2.place(x=10, y=80)
    bntIr = e.CTkButton(janelaT, text="Multiplicar", command=lambda:clique()).place(x=10, y=160)
    mostrar = e.CTkLabel(janelaT, text=" ")
    mostrar.place(x=10, y=130)
    
    def clique():

        try:
            resultado =equacoes.multiplicacao(field.get(), field2.get())
            mostrar.configure(text=f"Resultado: {resultado}", text_color="Lightgreen", font=("Arial", 20, "bold"))
        except Exception as ex:
            mostrar.configure(text=f"Erro: {ex}")


    janelaT.lift()