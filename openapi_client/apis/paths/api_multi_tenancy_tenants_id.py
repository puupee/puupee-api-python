from openapi_client.paths.api_multi_tenancy_tenants_id.get import ApiForget
from openapi_client.paths.api_multi_tenancy_tenants_id.put import ApiForput
from openapi_client.paths.api_multi_tenancy_tenants_id.delete import ApiFordelete


class ApiMultiTenancyTenantsId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
