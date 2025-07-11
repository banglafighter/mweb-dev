from mweb_crud.crud import CRUDManager
from rest_app.dto.school_dto import SchoolCreateDTO, SchoolDetailsDTO
from rest_app.model.school import School


class SchoolService:
    crud_manager = CRUDManager(model=School)

    async def create(self):
        return await self.crud_manager.create(request=SchoolCreateDTO())

    async def create_response_model(self):
        return await self.crud_manager.create(request=SchoolCreateDTO(), response=SchoolDetailsDTO())
