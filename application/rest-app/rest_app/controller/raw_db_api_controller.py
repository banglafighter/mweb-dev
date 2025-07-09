from mweb import Controller
from mweb_crud import mweb_paginate_endpoint, mweb_upload_endpoint, mweb_endpoint
from rest_app.dto.person_dto import PersonCreateDTO, PersonUploadDTO, PersonDetailsDTO
from rest_app.model.author import Author

controller_url = "/api/v1/raw-db"
raw_db_api_controller = Controller(
    name="raw_db_api_controller",
    url=controller_url
)


@raw_db_api_controller.route("/save", methods=['POST', 'GET'])
@mweb_endpoint(request_obj=PersonCreateDTO, mweb_message_response=True)
async def save():
    auther = await Author(name="Touhid Mia").save()
    return "Response"


@raw_db_api_controller.route("/details/<int:model_id>", methods=['GET'])
@mweb_endpoint(request_obj=PersonCreateDTO, mweb_message_response=True)
async def details(model_id: int):
    pass


@raw_db_api_controller.route("/update", methods=['POST'])
@mweb_endpoint(request_obj=PersonCreateDTO, mweb_message_response=True)
async def update():
    pass


@raw_db_api_controller.route("/delete/<int:model_id>", methods=['DELETE'])
@mweb_endpoint()
async def delete(model_id: int):
    pass


@raw_db_api_controller.route("/upload", methods=['POST'])
@mweb_upload_endpoint(request_obj=PersonUploadDTO, mweb_message_response=True)
async def upload():
    pass


@raw_db_api_controller.route("/read-all", methods=['GET'])
@mweb_paginate_endpoint(response_obj=PersonDetailsDTO)
async def read_all():
    return []
