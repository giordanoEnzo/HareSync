from sqlalchemy.orm import Session
from ..models.funcionario import Funcionario


def get_funcionarios(db: Session):
    return db.query(Funcionario).all()


def get_funcionario_by_id(db: Session, codigo_funcionario: int):
    return db.query(Funcionario).filter(Funcionario.codigo_funcionario == codigo_funcionario).first()


def create_funcionario(db: Session, funcionario: Funcionario):
    db.add(funcionario)
    db.commit()
    db.refresh(funcionario)
    return funcionario


def update_funcionario(db: Session, codigo_funcionario: int, nome_funcionario: str, cpf: str, email: str, senha: str, telefone: str, cargo: str, empresa: str):
    funcionario = db.query(Funcionario).filter(Funcionario.codigo_funcionario == codigo_funcionario).first()
    if funcionario:
        funcionario.nome_funcionario = nome_funcionario
        funcionario.cpf = cpf
        funcionario.email = email
        funcionario.senha = senha
        funcionario.telefone = telefone
        funcionario.cargo = cargo
        funcionario.empresa = empresa
        db.commit()
        db.refresh(funcionario)
    return funcionario


def delete_funcionario(db: Session, codigo_funcionario: int):
    funcionario = db.query(Funcionario).filter(Funcionario.codigo_funcionario == codigo_funcionario).first()
    if funcionario:
        db.delete(funcionario)
        db.commit()
    return funcionario
