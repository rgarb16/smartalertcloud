# -*- coding: utf-8 -*-

from app import app

if __name__ == '__main__':
    # Running app in debug mode
    app.run(debug=True,host='0.0.0.0',port=80)
