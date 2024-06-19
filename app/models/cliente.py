from sqlalchemy import Column, Integer, String, ForeignKey
from ..db.models_base import Base

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

