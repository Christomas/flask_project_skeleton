import os

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db, models

# 初始化app manager migrate工具集
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


# 预定义上下文
def make_shell_context():
    return dict(app=app, db=db, models=models)

# 添加预定义上下文全局变量
manager.add_command('shell', Shell(make_context=make_shell_context))
# 添加数据库迁移命令
manager.add_command('db', MigrateCommand)


# 添加单元测试命令
@manager.command
def test():
    """进行单元测试"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
