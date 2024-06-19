# HareSync/app/models/contrato.py

from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from . import Base  

class Contrato(Base):
    __tablename__ = 'HSCT'

    codigo_contrato = Column(String(50), primary_key=True)
    codigo_cliente = Column(String(20), ForeignKey('HSCL.codigo_cliente'))  
    tipo_contrato = Column(String(50))
    data_final_contrato = Column(Date)
    valor_contrato = Column(Float)
    pagamento = Column(String(50))

    def __repr__(self):
        return f"<Contrato(codigo_contrato='{self.codigo_contrato}', tipo_contrato='{self.tipo_contrato}', valor_contrato={self.valor_contrato})>"
