from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title('')
janela.geometry('310x270')
janela.resizable(width=False, height=False)
janela.configure(bg='white')
janela.iconphoto(False, PhotoImage(file='logo.png'))


# Cores

co0 ='#ffffff'
co1 = '#000000'
co2 = '#a8caff'

# dividindo a janela em duas partes

frame_cima= Frame(janela, width=295, height=50, bg='white', pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo= Frame(janela, width=295, height=180, bg='white', pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)


#-----função ------
def calcular():

    
    peso = float(e_peso.get())
    altura = float(e_altura.get())
    
    imc = resultado = peso / altura**2
    
    resultado = imc

    

    if resultado < 18.5:
        l_resultado_texto['text'] ='Seu IMC é: Abaixo do peso.'
        
        
    elif resultado >= 18.5 and resultado < 25: 
        l_resultado_texto['text'] ='Seu IMC é: Normal.'
        
    elif resultado >= 25 and resultado < 30:
         l_resultado_texto['text'] ='Seu IMC é: Sobrepeso'
         
    else:  
        l_resultado_texto['text'] = 'Seu IMC é: Obesidade.'

    l_resultado['text'] = "{:.{}f}".format(resultado, 2)

   


# ------------ configurando frame cima ------------

app_nome = Label(frame_cima, text='Calculadora de IMC', width=22, height=1, padx=0, relief='flat', anchor='center', font=('Poppins 16 '), bg=co0, fg=co1)
app_nome.place(x=0, y=0)

app_linha = Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Poppins 1'), bg=co2, fg=co1)
app_linha.place(x=0, y=35)



# configurando frame de baixo

l_peso = Label(frame_baixo, text='Insira seu peso:', height=1, padx=5, relief='flat', anchor='w', font=('Poppins 10 '), bg=co0, fg=co1)
l_peso.grid(row=0, column=0, sticky=W, pady=10, padx=3)

e_peso = Entry(frame_baixo, width=5, relief='solid', font=('Poppins 10 bold'), justify='center')
e_peso.grid(row=0, column=1, sticky=W, pady=10, padx=3)

# FRAME ALTURA

l_altura = Label(frame_baixo, text='Insira sua altura:', height=1, padx=5, relief='flat', anchor='w', font=('Poppins 10 '), bg=co0, fg=co1)
l_altura.grid(row=1, column=0, sticky=W, pady=10, padx=3)

e_altura = Entry(frame_baixo, width=5, relief='solid', font=('Poppins 10 bold'), justify='center')
e_altura.grid(row=1, column=1, sticky=W, pady=10, padx=3)

#RESULTADO

l_resultado = Label(frame_baixo, text='---', width=4, height=1, padx=6, pady=12,  relief='flat', anchor='center', font=('Poppins 20 bold'), bg=co2, fg=co0)
l_resultado.place(x=200, y=12)

# -----------------------------

l_resultado_texto = Label(frame_baixo, text='', width=35, height=1, padx=6, pady=12,  relief='flat', anchor='center', font=('Poppins 10 bold'), bg=co0, fg=co1)
l_resultado_texto.place(x=0, y=100)

b_calcular = Button(frame_baixo, command=calcular, text='Calcular', width=36, height=1, overrelief=SOLID,  relief='raised', anchor='center', font=('Poppins 10 bold'), bg=co2, fg=co1)
b_calcular.grid(row=4, column=0, sticky=W, pady=60, padx=5, columnspan=25)

#----- calculos configuração -----


janela.mainloop()