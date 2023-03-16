from puupee-api.paths.api_feature_management_features.get import ApiForget
from puupee-api.paths.api_feature_management_features.put import ApiForput
from puupee-api.paths.api_feature_management_features.delete import ApiFordelete


class ApiFeatureManagementFeatures(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
