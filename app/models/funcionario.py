from sqlalchemy import Column, Integer, String, ForeignKey
from ..db.models_base import Base

class Funcionario(Base):
    __tablename__ = 'HSFU'

    codigo_funcionario = Column(Integer, primary_key=True, autoincrement=True)
    nome_funcionario = Column(String(100))
    cpf = Column(String(14))  
    email = Column(String(100))
    senha = Column(String(50))
    telefone = Column(String(20))
    cargo = Column(String(100))
    empresa = Column(String(100), ForeignKey('HSCL.codigo_cliente'))

