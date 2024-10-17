# 10. 
# Crie um banco de dados usando Python e MySQL chamado ‘empregados’ e uma tabela com os campos: ‘id’, ‘nome’ e ‘endereco’.

import mysql.connector
bd = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2001"
)

bd_cursor = bd.cursor()
bd_cursor.execute("SHOW DATABASES")
for banco in bd_cursor:
    print(banco)
