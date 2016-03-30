from functools import partial

from . import db

# 定义字段wrapper，默认非空
Column = partial(db.Column, nullable=False)
# 定义字段wrapper，默认为空
NullColumn = partial(db.Column, nullable=True)
# 定义关系wrapper，默认dynamic
relationship = partial(db.relationship, lazy='dynamic')


# 定义通用模型类
class Model(db.Model):
    __abstract__ = True

    def __str__(self):
        try:
            return self.name
        except ValueError:
            return super().__str__(self)

    @property
    def session(self):
        return db.session
