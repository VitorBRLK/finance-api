from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração da URL de conexão com PostgreSQL
# Substitua com suas credenciais
DATABASE_URL = "postgresql://postgres:admin@localhost:5432/finance-api"

# Cria o engine (conexão com o banco)
engine = create_engine(DATABASE_URL)

# Cria a sessão do banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos (classes do SQLAlchemy)
Base = declarative_base()

# Dependência para usar nos endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()