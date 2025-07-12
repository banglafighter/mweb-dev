from mweb import Controller
from mweb_crud import mweb_upload_endpoint
from rest_app.dto.file_example_dto import UploadAnyFileDTO, UploadPDFFileDTO, UploadDocFileDTO, UploadArchiveFileDTO, \
    UploadImageFileDTO, UploadCustomNameFileDTO, UploadPrefixNameFileDTO, UploadSizedFileDTO, DataAndUploadFileDTO
from rest_app.service.file_example_service import FileExampleService

controller_url = "/api/v1/file-holder"
file_example_api_controller = Controller(
    name="file_example_api_controller",
    url=controller_url
)


file_example_service = FileExampleService()


@file_example_api_controller.route("/upload-any-file", methods=['POST'])
@mweb_upload_endpoint(request_obj=UploadAnyFileDTO, mweb_message_response=True)
async def upload_any_file():
    return await file_example_service.upload_any_file()


@file_example_api_controller.route("/upload-pdf-file", methods=['POST'])
@mweb_upload_endpoint(request_obj=UploadPDFFileDTO, mweb_message_response=True)
async def upload_pdf_file():
    return await file_example_service.upload_pdf_file()


@file_example_api_controller.route("/upload-doc-file", methods=['POST'])
@mweb_upload_endpoint(request_obj=UploadDocFileDTO, mweb_message_response=True)
async def upload_doc_file():
    return await file_example_service.upload_doc_file()


@file_example_api_controller.route("/upload-archive-file", methods=['POST'])
@mweb_upload_endpoint(request_obj=UploadArchiveFileDTO, mweb_message_response=True)
async def upload_archive_file():
    return await file_example_service.upload_archive_file()


@file_example_api_controller.route("/upload-image-file", methods=['POST'])
@mweb_upload_endpoint(request_obj=UploadImageFileDTO, mweb_message_response=True)
async def upload_image_file():
    return await file_example_service.upload_image_file()


@file_example_api_controller.route("/upload-custom-name-file", methods=['POST'])
@mweb_upload_endpoint(request_obj=UploadCustomNameFileDTO, mweb_message_response=True)
async def upload_custom_name_file():
    return await file_example_service.upload_custom_name_file()


@file_example_api_controller.route("/upload-prefix-name-file", methods=['POST'])
@mweb_upload_endpoint(request_obj=UploadPrefixNameFileDTO, mweb_message_response=True)
async def upload_prefix_name_file():
    return await file_example_service.upload_prefix_name_file()


@file_example_api_controller.route("/upload-sized-file", methods=['POST'])
@mweb_upload_endpoint(request_obj=UploadSizedFileDTO, mweb_message_response=True)
async def upload_sized_file():
    return await file_example_service.upload_sized_file()


@file_example_api_controller.route("/data-and-upload-file", methods=['POST'])
@mweb_upload_endpoint(request_obj=DataAndUploadFileDTO, mweb_message_response=True)
async def data_and_upload_file():
    return await file_example_service.data_and_upload_file()
