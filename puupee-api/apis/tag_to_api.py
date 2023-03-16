import typing_extensions

from puupee-api.apis.tags import TagValues
from puupee-api.apis.tags.abp_api_definition_api import AbpApiDefinitionApi
from puupee-api.apis.tags.abp_application_configuration_api import AbpApplicationConfigurationApi
from puupee-api.apis.tags.abp_application_localization_api import AbpApplicationLocalizationApi
from puupee-api.apis.tags.abp_tenant_api import AbpTenantApi
from puupee-api.apis.tags.account_api import AccountApi
from puupee-api.apis.tags.app_api import AppApi
from puupee-api.apis.tags.app_feature_api import AppFeatureApi
from puupee-api.apis.tags.app_pricing_api import AppPricingApi
from puupee-api.apis.tags.app_pricing_item_api import AppPricingItemApi
from puupee-api.apis.tags.app_release_api import AppReleaseApi
from puupee-api.apis.tags.app_sdk_api import AppSdkApi
from puupee-api.apis.tags.app_user_score_api import AppUserScoreApi
from puupee-api.apis.tags.device_api import DeviceApi
from puupee-api.apis.tags.email_settings_api import EmailSettingsApi
from puupee-api.apis.tags.features_api import FeaturesApi
from puupee-api.apis.tags.key_value_api import KeyValueApi
from puupee-api.apis.tags.login_api import LoginApi
from puupee-api.apis.tags.permissions_api import PermissionsApi
from puupee-api.apis.tags.profile_api import ProfileApi
from puupee-api.apis.tags.puupee_api import PuupeeApi
from puupee-api.apis.tags.role_api import RoleApi
from puupee-api.apis.tags.settings_api import SettingsApi
from puupee-api.apis.tags.simple_data_api import SimpleDataApi
from puupee-api.apis.tags.storage_object_api import StorageObjectApi
from puupee-api.apis.tags.subscription_api import SubscriptionApi
from puupee-api.apis.tags.sync_state_api import SyncStateApi
from puupee-api.apis.tags.tenant_api import TenantApi
from puupee-api.apis.tags.test_api import TestApi
from puupee-api.apis.tags.user_api import UserApi
from puupee-api.apis.tags.user_lookup_api import UserLookupApi
from puupee-api.apis.tags.user_storage_api import UserStorageApi
from puupee-api.apis.tags.verification_api import VerificationApi

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
        TagValues.APP_PRICING: AppPricingApi,
        TagValues.APP_PRICING_ITEM: AppPricingItemApi,
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
        TagValues.SUBSCRIPTION: SubscriptionApi,
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
        TagValues.APP_PRICING: AppPricingApi,
        TagValues.APP_PRICING_ITEM: AppPricingItemApi,
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
        TagValues.SUBSCRIPTION: SubscriptionApi,
        TagValues.SYNC_STATE: SyncStateApi,
        TagValues.TENANT: TenantApi,
        TagValues.TEST: TestApi,
        TagValues.USER: UserApi,
        TagValues.USER_LOOKUP: UserLookupApi,
        TagValues.USER_STORAGE: UserStorageApi,
        TagValues.VERIFICATION: VerificationApi,
    }
)
