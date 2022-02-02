# Instale o SQLAlchemy -> Windows: pip install sqlalchemy
# Crie uma pasta para o projeto, ex: sqlalchemy (dentro da pasta Documentos)
# Certifique-se que tem o Python e PyCharm instalados, e vamos mão a obra

from sqlalchemy import (create_engine, String, Integer, Column, Table, MetaData)

engine = create_engine('sqlite:///banco.db', echo=True)
metadata = MetaData(bind=engine)

tabela_usuario = Table('usuario', metadata,
                      Column('id', Integer, primary_key=True),
                      Column('nome', String(40)),
                      Column('idade', Integer),
                      Column('endereco', String(100)),
                      Column('cidade', String(65)),
                      Column('estado', String(2)))

metadata.create_all()