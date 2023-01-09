import sqlite3#biblioteca do sql

conn = sqlite3.connect('UsersData.db')#Conectar a pasta, que sera criada com o nome dado da variavel 


cursor = conn.cursor()#Cursor de conectividade


#CRIANDO TABELA DOS DADOS QUE SERÃO ARMAZENADOS
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    User TEXT NOT NULL,
    Password TEXT NOT NULL
);
""")

print("Conectado ao Banco de Dados")
