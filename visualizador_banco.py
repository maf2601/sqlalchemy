from sqlalchemy import select
from main import tabela_usuario

sl = select([tabela_usuario])

for linha in sl.execute():
    print(linha)