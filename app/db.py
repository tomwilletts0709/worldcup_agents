from sqlalcemy import create_engine

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(DATABASE_URL) 

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

