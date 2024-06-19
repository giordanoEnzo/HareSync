# HareSync/app/models/cliente.py

from sqlalchemy import Column, Integer, String, ForeignKey
from . import Base  # Importe a Base do SQLAlchemy adequada ao seu projeto

class Cliente(Base):
    __tablename__ = 'HSCL'

    codigo_cliente = Column(String(20), primary_key=True)
    nome_cliente = Column(String(100))
    sigla = Column(String(10))
    cpf_cnpj = Column(String(14))
    senha = Column(String(50))
    email = Column(String(100))
    telefone = Column(String(20))
    contrato = Column(String(50), ForeignKey('HSCT.codigo_contrato'))

    def __repr__(self):
        return f"<Cliente(codigo_cliente='{self.codigo_cliente}', nome_cliente='{self.nome_cliente}', email='{self.email}')>"
