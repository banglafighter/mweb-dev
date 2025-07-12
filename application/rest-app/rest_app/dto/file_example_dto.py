from mweb_crud.data_transfer import MWebDTO, dto
from rest_app.model.file_example import FileExample


class UploadAnyFileDTO(MWebDTO):
    anyFile = dto.File(required=True, error_messages={"required": "Please enter any kind of file"})

    class Meta:
        model = FileExample



class UploadPDFFileDTO(MWebDTO):
    pdfFile = dto.File(required=True, error_messages={"required": "Please enter PDF File"}).set_allowed_extension(["pdf"])

    class Meta:
        model = FileExample



class UploadDocFileDTO(MWebDTO):
    docFile = dto.File(required=True, error_messages={"required": "Please enter Document File"}).set_allowed_extension(["doc", "docx", "xlsx"])

    class Meta:
        model = FileExample



class UploadArchiveFileDTO(MWebDTO):
    archiveFile = dto.File(required=True, error_messages={"required": "Please enter Archive File"}).set_allowed_extension(["zip", "7z"])

    class Meta:
        model = FileExample



class UploadImageFileDTO(MWebDTO):
    imageFile = dto.File(required=True, error_messages={"required": "Please enter Image File"}).set_allowed_extension(["jpg", "png", "jpeg"])

    class Meta:
        model = FileExample



class UploadCustomNameFileDTO(MWebDTO):
    customNameFile = dto.File(required=True, error_messages={"required": "Please enter any kind of file"})

    class Meta:
        model = FileExample



class UploadPrefixNameFileDTO(MWebDTO):
    anyFile = dto.File(required=True, error_messages={"required": "Please enter any kind of file"}).set_save_prefix("prefix")

    class Meta:
        model = FileExample



class UploadSizedFileDTO(MWebDTO):
    anyFile = dto.File(required=True, error_messages={"required": "Please enter file less than 100KB"}).set_max_size_kb(100)

    class Meta:
        model = FileExample



class DataAndUploadFileDTO(MWebDTO):
    anyFile = dto.File(required=True, error_messages={"required": "Please enter any kind of file"})
    alterText = dto.String(required=True, error_messages={"required": "Please enter alter text"})
    title = dto.String(allow_none=True)

    class Meta:
        model = FileExample

