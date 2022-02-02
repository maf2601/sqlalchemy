from main import engine, tabela_usuario

connect = engine.connect()
insert = tabela_usuario.insert()

usuario = insert.values(nome='Maria Silveira', idade=44, endereco='Rua A', cidade='Olinda', estado='PE')
usuario02 = insert.values(nome='Viviane Ferreira', idade=43, endereco='Rua B', cidade='Morumbi', estado='SP')
usuario03 = insert.values(nome='Bruno Silva', idade=28, endereco='Rua C', cidade='Joinville', estado='SC')

connect.execute(usuario)
connect.execute(usuario02)
connect.execute(usuario03)