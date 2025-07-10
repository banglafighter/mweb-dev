from mweb import Controller
from mweb_crud import mweb_endpoint
from mweb_crud.common import MWebCRUDException

controller_url = "/api/v1/exception"
exception_api_controller = Controller(
    name="exception_api_controller",
    url=controller_url
)


@exception_api_controller.route("/error", methods=['GET'])
@mweb_endpoint(mweb_message_response=True)
async def error():
    raise MWebCRUDException(message="Error Message")
