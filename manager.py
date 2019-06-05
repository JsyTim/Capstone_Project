# -*- coding: utf-8 -*-
from application import app, manager
from flask_script import Server
# from jobs.launcher import runJob
import www # add all routers in entrance

##server entrance
manager.add_command("runserver", Server(host='192.168.56.1', port=app.config['SERVER_PORT'],\
                                         use_debugger=False, use_reloader=True))

#job entrance
# manager.add_command('runjob', runJob())


def main():
    manager.run()


if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()