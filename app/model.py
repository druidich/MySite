from app import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


# user = User.query.filter_by(username='John').first()
# print(user)
# db.drop_all()
# db.create_all()
# admin_role = Role(name='Admin')
# mod_role = Role(name='Moderator')
# user_role = Role(name='User')
# user_john = User(username='John', role =user_role)
# db.session.add(admin_role)
# db.session.add(mod_role)
# db.session.add(user_role)
# db.session.add(user_john)
# db.session.commit()
#
# print(str(user_role.users.order_by(User.username).all()))
# print(str(Role.query.all()))
