from tkinter import* 
from tkinter import Tk, StringVar, ttk
from tkinter import filedialog as fd
from tkinter import messagebox

from PIL import Image, ImageTk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

#importando views
from view import *


c00 = "#2e2d2b"   # Preta
c01 = "#feffff"   # branca
c02 = "#4fa882"   # verde
c03 = "#38576b"   # valor
c04 = "#403d3d"   # letra
c05 = "#e06636"   # profit
c06 = "#03cfcf"   # azul
c07 = "#3fbfb9"   # verde
c08 = "#263238"   # + verde
c09 = "#e9edf5"   # + verde

colors = ['#1f77b4', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555', '#1f77b4', '#ff7f0e',
          '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbc22', '#17becf',
          '#ff9896', '#98df8a']



#criando janela

janela = Tk ()
janela.title ("")
janela.geometry('700x350')
janela.configure (background=c09)
janela.resizable (width=FALSE, height=FALSE)

#definindo estilo
style = ttk.Style(janela)
style.theme_use("clam")



#dividindo la janelita

frameCima = Frame(janela, width=700, height=50, bg=c01, relief="flat",)
frameCima.grid(row=0, column=0) #cria a sessão superior, com a logo e o titulo

frameMeio = Frame(janela, width=700, height=300, bg=c01)
frameMeio.grid(row=1, column=0, sticky=NSEW)#cria o meio com as opções


#abrindo imagens, icones etc

app_img = Image.open('icon.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text="Organizador de arquivos", width=700, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20'), bg=c01, fg=c04)
app_logo.place(x=0, y=0)

#criando o meio

frame_operacoes = Frame(frameMeio, width=300, height=350, bg=c01)
frame_operacoes.grid(row=0, column=0)

frame_grafico = Frame(frameMeio, width=400, height=350, bg=c01)
frame_grafico.place(x=170, y=0)

frame_operacoes.lift()

#funcao grafico pie

def grafico_pie(lista_1, lista_2):
    figura = plt.Figure(figsize=(5, 3), dpi=100)
    ax = figura.add_subplot(111)

    lista_valores = lista_1
    lista_extencao = lista_2

    ax.pie(lista_valores, wedgeprops=dict(width=0.3), colors=colors, shadow=True, startangle=90)

    ax.legend(lista_extencao, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva = FigureCanvasTkAgg(figura, frame_grafico)
    canva.get_tk_widget().grid(row=0, column=0, sticky=NSEW)




#criando entradas e botões

l_app = Label(frame_operacoes, text="Selecione a pasta",anchor=NW, font=('Ivy 10 bold'), bg=c01, fg=c04)
l_app.place(x=10, y=10)

#definindo global a variavel pasta
global pasta 

#funcao para escolher a pasta

def escolher_pasta():
    global escolher_pasta

    pasta = fd.askdirectory() 


    #criando lista de extencoes compativeis
    lista_extencao = ['.txt','.psd','.pdf', '.png','jpg', 'mp4','mp3', '.wav', '.docx']
    lista_extencao_comobox = []
    lista_extencao_contado = []
    lista_extencao_valores = []

    numero_de_pastas = 0

    for i in lista_extencao:
        caminho_pasta = pasta
        extensao = i
        numero_de_ficheiros, numero_de_pasta = count_files_and_folders(caminho_pasta, extensao)

        if numero_de_ficheiros <= 0:
            pass
        else: 
            lista_extencao_contado.append(i + ": " + str(numero_de_ficheiros))
            lista_extencao_comobox.append(i)
            lista_extencao_valores.append(numero_de_ficheiros)
            numero_de_pasta = numero_de_pasta

    #adicionando o total de numero de pastas
    lista_extencao_contado.append('pastas: ' + str(numero_de_pasta))
    lista_extencao_valores.append(numero_de_pasta)

    #passando extencoes para combobox
    combo_extensao['values'] = (lista_extencao_comobox)


    #enviando os valores para o grafico chamando a funcao grafico
    grafico_pie(lista_extencao_valores, lista_extencao_contado)
#isso vai criar o botão para "escolher a pasta", talvez de modo funcional

b_escolher = Button(frame_operacoes, command=escolher_pasta, text="Escolher", width=15, overrelief=RIDGE, font=('ivy 8'),bg=c01, fg=c04)
b_escolher.place(x=10, y=40)


l_app = Label(frame_operacoes, text='Copiar Arquivos' , anchor=NW, relief='flat', font=('Ivy 10'), bg=c01, fg=c04)
l_app.place(x=10, y=91)

def copiar():
    global pasta 
    # pegando extensao
    extensao = combo_extensao.get()
    # pegando extensao
    destino = fd.askdirectory()
    #chamand funcao copiar arquivos
    copiar_arquivos(pasta, destino, extensao)

    messagebox.showinfo('Copiar', 'Os ficheiros foram copiados com sucesso.')

    # após isso, limpa 

    combo_extensao.delete(0, END)

combo_extensao = ttk.Combobox(frame_operacoes, width=5, font=('Ivy 10'))
combo_extensao.place(x=110, y=91)

janela.mainloop()

img_copiar = Image.open('copy.png')
img_copiar = img_copiar.resize((17,17))
img_copiar = ImageTk.PhotoImage(img_copiar)

b_copiar = Button(frame_operacoes, command=copiar, image=img_copiar, compound=LEFT, anchor=NW, text = "Escolher destino", width=100, overrelief= RIDGE, font=('Ivy 8'), bg=c01, fg=c04)
b_copiar.place(x=171, y=90) 