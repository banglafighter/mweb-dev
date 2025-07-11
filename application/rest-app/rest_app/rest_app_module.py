from mw_common.mw_console_log import Console
from mweb.engine.mweb_base import MWebBase
from mweb.engine.mweb_config import MWebConfig
from mweb.engine.mweb_connector import MWebModule
from mweb.engine.mweb_data import MWebModuleDetails
from mweb.engine.mweb_hook import MWebHook
from rest_app.controller.exception_api_controller import exception_api_controller
from rest_app.controller.raw_db_api_controller import raw_db_api_controller
from rest_app.controller.rest_api_controller import rest_api_controller
from rest_app.controller.school_api_controller import school_api_controller
from rest_app.model.author import Author
from rest_app.model.book import Book
from rest_app.model.operator import Operator
from rest_app.model.school import School


class RestAppModule(MWebModule):

    def register_module(self) -> MWebModuleDetails:
        return MWebModuleDetails(systemName="rest-app", displayName="REST Application")

    def initialize(self, mweb_app: MWebBase, config: MWebConfig, hook: MWebHook, **kwargs):
        Console.log("Initializing MWeb Module")
        Console.log(__name__)

    def register_model(self, mweb_db) -> list:
        Console.log("Registering MWeb Model")
        return [
            School,
            Author,
            Operator,
            Book
        ]

    def register_controller(self, mweb_app: MWebBase):
        Console.log("Registering MWeb Controller")
        mweb_app.register_controller(school_api_controller)
        mweb_app.register_controller(rest_api_controller)
        mweb_app.register_controller(raw_db_api_controller)
        mweb_app.register_controller(exception_api_controller)

    def run_on_start(self, mweb_app: MWebBase, config: MWebConfig):
        Console.log("Running MWeb Module")

    def run_on_cli_init(self, mweb_app: MWebBase, config: MWebConfig):
        Console.log("Running MWeb Module")
