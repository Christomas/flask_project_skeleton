from flask import Blueprint


# 定义蓝图
main = Blueprint('main', __name__)

from . import views, errors
