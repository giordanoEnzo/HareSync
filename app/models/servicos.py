# HareSync/app/models/servico.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from . import Base  

class Servico(Base):
    __tablename__ = 'HSSV'

    codigo_servico = Column(Integer, primary_key=True, autoincrement=True)
    codigo_contrato = Column(String(50), ForeignKey('HSCT.codigo_contrato')) 
    nome_servico = Column(String(100))
    valor_servico = Column(Float)

    def __repr__(self):
        return f"<Servico(codigo_servico='{self.codigo_servico}', nome_servico='{self.nome_servico}', valor_servico={self.valor_servico})>"
