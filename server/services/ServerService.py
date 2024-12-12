from loguru import logger

from server.dto.ServerDTO import TemplateRequest, TemplateResponse


class ServerService:
    def __init__(self):
        self.template_response = "template"

    def create_template(self, request: TemplateRequest):
        logger.info(f"Creating template: {request=}")
        return TemplateResponse(template=self.template_response)

    def get_template(self):
        logger.info("Get template")
        return TemplateResponse(template=self.template_response)
