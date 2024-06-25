from sqlalchemy.orm import Session
from ..models.cliente import Cliente

def get_clientes(db: Session):
    return db.query(Cliente).all()

def get_cliente_by_id(db: Session, codigo_cliente: str):
    return db.query(Cliente).filter(Cliente.codigo_cliente == codigo_cliente).first()

def create_cliente(db: Session, cliente: Cliente):
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente


def update_cliente(db: Session, codigo_cliente: str, nome_cliente: str, sigla: str, cpf_cnpj: str, senha: str, email: str, telefone: str, contrato: str):
    cliente = db.query(Cliente).filter(Cliente.codigo_cliente == codigo_cliente).first()
    if cliente:
        cliente.nome_cliente = nome_cliente
        cliente.sigla = sigla
        cliente.cpf_cnpj = cpf_cnpj
        cliente.senha = senha
        cliente.email = email
        cliente.telefone = telefone
        cliente.contrato = contrato
        db.commit()
        db.refresh(cliente)
    return cliente

def delete_cliente(db: Session, codigo_cliente: str):
    cliente = db.query(Cliente).filter(Cliente.codigo_cliente == codigo_cliente).first()
    if cliente:
        db.delete(cliente)
        db.commit()
    return cliente
