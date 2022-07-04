from src.modelo.asignatura import Asignatura
from src.modelo.declarative_base import engine, Base, session

class editAsignatura():

    def __init__(self):
        Base.metadata.create_all(engine)

    def editar_asignatura(self, nombreAsignatura, nombreDocente):

        if (len(nombreAsignatura) and len(nombreDocente))==0:
            return False
        busqueda = session.query(Asignatura).filter(Asignatura.nombreAsignatura == nombreAsignatura and Asignatura.nombreDocente == nombreDocente).all()
        if len(busqueda) == 0:
            asignatura = session.query(Asignatura).get(2)
            asignatura1 = Asignatura(nombreAsignatura=nombreAsignatura, nombreDocente=nombreDocente)
            session.add(asignatura1)
            session.delete(asignatura)
            session.commit()
            return True
        else:
            return False
