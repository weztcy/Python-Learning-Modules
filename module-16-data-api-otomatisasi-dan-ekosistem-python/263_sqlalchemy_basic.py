from sqlalchemy import Column, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Session


class Base(DeclarativeBase):
    pass


class Siswa(Base):
    __tablename__ = "siswa"
    id = Column(Integer, primary_key=True)
    nama = Column(String, nullable=False)


# SQLite in-memory memungkinkan ORM diuji tanpa file database.
engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)
with Session(engine) as sesi:
    sesi.add(Siswa(nama="Ayu"))
    sesi.commit()
    print("Nama:", sesi.scalars(select(Siswa.nama)).all())