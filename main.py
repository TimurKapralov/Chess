from flask import redirect, render_template, Flask
from data.login import LoginForm
from forms.user import RegisterForm
from data.users import User
from data import db_session
from flask_login import LoginManager, login_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    formm = RegisterForm()
    if formm.validate_on_submit():
        if formm.password.data != formm.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=formm,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == formm.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=formm,
                                   message="Такой пользователь уже есть")
        user = User(
            name=formm.name.data,
            email=formm.email.data,
            surname=formm.surname.data,
            clas=formm.clas.data
        )
        user.set_password(formm.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=formm)


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')