import tkinter as tk
import requests
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import StringVar

def get_image(url):
    resposta = requests.get(url, stream=True)
    resposta.raw.decode_content=True
    return resposta.raw.read()

def aplicar(frame):
    a = filme.get() 
    frame.destroy()
    f5 = tk.Frame()
    f5.pack()
    f5.tkraise()
    tk.Label(f5, text=a, font=fonte3).grid()
    
    parametros = {"t":a, "apikey":"a6cd2fcc"}
    resposta = requests.get("http://www.omdbapi.com", params=parametros)
    resposta_dic = resposta.json() 
    
    frase2 = tk.Label(f5, text="Ano")
    frase2.grid(row=3, column=0, ipadx=10)
    frase3 = tk.Label(f5, text="Lançamento:")
    frase3.grid(row=4 , column=0)
    frase4 = tk.Label(f5, text="Duração:")
    frase4.grid(row=5 , column=0)
    frase5 = tk.Label(f5, text="Genero")
    frase5.grid(row=6 , column=0)
    frase6 = tk.Label(f5, text="Diretor")
    frase6.grid(row=7 , column=0)
    frase7 = tk.Label(f5, text="Escritor")
    frase7.grid(row=8 , column=0)
    frase8 = tk.Label(f5, text="Ator")
    frase8.grid(row=9 , column=0)
    frase9 = tk.Label(f5, text="Enredo:")
    frase9.grid(row=10 , column=0)
    frase11 = tk.Label(f5, text="Idioma")
    frase11.grid(row=11 , column=0)
    frase12 = tk.Label(f5, text="Pais origem")
    frase12.grid(row=12 , column=0)
    frase13 = tk.Label(f5, text="Premios")
    frase13.grid(row=13 , column=0)
    nome = tk.Label(f5, text=resposta_dic['Year'])
    nome.grid(row=3, column=1)
    nasc = tk.Label(f5, text=resposta_dic['Released'])
    nasc.grid(row=4, column=1)
    cpf = tk.Label(f5, text=resposta_dic['Runtime'])
    cpf.grid(row=5, column=1)
    mail = tk.Label(f5, text=resposta_dic['Genre'])
    mail.grid(row=6, column=1)
    city = tk.Label(f5, text=resposta_dic['Director'])
    city.grid(row=7, column=1)
    rua = tk.Label(f5, text=resposta_dic['Writer'])
    rua.grid(row=8, column=1)
    cpl = tk.Label(f5, text=resposta_dic['Actors'])
    cpl.grid(row=9, column=1)
    ref = tk.Label(f5, text=resposta_dic['Plot'])
    ref.grid(row=10, column=1)
    ncard = tk.Label(f5, text=resposta_dic['Language'])
    ncard.grid(row=11, column=1)
    nume = tk.Label(f5, text=resposta_dic['Country'])
    nume.grid(row=12, column=1)
    venc = tk.Label(f5, text=resposta_dic['Awards'])
    venc.grid(row=13, column=1)    
    f6 = tk.Frame()
    f6.pack()
    voltar = tk.Button(f6, command=lambda:inicial(f5, f6), text='Voltar')
    voltar.grid()
    
def aplicar2(frame):
    a = filme.get() 
    frame.destroy()
    f5 = tk.Frame()
    f5.pack()
    f5.tkraise()
    tk.Label(f5, text=a, font=fonte3).pack()
    parametros = {
    "q":a,
    "format":"json"
    }
    resposta = requests.get("http://api.duckduckgo.com", params=parametros)
    resposta_dic = resposta.json()
    T = tk.Text(f5, height=2, width=30)
    T.pack()
    T.insert(END, text=resposta_dic["Abstract"])
    #tk.Label(f5, text=resposta_dic["Abstract"]).pack()
    f6 = tk.Frame()
    f6.pack()
    voltar = tk.Button(f6, command=lambda:inicial(f5, f6), text='Voltar')
    voltar.pack()
     
    
