from django.apps import AppConfig


class StockappConfig(AppConfig):
    name = 'stockapp'
    
    def ready(self):
        from updater import update
        update.start()