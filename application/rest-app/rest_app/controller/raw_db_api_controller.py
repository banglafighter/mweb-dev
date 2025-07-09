from mw_common.mw_console_log import Console
from mweb import Controller
from mweb_crud import mweb_paginate_endpoint, mweb_upload_endpoint, mweb_endpoint
from rest_app.dto.person_dto import PersonCreateDTO, PersonUploadDTO, PersonDetailsDTO
from rest_app.model.author import Author
from mweb_orm import and_

controller_url = "/api/v1/raw-db"
raw_db_api_controller = Controller(
    name="raw_db_api_controller",
    url=controller_url
)


@raw_db_api_controller.route("/save", methods=['POST', 'GET'])
@mweb_endpoint(mweb_message_response=True)
async def save():
    author = Author(name="Touhid Mia")
    if author.is_saved():
        Console.log("Before Saved")

    auther = await author.save()
    if author.is_saved():
        return "Saved successfully"

    return "Unable to save successfully"


@raw_db_api_controller.route("/save-all", methods=['POST', 'GET'])
@mweb_endpoint(mweb_message_response=True)
async def save_all():
    authos = []
    for index in range(0, 20):
        author = Author(name=f"Author Name #{index}")
        authos.append(author)
    await Author.save_all(authos)

    return "Saved all"


@raw_db_api_controller.route("/read-all", methods=['POST', 'GET'])
@mweb_endpoint(mweb_message_response=True)
async def read_all():
    result = await Author.query.read_all()
    print(result)
    result2 = await Author.select(Author.name).read_all()
    single = await Author.query.where(
        and_(Author.id == 10)
    ).first()
    print(single)

    count = await Author.query.count()
    print(count)

    conditional_count = await Author.query.where(Author.id > 500).count()
    print(conditional_count)

    pagination = await Author.query.paginate()
    print(f"Item Count: {len(pagination.items)}")
    print(pagination)

    pagination = await Author.query.paginate(item_per_page=-1)
    print(f"Item Count: {len(pagination.items)}")
    print(pagination)

    return "Read all"


@raw_db_api_controller.route("/details/<int:model_id>", methods=['GET'])
@mweb_endpoint(mweb_message_response=True)
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