def inicial(frame, frame2):
    global filme
    frame.destroy()
    frame2.destroy()
    f4 = tk.Frame()
    f4.pack()
    f4.tkraise()   
    tk.Label(f4, text="Filmes", font=fonte3).pack()
    notebook = ttk.Notebook(f4)
    f1 = ttk.Frame(notebook)
    f2 = ttk.Frame(notebook)
    f3 = ttk.Frame(notebook)
    notebook.add(f1, text='Pesquisa')
    notebook.add(f2, text='Séries')
    notebook.add(f3, text='Informações da conta')
    notebook.pack()
    tk.Button(f4, text="logoff", command=lambda:entrar2(f4), font=fonte, bg="grey").pack()
    frase1 = tk.Label(f3, text="DADOS DO USUÁRIO")
    frase1.grid(row=2 , column=1)
    frase2 = tk.Label(f3, text="Nome de usuário")
    frase2.grid(row=3, column=0)
    frase3 = tk.Label(f3, text="Data de Nascimento")
    frase3.grid(row=4 , column=0)
    frase4 = tk.Label(f3, text="CPF")
    frase4.grid(row=5 , column=0)
    frase5 = tk.Label(f3, text="e-mail")
    frase5.grid(row=6 , column=0)
    frase6 = tk.Label(f3, text="ENDEREÇO DE COBRANÇA")
    frase6.grid(row=7 , column=1)
    frase7 = tk.Label(f3, text="Cidade")
    frase7.grid(row=8 , column=0)
    frase8 = tk.Label(f3, text="Rua")
    frase8.grid(row=9 , column=0)
    frase9 = tk.Label(f3, text="Complemento")
    frase9.grid(row=10 , column=0)
    frase11 = tk.Label(f3, text="Referência")
    frase11.grid(row=11 , column=0)
    frase12 = tk.Label(f3, text="DADOS DE PAGAMENTO")
    frase12.grid(row=12 , column=1)
    frase13 = tk.Label(f3, text="Nome (Como Impresso no Cartão)")
    frase13.grid(row=13 , column=0)
    frase14 = tk.Label(f3, text="Número do Cartão")
    frase14.grid(row=14 , column=0)
    frase15 = tk.Label(f3, text="Data de Vencimento")
    frase15.grid(row=15 , column=0)
    frase16 = tk.Label(f3, text="Código de Segurança")
    frase16.grid(row=16 , column=0)
    nome = tk.Label(f3, text=nome_final)
    nome.grid(row=3, column=1)
    nasc = tk.Label(f3, text=nasc_final)
    nasc.grid(row=4, column=1)
    cpf = tk.Label(f3, text=cpf_final)
    cpf.grid(row=5, column=1)
    mail = tk.Label(f3, text=mail_final)
    mail.grid(row=6, column=1)
    city = tk.Label(f3, text=city_final)
    city.grid(row=8, column=1)
    rua = tk.Label(f3, text=rua_final)
    rua.grid(row=9, column=1)
    cpl = tk.Label(f3, text=complemento_final)
    cpl.grid(row=10, column=1)
    ref = tk.Label(f3, text=ref_final)
    ref.grid(row=11, column=1)
    ncard = tk.Label(f3, text=ncard_final)
    ncard.grid(row=13, column=1)
    nume = tk.Label(f3, text=nume_final)
    nume.grid(row=14, column=1)
    venc = tk.Label(f3, text=venc_final)
    venc.grid(row=15, column=1)
    cod = tk.Label(f3, text=cod_final)
    cod.grid(row=16, column=1)   
    cat = tk.Label(f1, text='Escreva o filme que deseja pesquisar:')
    cat.pack()
    filme = tk.Entry(f1)
    filme.pack()
    tk.Button(f1,command=lambda:aplicar(f4), text='aplicar').pack()
    
    cat = tk.Label(f2, text='Escreva o nome do ator:')
    cat.pack()
    filme = tk.Entry(f2)
    filme.pack()
    tk.Button(f2,command=lambda:aplicar2(f4), text='aplicar').pack()
    
    
def criar_conta(frame):
    global nome
    global nasc
    global cpf
    global mail
    global city
    global rua
    global compl
    global ref
    global ref
    global ncard
    global nume
    global venc
    global code
    global senha1
    global senha2
    frame.destroy()
    f3 = tk.Frame()
    f3.pack()
    f3.tkraise()
    tk.Label(f3, text="Criar Conta", font=fonte2).grid(row=0, column=0)
    nome=tk.Entry(f3)
    nome.grid(row=3, column=1)
    nasc=tk.Entry(f3)
    nasc.grid(row=4, column=1)
    cpf=tk.Entry(f3)
    cpf.grid(row=5, column=1)
    mail=tk.Entry(f3)
    mail.grid(row=6, column=1)
    city=tk.Entry(f3)
    city.grid(row=8, column=1)
    rua=tk.Entry(f3)
    rua.grid(row=9, column=1)
    compl=tk.Entry(f3)
    compl.grid(row=10, column=1)
    ref=tk.Entry(f3)
    ref.grid(row=11, column=1)
    ncard=tk.Entry(f3)
    ncard.grid(row=13, column=1)
    nume=tk.Entry(f3)
    nume.grid(row=14, column=1)
    venc=tk.Entry(f3)
    venc.grid(row=15, column=1)
    code=tk.Entry(f3)
    code.grid(row=16, column=1)
    senha1 = tk.Entry(f3, show="*")
    senha1.grid(row=18, column=1)
    senha2 = tk.Entry(f3, show="*")
    senha2.grid(row=19, column=1)
    frase1 = tk.Label(f3, text="DADOS DO USUÁRIO")
    frase1.grid(row=2 , column=1)
    frase2 = tk.Label(f3, text="Nome de usuário")
    frase2.grid(row=3, column=0)
    frase3 = tk.Label(f3, text="Data de Nascimento")
    frase3.grid(row=4 , column=0)
    frase4 = tk.Label(f3, text="CPF")
    frase4.grid(row=5 , column=0)
    frase5 = tk.Label(f3, text="e-mail")
    frase5.grid(row=6 , column=0)
    frase6 = tk.Label(f3, text="ENDEREÇO DE COBRANÇA")
    frase6.grid(row=7 , column=1)
    frase7 = tk.Label(f3, text="Cidade")
    frase7.grid(row=8 , column=0)
    frase8 = tk.Label(f3, text="Rua")
    frase8.grid(row=9 , column=0)
    frase9 = tk.Label(f3, text="Complemento")
    frase9.grid(row=10 , column=0)
    frase11 = tk.Label(f3, text="Referência")
    frase11.grid(row=11 , column=0)
    frase12 = tk.Label(f3, text="DADOS DE PAGAMENTO")
    frase12.grid(row=12 , column=1)
    frase13 = tk.Label(f3, text="Nome Cartão")
    frase13.grid(row=13 , column=0)
    frase14 = tk.Label(f3, text="Número do Cartão")
    frase14.grid(row=14 , column=0)
    frase15 = tk.Label(f3, text="Data de Vencimento")
    frase15.grid(row=15 , column=0)
    frase16 = tk.Label(f3, text="Código de Segurança")
    frase16.grid(row=16 , column=0)
    frase17 = tk.Label(f3, text="SENHA")
    frase17.grid(row=17, column=1)
    frase18 = tk.Label(f3, text="digite a senha")
    frase18.grid(row=18, column=0)
    frase19 = tk.Label(f3, text="digite a senha novamente")
    frase19.grid(row=19, column=0)
    tk.Label(f3, text="").grid()
    tk.Button(f3, text="APLICAR", command=lambda:entrar(f3), font=fonte, bg="grey").grid()
    tk.Label(f3, text="").grid()
    
