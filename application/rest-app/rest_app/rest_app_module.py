from mw_common.mw_console_log import Console
from mweb.engine.mweb_base import MWebBase
from mweb.engine.mweb_config import MWebConfig
from mweb.engine.mweb_connector import MWebModule
from mweb.engine.mweb_data import MWebModuleDetails
from mweb.engine.mweb_hook import MWebHook


class RestAppModule(MWebModule):

    def register_module(self) -> MWebModuleDetails:
        return MWebModuleDetails(systemName="rest-app", displayName="REST Application")

    def initialize(self, mweb_app: MWebBase, config: MWebConfig, hook: MWebHook, **kwargs):
        Console.log("Initializing MWeb Module")

    def register_model(self, mweb_db) -> list:
        Console.log("Registering MWeb Model")

    def register_controller(self, mweb_app: MWebBase):
        Console.log("Registering MWeb Controller")

    def run_on_start(self, mweb_app: MWebBase, config: MWebConfig):
        Console.log("Running MWeb Module")

    def run_on_cli_init(self, mweb_app: MWebBase, config: MWebConfig):
        Console.log("Running MWeb Module")
