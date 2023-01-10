import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.abp_api_definition_api import AbpApiDefinitionApi
from openapi_client.apis.tags.abp_application_configuration_api import AbpApplicationConfigurationApi
from openapi_client.apis.tags.abp_application_localization_api import AbpApplicationLocalizationApi
from openapi_client.apis.tags.abp_tenant_api import AbpTenantApi
from openapi_client.apis.tags.account_api import AccountApi
from openapi_client.apis.tags.app_api import AppApi
from openapi_client.apis.tags.app_feature_api import AppFeatureApi
from openapi_client.apis.tags.app_release_api import AppReleaseApi
from openapi_client.apis.tags.app_sdk_api import AppSdkApi
from openapi_client.apis.tags.app_user_score_api import AppUserScoreApi
from openapi_client.apis.tags.device_api import DeviceApi
from openapi_client.apis.tags.email_settings_api import EmailSettingsApi
from openapi_client.apis.tags.features_api import FeaturesApi
from openapi_client.apis.tags.key_value_api import KeyValueApi
from openapi_client.apis.tags.login_api import LoginApi
from openapi_client.apis.tags.permissions_api import PermissionsApi
from openapi_client.apis.tags.profile_api import ProfileApi
from openapi_client.apis.tags.puupee_api import PuupeeApi
from openapi_client.apis.tags.role_api import RoleApi
from openapi_client.apis.tags.settings_api import SettingsApi
from openapi_client.apis.tags.simple_data_api import SimpleDataApi
from openapi_client.apis.tags.storage_object_api import StorageObjectApi
from openapi_client.apis.tags.sync_state_api import SyncStateApi
from openapi_client.apis.tags.tenant_api import TenantApi
from openapi_client.apis.tags.test_api import TestApi
from openapi_client.apis.tags.user_api import UserApi
from openapi_client.apis.tags.user_lookup_api import UserLookupApi
from openapi_client.apis.tags.user_storage_api import UserStorageApi
from openapi_client.apis.tags.verification_api import VerificationApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ABP_API_DEFINITION: AbpApiDefinitionApi,
        TagValues.ABP_APPLICATION_CONFIGURATION: AbpApplicationConfigurationApi,
        TagValues.ABP_APPLICATION_LOCALIZATION: AbpApplicationLocalizationApi,
        TagValues.ABP_TENANT: AbpTenantApi,
        TagValues.ACCOUNT: AccountApi,
        TagValues.APP: AppApi,
        TagValues.APP_FEATURE: AppFeatureApi,
        TagValues.APP_RELEASE: AppReleaseApi,
        TagValues.APP_SDK: AppSdkApi,
        TagValues.APP_USER_SCORE: AppUserScoreApi,
        TagValues.DEVICE: DeviceApi,
        TagValues.EMAIL_SETTINGS: EmailSettingsApi,
        TagValues.FEATURES: FeaturesApi,
        TagValues.KEY_VALUE: KeyValueApi,
        TagValues.LOGIN: LoginApi,
        TagValues.PERMISSIONS: PermissionsApi,
        TagValues.PROFILE: ProfileApi,
        TagValues.PUUPEE: PuupeeApi,
        TagValues.ROLE: RoleApi,
        TagValues.SETTINGS: SettingsApi,
        TagValues.SIMPLE_DATA: SimpleDataApi,
        TagValues.STORAGE_OBJECT: StorageObjectApi,
        TagValues.SYNC_STATE: SyncStateApi,
        TagValues.TENANT: TenantApi,
        TagValues.TEST: TestApi,
        TagValues.USER: UserApi,
        TagValues.USER_LOOKUP: UserLookupApi,
        TagValues.USER_STORAGE: UserStorageApi,
        TagValues.VERIFICATION: VerificationApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ABP_API_DEFINITION: AbpApiDefinitionApi,
        TagValues.ABP_APPLICATION_CONFIGURATION: AbpApplicationConfigurationApi,
        TagValues.ABP_APPLICATION_LOCALIZATION: AbpApplicationLocalizationApi,
        TagValues.ABP_TENANT: AbpTenantApi,
        TagValues.ACCOUNT: AccountApi,
        TagValues.APP: AppApi,
        TagValues.APP_FEATURE: AppFeatureApi,
        TagValues.APP_RELEASE: AppReleaseApi,
        TagValues.APP_SDK: AppSdkApi,
        TagValues.APP_USER_SCORE: AppUserScoreApi,
        TagValues.DEVICE: DeviceApi,
        TagValues.EMAIL_SETTINGS: EmailSettingsApi,
        TagValues.FEATURES: FeaturesApi,
        TagValues.KEY_VALUE: KeyValueApi,
        TagValues.LOGIN: LoginApi,
        TagValues.PERMISSIONS: PermissionsApi,
        TagValues.PROFILE: ProfileApi,
        TagValues.PUUPEE: PuupeeApi,
        TagValues.ROLE: RoleApi,
        TagValues.SETTINGS: SettingsApi,
        TagValues.SIMPLE_DATA: SimpleDataApi,
        TagValues.STORAGE_OBJECT: StorageObjectApi,
        TagValues.SYNC_STATE: SyncStateApi,
        TagValues.TENANT: TenantApi,
        TagValues.TEST: TestApi,
        TagValues.USER: UserApi,
        TagValues.USER_LOOKUP: UserLookupApi,
        TagValues.USER_STORAGE: UserStorageApi,
        TagValues.VERIFICATION: VerificationApi,
    }
)
