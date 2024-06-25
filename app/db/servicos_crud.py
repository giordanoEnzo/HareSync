from sqlalchemy.orm import Session
from ..models.servicos import Servico


def get_servicos(db: Session):
    return db.query(Servico).all()


def get_servico_by_id(db: Session, codigo_servico: int):
    return db.query(Servico).filter(Servico.codigo_servico == codigo_servico).first()
def create_servico(db: Session, servico: Servico):
    db.add(servico)
    db.commit()
    db.refresh(servico)
    return servico

def update_servico(db: Session, codigo_servico: int, codigo_contrato: str, nome_servico: str, valor_servico: float):
    servico = db.query(Servico).filter(Servico.codigo_servico == codigo_servico).first()
    if servico:
        servico.codigo_contrato = codigo_contrato
        servico.nome_servico = nome_servico
        servico.valor_servico = valor_servico
        db.commit()
        db.refresh(servico)
    return servico


def delete_servico(db: Session, codigo_servico: int):
    servico = db.query(Servico).filter(Servico.codigo_servico == codigo_servico).first()
    if servico:
        db.delete(servico)
        db.commit()
    return servico
