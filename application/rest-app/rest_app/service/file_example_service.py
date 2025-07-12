from mw_file_content.file.mwfc_file_util import FileUtil
from mweb.engine.mweb_registry import MWebRegistry
from mweb_crud.crud import CRUDManager
from mweb_crud.file_upload import UploadCustomizer
from rest_app.dto.file_example_dto import DataAndUploadFileDTO, UploadSizedFileDTO, UploadPrefixNameFileDTO, \
    UploadCustomNameFileDTO, UploadImageFileDTO, UploadArchiveFileDTO, UploadDocFileDTO, UploadPDFFileDTO, \
    UploadAnyFileDTO
from rest_app.model.file_example import FileExample


class FileExampleService:
    crud_manager = CRUDManager(model=FileExample)

    @property
    def upload_path(self):
        return FileUtil.join_path(MWebRegistry.config.UPLOADED_STATIC_RESOURCES, "file-example")

    async def upload_any_file(self):
        return await self.crud_manager.create(request=UploadAnyFileDTO(), allow_files=True, upload_path=self.upload_path)

    async def data_and_upload_file(self):
        return await self.crud_manager.create(request=DataAndUploadFileDTO(), allow_files=True, upload_path=self.upload_path)

    async def upload_pdf_file(self):
        return await self.crud_manager.create(request=UploadPDFFileDTO(), allow_files=True, upload_path=self.upload_path)

    async def upload_doc_file(self):
        return await self.crud_manager.create(request=UploadDocFileDTO(), allow_files=True, upload_path=self.upload_path)

    async def upload_archive_file(self):
        return await self.crud_manager.create(request=UploadArchiveFileDTO(), allow_files=True, upload_path=self.upload_path)

    async def upload_image_file(self):
        return await self.crud_manager.create(request=UploadImageFileDTO(), allow_files=True, upload_path=self.upload_path)

    async def upload_custom_name_file(self):
        upload_customizer: UploadCustomizer = UploadCustomizer()
        upload_customizer.add_name("customNameFile", "some-file-name")
        return await self.crud_manager.create(request=UploadCustomNameFileDTO(), allow_files=True, upload_path=self.upload_path, upload_customizer=upload_customizer)

    async def upload_prefix_name_file(self):
        return await self.crud_manager.create(request=UploadPrefixNameFileDTO(), allow_files=True, upload_path=self.upload_path)

    async def upload_sized_file(self):
        return await self.crud_manager.create(request=UploadSizedFileDTO(), allow_files=True, upload_path=self.upload_path)