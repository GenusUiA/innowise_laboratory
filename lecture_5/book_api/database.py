from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Connection string
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

# Create SQLAlchemyEngine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False}
)

# Create session to connect to database
SessionLocal = sessionmaker(autoflush=False, bind = engine)