from run import db, User, Role

SQLALCHEMY_TRACK_MODIFICATIONS = True
extend_existing = True


# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#
#     def __repr__(self):
#         return '<Role %r>' % self.name
#
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), unique=True, index=True)
#
#     def __repr__(self):
#         return '<User %r>' % self.username
# db.drop_all()
# admin_role = Role(name='Admin')
# mod_role = Role(name='Moderator')
# user_role = Role(name='User')
# user_john = User(username='john', role=admin_role)
# user_susan = User(username='susan', role=user_role)
# user_david = User(username='david', role=user_role)
# db.session.add(admin_role)
# db.session.add(mod_role)
# db.session.add(user_role)
# db.session.add(user_john)
# db.session.add(user_susan)
# db.session.add(user_david)
db.create_all()
