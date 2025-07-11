from mweb_crud.crud import CRUDManager
from rest_app.dto.school_dto import SchoolCreateDTO, SchoolDetailsDTO
from rest_app.model.school import School


class SchoolService:
    crud_manager = CRUDManager(model=School)

    async def create(self):
        return await self.crud_manager.create(request=SchoolCreateDTO())

    async def create_response_model(self):
        return await self.crud_manager.create(request=SchoolCreateDTO(), response=SchoolDetailsDTO())

    async def details(self, record_id: int):
        return await self.crud_manager.details(record_id=record_id, response=SchoolDetailsDTO())

    async def read_all(self):
        search_fields: list = ["name", "email", "location"]
        return await self.crud_manager.paginated_read_all(response=SchoolDetailsDTO(), search_fields=search_fields)

    async def delete(self, record_id: int):
        return await self.crud_manager.delete(record_id=record_id)
