from mweb import Controller
from mweb_crud import mweb_paginate_endpoint, mweb_upload_endpoint, mweb_endpoint
from mweb_crud.crud import RequestContext
from rest_app.dto.person_dto import PersonCreateDTO, PersonUploadDTO, PersonDetailsDTO

controller_url = "/api/v1/rest"
rest_api_controller = Controller(
    name="rest_api_controller",
    url=controller_url
)

request_context = RequestContext()


@rest_api_controller.route("/create", methods=['POST'])
@mweb_endpoint(request_obj=PersonCreateDTO, mweb_message_response=True)
async def create():
    json_body = await request_context.get_json_body()
    validator = PersonDetailsDTO()
    data = await request_context.get_data(validator=validator)
    print(json_body)
    return data


@rest_api_controller.route("/details/<int:model_id>", methods=['GET'])
@mweb_endpoint(request_obj=PersonCreateDTO, mweb_message_response=True)
async def details(model_id: int):
    pass


@rest_api_controller.route("/update", methods=['POST'])
@mweb_endpoint(request_obj=PersonCreateDTO, mweb_message_response=True)
async def update():
    pass


@rest_api_controller.route("/delete/<int:model_id>", methods=['DELETE'])
@mweb_endpoint()
async def delete(model_id: int):
    pass


@rest_api_controller.route("/upload", methods=['POST'])
@mweb_upload_endpoint(request_obj=PersonUploadDTO, mweb_message_response=True)
async def upload():
    pass


@rest_api_controller.route("/read-all", methods=['GET'])
@mweb_paginate_endpoint(response_obj=PersonDetailsDTO)
async def read_all():
    return []
