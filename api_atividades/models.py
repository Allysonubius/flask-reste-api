from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationships
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db', convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Peoples(Base):
    __tablename__ = 'Peoples'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), index=True)
    age = Column(Integer)

    def __repr__(self):
        return '<Peoples {}>'.format(self.name)

    def save(self):
        db_session.add(self)
        db_session.commit()

# class Atividades(Base):
#      __tablename__ = 'Atividades'
#      id = Column(Integer, primary_key=True)
#      name = Column(Integer, ForeignKey('people.id'))
#      people = relationships("Peoples")

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()
