import os
# _basedir is a trick for you to get the folder where the script runs
_basedir = os.path.abspath(os.path.dirname(__file__))

# DEBUG indicates that it is a dev environment, you'll get the very helpful error page from flask when an error occurs.
DEBUG = False

# ADMINS will be used if you need to email information to the site administrators.
# SECRET_KEY will be used to sign cookies. Change it and all your users will have to login again.
ADMINS = frozenset(['minhaz.ratul@gmail.com'])
SECRET_KEY = 'This string will be replaced with a proper key in production.'


# SQLALCHEMY_DATABASE_URI and DATABASE_CONNECT_OPTIONS are SQLAlchemy connection options (hard to guess)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

# THREADS_PER_PAGE my understanding was 2/core... might be wrong :)
THREADS_PER_PAGE = 8

# WTF_CSRF_ENABLED and WTF_CSRF_SECRET_KEY are protecting against form post fraud
WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = "somethingimpossibletoguess"

# RECAPTCHA_* WTForms comes with a RecaptchaField ready to use... just need to go to recaptcha website and get your public and private key.
RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_OPTIONS = {'theme': 'white'}
