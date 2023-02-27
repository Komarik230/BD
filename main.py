from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    user.hashed_password = "cap"

    user1 = User()
    user1.surname = "Scott"
    user1.name = "Warter"
    user1.age = 24
    user1.position = "engineer"
    user1.speciality = "search engineer"
    user1.address = "module_21"
    user1.email = "scott_warter@mars.org"
    user1.hashed_password = "scott"

    user2 = User()
    user2.surname = "Scott"
    user2.name = "Warter"
    user2.age = 10
    user2.position = "engineer"
    user2.speciality = "doctor"
    user2.address = "module_22"
    user2.email = "scott_warter111111111@mars.org"
    user2.hashed_password = "23ekbr"

    user3 = User()
    user3.surname = "Meow"
    user3.name = "Warter"
    user3.age = 19
    user3.position = "engineer"
    user3.speciality = "search engineer"
    user3.address = "module_23"
    user3.email = "scott_warter11@mars.org"
    user3.hashed_password = "help"

    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.add(user1)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()