from puupee-api.paths.api_identity_users_id.get import ApiForget
from puupee-api.paths.api_identity_users_id.put import ApiForput
from puupee-api.paths.api_identity_users_id.delete import ApiFordelete


class ApiIdentityUsersId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
