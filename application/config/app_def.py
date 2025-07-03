from mweb.engine.mweb_connector import MWebAppDefinition
from rest_app.rest_app_module import RestAppModule


class AppDef(MWebAppDefinition):

    def register_modules(self) -> list:
        return [
            RestAppModule
        ]
