from puupee-api.paths.api_app_message_template_id.get import ApiForget
from puupee-api.paths.api_app_message_template_id.put import ApiForput
from puupee-api.paths.api_app_message_template_id.delete import ApiFordelete


class ApiAppMessageTemplateId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
