from mweb import Controller
from mweb_crud import mweb_endpoint
from rest_app.dto.school_dto import SchoolCreateDTO, SchoolDetailsDTO
from rest_app.service.school_service import SchoolService

controller_url = "/api/v1/school"
school_api_controller = Controller(
    name="school_api_controller",
    url=controller_url
)

school_service = SchoolService()


@school_api_controller.route("/create", methods=['POST'])
@mweb_endpoint(request_obj=SchoolCreateDTO, mweb_message_response=True)
async def create():
    return await school_service.create()


@school_api_controller.route("/create-response-model", methods=['POST'])
@mweb_endpoint(request_obj=SchoolCreateDTO, response_obj=SchoolDetailsDTO)
async def create_response_model():
    return await school_service.create_response_model()


@school_api_controller.route("/details/<int:model_id>", methods=['GET'])
@mweb_endpoint(response_obj=SchoolDetailsDTO)
async def details(model_id: int):
    return await school_service.details(model_id=model_id)
