from models import Base, Link
from db import engine

if __name__ == "__main__":
    # Base.metadata.create_all(engine)
    print(Base.metadata.tables.keys())