def entrar2 (frame):
    frame.destroy()
    f1 = tk.Frame()
    f1.pack()
    f1.tkraise()
    tk.Label(f1, text="FILMES", font=fonte3, fg="red").grid(row=0, column=2)
    tk.Label(f1, text="nome:").grid(row=2, column=1)
    tk.Label(f1, text="senha:").grid(row=3, column=1)
    usuario = tk.Entry(f1)
    usuario.grid(row=2, column=2)
    senha = tk.Entry(f1, show="*")
    senha.grid(row=3, column=2)
    tk.Button(f1, text="entrar",  command=lambda:inicial(f1), font=fonte).grid(row=4, column=2)
    tk.Label(f1, text="ainda não é cadastrado?").grid(row=6, column=3)
    tk.Button(f1, text="clique aqui", command=lambda:criar_conta(f1)).grid(row=6, column=4)



def entrar (frame):
    global nome_final
    global nasc_final
    global cpf_final
    global mail_final
    global city_final
    global rua_final
    global complemento_final
    global ref_final
    global ncard_final
    global nume_final
    global venc_final 
    global cod_final
    global usuario_final
    global senha_final
    global senha_final2
    global usuario
    global senha
    senha_final3 = senha2.get()
    senha_final = senha1.get()
    nome_final = nome.get()
    nasc_final = nasc.get()
    cpf_final = cpf.get()
    mail_final = mail.get()
    city_final = city.get()
    rua_final = rua.get()
    complemento_final = compl.get() 
    ref_final = ref.get()
    ncard_final = ncard.get()
    nume_final = nume.get()
    venc_final = venc.get()
    cod_final = code.get()
    if senha_final3 == senha_final:
        f2=tk.Label()
        lista = [nome_final, senha_final]
        frame.destroy()
        f1 = tk.Frame()
        f1.pack()
        f1.tkraise()
        tk.Label(f1, text="FILMES", font=fonte3, fg="red").grid(row=0, column=2)
        tk.Label(f1, text="nome:").grid(row=2, column=1)
        tk.Label(f1, text="senha:").grid(row=3, column=1)
        usuario = tk.Entry(f1)
        usuario.grid(row=2, column=2)
        senha = tk.Entry(f1, show="*")
        senha.grid(row=3, column=2)
        tk.Button(f1, text="entrar",  command=lambda:inicial(f1, f2), font=fonte).grid(row=4, column=2)
        tk.Label(f1, text="ainda não é cadastrado?").grid(row=6, column=3)
        tk.Button(f1, text="clique aqui", command=lambda:criar_conta(f1)).grid(row=6, column=4)

fontep = ("Verdana", 8)
fonte10= ("Verdana", 10)
fonte  = ("Verdana", 12)
fonte3 = ("Verdana", 20)
fonte2 = ("Verdana", 16)

root = tk.Tk()
root.geometry('700x600')
root.title("Filmes")


f1 = tk.Frame()
f1.pack()
f1.tkraise()
f2 = tk.Frame()
tk.Label(f1, text="FILMES", font=fonte3, fg="red").grid(row=0, column=2)
tk.Label(f1, text="nome:").grid(row=2, column=1)
tk.Entry(f1).grid(row=2, column=2)
tk.Label(f1, text="senha:").grid(row=3, column=1)
tk.Entry(f1, show="*").grid(row=3, column=2)
tk.Button(f1, text="entrar", command=lambda:inicial(f1, f2), font=fonte).grid(row=4, column=2)
tk.Label(f1, text="ainda não é cadastrado?").grid(row=6, column=3)
tk.Button(f1, text="clique aqui", command=lambda:criar_conta(f1)).grid(row=6, column=4)


root.mainloop()