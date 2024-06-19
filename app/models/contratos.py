from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from ..db.models_base import Base

class Contrato(Base):
    __tablename__ = 'HSCT'

    codigo_contrato = Column(String(50), primary_key=True)
    codigo_cliente = Column(String(20), ForeignKey('HSCL.codigo_cliente'))  
    tipo_contrato = Column(String(50))
    data_final_contrato = Column(Date)
    valor_contrato = Column(Float)
    pagamento = Column(String(50))

