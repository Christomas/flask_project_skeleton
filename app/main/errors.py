from flask import render_template

from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    error = '{}：您访问的页面不知所踪……'.format(e.code)
    return render_template('simple_message.html', message=error), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    error = '{}：服务器去寻找MH370了。'.format(e.code)
    return render_template('simple_message.html', message=error), 500
