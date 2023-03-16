from puupee-api.paths.api_app_app_id.get import ApiForget
from puupee-api.paths.api_app_app_id.put import ApiForput
from puupee-api.paths.api_app_app_id.delete import ApiFordelete


class ApiAppAppId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
