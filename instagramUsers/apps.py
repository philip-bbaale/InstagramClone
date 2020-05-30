from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'instagramUsers'

    def ready(self):
        import instagramUsers.signals