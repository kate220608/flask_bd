from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    #app.run()
    db_sess = db_session.create_session()
    for el in [['Scott', 'Ridley', 21, 'captain', 'research engineer', 'module_1', 'scott_chief@mars.org'],
               ['Sggt', 'Rggy', 44, 'cafffn', 'engineer', 'module6', 'sfrggf@mars.org'],
               ['Antobu', 'Fake', 20, 'dmdnv', 'researcer', 'module_9', 'adsf@mars.org'],
               ['Emma', 'Ridley', 30, 'cooker', 'doctor', 'module_18', 'ghghg@mars.org']]:
        user = User()
        user.surname = el[0]
        user.name = el[1]
        user.age = el[2]
        user.position = el[3]
        user.speciality = el[4]
        user.address = el[5]
        user.email = el[6]
        db_sess.add(user)
        db_sess.commit()


if __name__ == '__main__':
    main()