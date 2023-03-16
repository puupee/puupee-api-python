from puupee-api.paths.api_identity_roles_id.get import ApiForget
from puupee-api.paths.api_identity_roles_id.put import ApiForput
from puupee-api.paths.api_identity_roles_id.delete import ApiFordelete


class ApiIdentityRolesId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
