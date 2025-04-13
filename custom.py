import customtkinter as e
import math
import telas

janela = e.CTk()
janela.lower()
janela.title("Minha Janela")
janela.maxsize(500, 400)
janela.geometry("400x300")
janela._set_appearance_mode("dark")
janela.configure(fg_color="teal")


texto = e.CTkLabel(janela, text="Ola Mundo!", text_color="White", font=("Arial", 20, "bold"))
texto.place(x=150, y=10)


btn1 = e.CTkButton(janela, text="Soma", command=lambda:telas.novaTela(janela), fg_color="red", border_color="white", border_width=4, height=50)
btn1.configure(hover_color="green")
btn1.place(x=50, y=200)

btn2 = e.CTkButton(janela, text="Multiplicação", command=lambda:telas.JanelaTroll(janela), fg_color="purple", border_color="white", border_width=4, height=50)
btn2.configure(hover_color="green")
btn2.place(x=240, y=200)

janela.mainloop()
