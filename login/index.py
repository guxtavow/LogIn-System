#importação de bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk         #biblioteca grafica para box de texto
import DataBase


#Criação da janela
jan  = Tk()#variavel da janela. metodo TK() é a atribuição para mostrar que nossa variavel é uma JANELA DE ACESSO
jan.title("DP System  - Painel de Acesso")#Titulo da janela
jan.geometry("600x300")#Tamanho da janela
jan.configure(background="white")#Cor da nossa janela
jan.resizable(width=False, height=False)#Para janela não perder as propriedades de largura e tamanho(maximização, diminuição etc)
#como o programa é pequeno = sem necessidade de ser responsivo
#jan.attributes("-alpha",0.9) para caso queira sua janela transparente, quanto menor o numero, mais transparente ela é
jan.iconbitmap(default="icons/LogoIcon.ico")#Para colocar o Icone da imagem no topo da janela

#------Carregar imagem------
logo = PhotoImage(file="icons/logo.png")#para receber a imagem no tkinter(tkinter é melhor de trabalhar com PNG)

#-----widgets da janela

#leftframe
LeftFrame = Frame(jan, width=200, height=300,bg="MIDNIGHTBLUE",relief="raise")#separação da janela, parte esquerda. ALtura, largura, cor e propriedades(raise = simples)
LeftFrame.pack(side=LEFT) #aparecer no lado esquerdo a separação
#leftframe

#rightframe
RightFrame = Frame(jan, width=395, height=300,bg="MIDNIGHTBLUE",relief="raise")#fundo branco para criar um separador mais simples do que criar uma propriedade para o separador
RightFrame.pack(side=RIGHT)
#rightframe

#LOGO
LogoLabel = Label(LeftFrame, image=logo,bg="MIDNIGHTBLUE")#Criando um label para por a imagem/O "bg" é por conta que foi alterado a cor da janela
LogoLabel.place(x=50, y=100)#posicionando a imagem
#LOGO

#Sistema do usuario-------
# LOGIN
#entrada de dados
#Usuario
UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE",fg="White")#criando a parte de username/FG = cor do texto/Font = Fonte do texto
UserLabel.place(x=5, y=100)#posicionamento do texto 

UserEntry= ttk.Entry(RightFrame, width=30)#Onde o usuario colocara seus dados
UserEntry.place(x=151, y=114)#posicionando dados

#Senha
PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE",fg="White")
PassLabel.place(x=5, y=150)#posicionamento do texto 

PassEntry= ttk.Entry(RightFrame, width=30, show='•')#Onde o usuario colocara seus dados
PassEntry.place(x=151, y=163)#posicionando dados
#LOGIN
#Sistema do usuario-------
def LogIn():#Seleciono as informações que quero a vereficação para saber se a pessoa tem registro no banco de dados
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBase.cursor.execute("""
    SELECT * FROM Users
    WHERE (User = ? AND Password = ?)
    """,(User, Pass))
    print("Selecionou")#verificar se nosso banco de dados selecionou as tabelas corretas
    VerifyLogin =  DataBase.cursor.fetchone() #fetchall pega todos os dados, já fetchone pega um
    try: #metodo de tentativa do usuario
        if(User in VerifyLogin and Pass in VerifyLogin):#verificando informações de login 
            messagebox.showinfo(title="Login Info", message="Login Sucessfull")
        else:
            pass #pular essa fase afinal o except já ira me dizer se o login está errado ou não 
    except:
        messagebox.showerror(title="Login Info", message="Username or Password are incorrect, please verify!!!")
#Botões----------
#Botão de login
LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=LogIn)#Criando o botão de login
LoginButton.place(x=110,y=225)#Posicionando o botão



#Botão de registro
def Register():#criando a função de registro
    #Removendo widgets de login
    LoginButton.place(x=6000)#dessa forma tiro o botão de login da tela para substituir por outro
    RegisterButton.place(x=6000)#Mesma coisa do login

    #Widgets de cadastro
    #NOME
    NomeLabel = Label(RightFrame, text="Name:",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")#Nome de registro
    NomeLabel.place(x=5,y=5)#Posicionando label

    NomeEntry = ttk.Entry(RightFrame,width=30)
    NomeEntry.place(x=120,y=20)
    #NOME

    #EMAIL
    EmailLabel = Label(RightFrame, text="Email:",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")#Email de registro
    EmailLabel.place(x=5,y=55)#Posicionando label

    EmailEntry = ttk.Entry(RightFrame,width=30)
    EmailEntry.place(x=120,y=68)
    #EMAIL

    def RegisterToDataBase():#inserção de dados ao database
        Name = NomeEntry.get()#Criei uma variavel que recebe o valor do entry
        Email = EmailEntry.get()
        Username = UserEntry.get()
        Password = PassEntry.get()
        #verificar informações
        if (Name == "" and Email == "" and Username== "" and Password== ""):#Campos não podem estar em branco
            messagebox.showerror(title="Register Error", message="Fill all informations for the register")
        else:
        #Insiro as variaveis que vou querer registrar e "?" no numero de variaveis que vou inserir
            DataBase.cursor.execute("""
            INSERT INTO Users(Name, Email, User, Password) VALUES(?,?,?,?)
            """, (Name, Email, Username, Password))#insiro as variaveis do python no banco de dados
            DataBase.conn.commit()#Commit = salva as alterações feitas no banco de dados
            messagebox.showinfo(title="Info de Registro", message="Register created sucessfull")#Mensagem apresentada ao usuario

    Register = ttk.Button(RightFrame, text="Register", width=20, command=RegisterToDataBase)
    Register.place(x=125,y=220)#botão de registro


    def BackToLogin():
            NomeLabel.place(x=6000)
            NomeEntry.place(x=6000)
            EmailEntry.place(x=6000)
            EmailLabel.place(x=6000)
            Register.place(x=6000)
            BackButton.place(x=6000)    
    #Trazendo os widgets de login de volta
            LoginButton.place(x=100)
            RegisterButton.place(x=125)

    BackButton = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    BackButton.place(x=125,y=260)# botão de back para login

RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)#Command é recomendado para botões
RegisterButton.place(x=140,y=260)       






#-----widgets da janela


jan.mainloop()#Para dizer que nossa janela acabou ou seja, fora da janela, não é do programa
#/Criação da janela