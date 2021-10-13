
import tkinter as tk

#janela principal.
janela = tk.Tk()
janela.geometry("320x333")
janela.resizable(0, 0)
janela.title("Calculadora")

# Expressão exibida no display.
expressao = ""

# Variável conectada ao display.
textoDoDisplay = tk.StringVar()

# Esta função atualiza o display sempre que uma tecla é pressionada.
def botaoClicado(botao):
    global expressao
    expressao = expressao + str(botao)
    textoDoDisplay.set(expressao)

# Esta função limpa o display.
def botaoLimparClicado(): 
    global expressao 
    expressao = "" 
    textoDoDisplay.set("")

# Esta função realiza o cálculo da expressão no display.
def botaoIgualClicado():
    global expressao
    resultado = str(eval(expressao))
    textoDoDisplay.set(resultado)
    expressao = resultado

# Cria uma moldura para o display.
frameDoDisplay = tk.Frame(janela, width=320, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
frameDoDisplay.pack(side=tk.TOP)

# Cria o display.
display = tk.Entry(frameDoDisplay, font=["courier", 18, "bold"], textvariable=textoDoDisplay, width=50, bg="white", bd=0, justify=tk.RIGHT)
display.grid(row=0, column=0)
display.pack(ipady=10)

# Cria uma moldura para os botões.
frameDosBotoes = tk.Frame(janela, width=320, height=190, bd=5, bg="grey")
frameDosBotoes.pack()

# Cria os botões.
limpar = tk.Button(frameDosBotoes, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "white", cursor = "hand1", command = lambda: botaoLimparClicado()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
dividir = tk.Button(frameDosBotoes, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand1", command = lambda: botaoClicado("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

sete = tk.Button(frameDosBotoes, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand1", command = lambda: botaoClicado(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
oito = tk.Button(frameDosBotoes, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand1", command = lambda: botaoClicado(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nove = tk.Button(frameDosBotoes, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand1", command = lambda: botaoClicado(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiplicar = tk.Button(frameDosBotoes, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand1", command = lambda: botaoClicado("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

quatro = tk.Button(frameDosBotoes, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand1", command = lambda: botaoClicado(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
cinco = tk.Button(frameDosBotoes, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand1", command = lambda: botaoClicado(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
seis = tk.Button(frameDosBotoes, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand1", command = lambda: botaoClicado(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
subtrair = tk.Button(frameDosBotoes, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand1", command = lambda: botaoClicado("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

um = tk.Button(frameDosBotoes, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand1", command = lambda: botaoClicado(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
dois = tk.Button(frameDosBotoes, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand1", command = lambda: botaoClicado(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
tres = tk.Button(frameDosBotoes, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand1", command = lambda: botaoClicado(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
somar = tk.Button(frameDosBotoes, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand1", command = lambda: botaoClicado("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

zero = tk.Button(frameDosBotoes, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand1", command = lambda: botaoClicado(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
ponto = tk.Button(frameDosBotoes, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand1", command = lambda: botaoClicado(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
igual = tk.Button(frameDosBotoes, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand1", command = lambda: botaoIgualClicado()).grid(row = 4, column = 3, padx = 1, pady = 1)

janela.mainloop()
