from models import Peoples

def insere_peoples():
    people = Peoples(nome = 'Allyson', idade='21')
    print(people)

def consulta_peoples():
    people = Peoples.query.filter_by(name='Allyson')
    print(people)
    people = Peoples.query.filter_by(name= 'Allyson')
    print(people)

if __name__ == '__main__':
    # insere_peoples()
    consulta_peoples()