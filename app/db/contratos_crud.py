from sqlalchemy.orm import Session
from ..models.contratos import Contrato


def get_contratos(db: Session):
    return db.query(Contrato).all()


def get_contrato_by_id(db: Session, codigo_contrato: str):
    return db.query(Contrato).filter(Contrato.codigo_contrato == codigo_contrato).first()


def create_contrato(db: Session, contrato: Contrato):
    db.add(contrato)
    db.commit()
    db.refresh(contrato)
    return contrato

def update_contrato(db: Session, codigo_contrato: str, codigo_cliente: str, tipo_contrato: str, data_final_contrato: Date, valor_contrato: float, pagamento: str):
    contrato = db.query(Contrato).filter(Contrato.codigo_contrato == codigo_contrato).first()
    if contrato:
        contrato.codigo_cliente = codigo_cliente
        contrato.tipo_contrato = tipo_contrato
        contrato.data_final_contrato = data_final_contrato
        contrato.valor_contrato = valor_contrato
        contrato.pagamento = pagamento
        db.commit()
        db.refresh(contrato)
    return contrato

def delete_contrato(db: Session, codigo_contrato: str):
    contrato = db.query(Contrato).filter(Contrato.codigo_contrato == codigo_contrato).first()
    if contrato:
        db.delete(contrato)
        db.commit()
    return contrato
