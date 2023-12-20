from .views import CreateUser

from rest_framework import routers

routeur = routers.DefaultRouter()
routeur.register('accounts', CreateUser, basename='accounts')
