import os
from app import create_app, db
from app.model import User, Role
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)
#
#
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
#
#
# manager.add_command("shell", Shell(make_context=make_shell_context))
# manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    # manager.run()
    app.run()

@manager.command
def test():
    """Run unitest"""
    import unittest
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(test)
