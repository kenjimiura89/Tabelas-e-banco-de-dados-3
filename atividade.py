#Utilizando o comando INSERT, insira mais dois novos fornecedores:
# “Padaria do Pão” e “Marcenaria Martelo”, com os ids 3 e 4 respectivamente, e crie também os endereços;

import sqlite3
conexao = sqlite3.connect('atividade_Fornecedores')

cursor.execute ('DELETE FROM Forncedores WHERE id = 3;')
cursor.execute ('DELETE FROM Forncedores WHERE id = 4;')
cursor.execute ('INSERT INTO Fornecedores (id, nome, endereço) VALUES (3, "Padaria do Pão", "Rua Pão, 50"));')
cursor.execute ('INSERT INTO Fornecedores (id, nome, endereço) VALUES (4, “Marcenaria Martelo, "Rua Martelo, 20"));')

conexao.commit()
conexao.close

#Atualize o endereço do fornecedor com id = 2 para “Rua dos Peixes, 26” com o comando UPDATE;

cursor.execute ('UPDATE Fornecedores SET endereço = “Rua dos Peixes, 26” WHERE id = 2')

#Selecione todos os registros da tabela fornecedor com o comando SELECT;

cursor.execute ('SELECT id, nome, endereço, produto FROM Fornecedores;')

#Selecione todos os registros da tabela fornecedor que tenham a coluna produto igual a Carnes;

cursor.execute ('SELECT produto FROM Fornecedores WHERE produtos = "Carnes";')

#Remova o fornecedor que tem o id = 1 com o comando DELETE.

cursor.execute ('DELETE FROM Fornecedores WHERE id = 1;')