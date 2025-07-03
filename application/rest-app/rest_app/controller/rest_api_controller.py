from mweb import Controller

controller_url = "/api/v1/rest"
rest_api_controller = Controller(
    name="rest_api_controller",
    url=controller_url
)


@rest_api_controller.route("/create", methods=['POST'])
async def create():
    pass


@rest_api_controller.route("/details/<int:model_id>", methods=['GET'])
async def details(model_id: int):
    pass


@rest_api_controller.route("/update", methods=['POST'])
async def update():
    pass


@rest_api_controller.route("/delete/<int:model_id>", methods=['DELETE'])
async def delete(model_id: int):
    pass


@rest_api_controller.route("/upload", methods=['POST'])
async def upload():
    pass


@rest_api_controller.route("/read-all", methods=['GET'])
async def read_all():
    return []
