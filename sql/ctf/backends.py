from django.contrib.auth.backends import BaseBackend
from django.db import connection
from django.contrib.auth.models import User

class RawSQLBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        with connection.cursor() as cursor:
            query = "SELECT * FROM auth_user WHERE username = '" + username + "' AND password = '" + password + "';"
            print(query)
            cursor.execute(query)
            row = cursor.fetchone()
            if row:
                return User.objects.get(pk=row[0])

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None