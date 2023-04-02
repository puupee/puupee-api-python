import typing_extensions

from puupee-api.paths import PathValues
from puupee-api.apis.paths.api_abp_api_definition import ApiAbpApiDefinition
from puupee-api.apis.paths.api_abp_application_configuration import ApiAbpApplicationConfiguration
from puupee-api.apis.paths.api_abp_application_localization import ApiAbpApplicationLocalization
from puupee-api.apis.paths.api_abp_multi_tenancy_tenants_by_name_name import ApiAbpMultiTenancyTenantsByNameName
from puupee-api.apis.paths.api_abp_multi_tenancy_tenants_by_id_id import ApiAbpMultiTenancyTenantsByIdId
from puupee-api.apis.paths.api_account_register import ApiAccountRegister
from puupee-api.apis.paths.api_account_send_password_reset_code import ApiAccountSendPasswordResetCode
from puupee-api.apis.paths.api_account_verify_password_reset_token import ApiAccountVerifyPasswordResetToken
from puupee-api.apis.paths.api_account_reset_password import ApiAccountResetPassword
from puupee-api.apis.paths.api_app_account import ApiAppAccount
from puupee-api.apis.paths.api_app_app import ApiAppApp
from puupee-api.apis.paths.api_app_app_id import ApiAppAppId
from puupee-api.apis.paths.api_app_app_id_with_user import ApiAppAppIdWithUser
from puupee-api.apis.paths.api_app_app_by_name import ApiAppAppByName
from puupee-api.apis.paths.api_app_app_upload_credentials import ApiAppAppUploadCredentials
from puupee-api.apis.paths.api_app_app_by_developer import ApiAppAppByDeveloper
from puupee-api.apis.paths.api_app_app_public import ApiAppAppPublic
from puupee-api.apis.paths.api_app_app_by_developer_all import ApiAppAppByDeveloperAll
from puupee-api.apis.paths.api_app_app_feature import ApiAppAppFeature
from puupee-api.apis.paths.api_app_app_feature_id import ApiAppAppFeatureId
from puupee-api.apis.paths.api_app_app_pricing import ApiAppAppPricing
from puupee-api.apis.paths.api_app_app_pricing_id import ApiAppAppPricingId
from puupee-api.apis.paths.api_app_app_pricing_by_app_id_app_id import ApiAppAppPricingByAppIdAppId
from puupee-api.apis.paths.api_app_app_pricing_item import ApiAppAppPricingItem
from puupee-api.apis.paths.api_app_app_pricing_item_id import ApiAppAppPricingItemId
from puupee-api.apis.paths.api_app_app_release import ApiAppAppRelease
from puupee-api.apis.paths.api_app_app_release_id import ApiAppAppReleaseId
from puupee-api.apis.paths.api_app_app_release_latest import ApiAppAppReleaseLatest
from puupee-api.apis.paths.api_app_app_sdk import ApiAppAppSdk
from puupee-api.apis.paths.api_app_app_sdk_id import ApiAppAppSdkId
from puupee-api.apis.paths.api_app_app_user_score import ApiAppAppUserScore
from puupee-api.apis.paths.api_app_device_bind import ApiAppDeviceBind
from puupee-api.apis.paths.api_app_device import ApiAppDevice
from puupee-api.apis.paths.api_app_device_refresh import ApiAppDeviceRefresh
from puupee-api.apis.paths.api_setting_management_emailing import ApiSettingManagementEmailing
from puupee-api.apis.paths.api_setting_management_emailing_send_test_email import ApiSettingManagementEmailingSendTestEmail
from puupee-api.apis.paths.api_feature_management_features import ApiFeatureManagementFeatures
from puupee-api.apis.paths.api_app_key_value_bool import ApiAppKeyValueBool
from puupee-api.apis.paths.api_app_key_value_date_time import ApiAppKeyValueDateTime
from puupee-api.apis.paths.api_app_key_value_decimal import ApiAppKeyValueDecimal
from puupee-api.apis.paths.api_app_key_value_double import ApiAppKeyValueDouble
from puupee-api.apis.paths.api_app_key_value_int import ApiAppKeyValueInt
from puupee-api.apis.paths.api_app_key_value_string import ApiAppKeyValueString
from puupee-api.apis.paths.api_app_key_value_set_bool import ApiAppKeyValueSetBool
from puupee-api.apis.paths.api_app_key_value_set_date_time import ApiAppKeyValueSetDateTime
from puupee-api.apis.paths.api_app_key_value_set_decimal import ApiAppKeyValueSetDecimal
from puupee-api.apis.paths.api_app_key_value_set_double import ApiAppKeyValueSetDouble
from puupee-api.apis.paths.api_app_key_value_set_int import ApiAppKeyValueSetInt
from puupee-api.apis.paths.api_app_key_value_set_string import ApiAppKeyValueSetString
from puupee-api.apis.paths.api_account_login import ApiAccountLogin
from puupee-api.apis.paths.api_account_logout import ApiAccountLogout
from puupee-api.apis.paths.api_account_check_password import ApiAccountCheckPassword
from puupee-api.apis.paths.api_app_message_publish import ApiAppMessagePublish
from puupee-api.apis.paths.api_app_message_recall import ApiAppMessageRecall
from puupee-api.apis.paths.api_app_message_subscribe import ApiAppMessageSubscribe
from puupee-api.apis.paths.api_app_message_unsubscribe import ApiAppMessageUnsubscribe
from puupee-api.apis.paths.api_app_message_template import ApiAppMessageTemplate
from puupee-api.apis.paths.api_app_message_template_id import ApiAppMessageTemplateId
from puupee-api.apis.paths.api_app_message_template_release import ApiAppMessageTemplateRelease
from puupee-api.apis.paths.api_app_message_template_release_id import ApiAppMessageTemplateReleaseId
from puupee-api.apis.paths.api_app_notification_bark_api_key_message import ApiAppNotificationBarkApiKeyMessage
from puupee-api.apis.paths.api_app_notification import ApiAppNotification
from puupee-api.apis.paths.api_app_notification_push import ApiAppNotificationPush
from puupee-api.apis.paths.api_permission_management_permissions import ApiPermissionManagementPermissions
from puupee-api.apis.paths.api_account_my_profile import ApiAccountMyProfile
from puupee-api.apis.paths.api_account_my_profile_change_password import ApiAccountMyProfileChangePassword
from puupee-api.apis.paths.api_app_puupee_pull import ApiAppPuupeePull
from puupee-api.apis.paths.api_app_puupee_push import ApiAppPuupeePush
from puupee-api.apis.paths.api_identity_roles_all import ApiIdentityRolesAll
from puupee-api.apis.paths.api_identity_roles import ApiIdentityRoles
from puupee-api.apis.paths.api_identity_roles_id import ApiIdentityRolesId
from puupee-api.apis.paths.api_app_settings import ApiAppSettings
from puupee-api.apis.paths.api_app_settings_set import ApiAppSettingsSet
from puupee-api.apis.paths.api_app_simple_data_id import ApiAppSimpleDataId
from puupee-api.apis.paths.api_app_simple_data import ApiAppSimpleData
from puupee-api.apis.paths.api_app_simple_data_save import ApiAppSimpleDataSave
from puupee-api.apis.paths.api_app_storage_object_file import ApiAppStorageObjectFile
from puupee-api.apis.paths.api_app_storage_object_thumb import ApiAppStorageObjectThumb
from puupee-api.apis.paths.api_app_storage_object_file_or_credentials import ApiAppStorageObjectFileOrCredentials
from puupee-api.apis.paths.api_app_storage_object_pre_sign_url import ApiAppStorageObjectPreSignUrl
from puupee-api.apis.paths.api_app_subscription_verify_apple import ApiAppSubscriptionVerifyApple
from puupee-api.apis.paths.api_app_sync_state import ApiAppSyncState
from puupee-api.apis.paths.api_app_sync_state_puupee_changed_eto import ApiAppSyncStatePuupeeChangedEto
from puupee-api.apis.paths.api_multi_tenancy_tenants_id import ApiMultiTenancyTenantsId
from puupee-api.apis.paths.api_multi_tenancy_tenants import ApiMultiTenancyTenants
from puupee-api.apis.paths.api_multi_tenancy_tenants_id_default_connection_string import ApiMultiTenancyTenantsIdDefaultConnectionString
from puupee-api.apis.paths.api_test_datetime import ApiTestDatetime
from puupee-api.apis.paths.api_identity_users_id import ApiIdentityUsersId
from puupee-api.apis.paths.api_identity_users import ApiIdentityUsers
from puupee-api.apis.paths.api_identity_users_id_roles import ApiIdentityUsersIdRoles
from puupee-api.apis.paths.api_identity_users_assignable_roles import ApiIdentityUsersAssignableRoles
from puupee-api.apis.paths.api_identity_users_by_username_user_name import ApiIdentityUsersByUsernameUserName
from puupee-api.apis.paths.api_identity_users_by_email_email import ApiIdentityUsersByEmailEmail
from puupee-api.apis.paths.api_identity_users_lookup_id import ApiIdentityUsersLookupId
from puupee-api.apis.paths.api_identity_users_lookup_by_username_user_name import ApiIdentityUsersLookupByUsernameUserName
from puupee-api.apis.paths.api_identity_users_lookup_search import ApiIdentityUsersLookupSearch
from puupee-api.apis.paths.api_identity_users_lookup_count import ApiIdentityUsersLookupCount
from puupee-api.apis.paths.api_app_user_storage import ApiAppUserStorage
from puupee-api.apis.paths.api_app_verification_send_code import ApiAppVerificationSendCode

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_ABP_APIDEFINITION: ApiAbpApiDefinition,
        PathValues.API_ABP_APPLICATIONCONFIGURATION: ApiAbpApplicationConfiguration,
        PathValues.API_ABP_APPLICATIONLOCALIZATION: ApiAbpApplicationLocalization,
        PathValues.API_ABP_MULTITENANCY_TENANTS_BYNAME_NAME: ApiAbpMultiTenancyTenantsByNameName,
        PathValues.API_ABP_MULTITENANCY_TENANTS_BYID_ID: ApiAbpMultiTenancyTenantsByIdId,
        PathValues.API_ACCOUNT_REGISTER: ApiAccountRegister,
        PathValues.API_ACCOUNT_SENDPASSWORDRESETCODE: ApiAccountSendPasswordResetCode,
        PathValues.API_ACCOUNT_VERIFYPASSWORDRESETTOKEN: ApiAccountVerifyPasswordResetToken,
        PathValues.API_ACCOUNT_RESETPASSWORD: ApiAccountResetPassword,
        PathValues.API_APP_ACCOUNT: ApiAppAccount,
        PathValues.API_APP_APP: ApiAppApp,
        PathValues.API_APP_APP_ID: ApiAppAppId,
        PathValues.API_APP_APP_ID_WITHUSER: ApiAppAppIdWithUser,
        PathValues.API_APP_APP_BYNAME: ApiAppAppByName,
        PathValues.API_APP_APP_UPLOADCREDENTIALS: ApiAppAppUploadCredentials,
        PathValues.API_APP_APP_BYDEVELOPER: ApiAppAppByDeveloper,
        PathValues.API_APP_APP_PUBLIC: ApiAppAppPublic,
        PathValues.API_APP_APP_BYDEVELOPERALL: ApiAppAppByDeveloperAll,
        PathValues.API_APP_APPFEATURE: ApiAppAppFeature,
        PathValues.API_APP_APPFEATURE_ID: ApiAppAppFeatureId,
        PathValues.API_APP_APPPRICING: ApiAppAppPricing,
        PathValues.API_APP_APPPRICING_ID: ApiAppAppPricingId,
        PathValues.API_APP_APPPRICING_BYAPPID_APP_ID: ApiAppAppPricingByAppIdAppId,
        PathValues.API_APP_APPPRICINGITEM: ApiAppAppPricingItem,
        PathValues.API_APP_APPPRICINGITEM_ID: ApiAppAppPricingItemId,
        PathValues.API_APP_APPRELEASE: ApiAppAppRelease,
        PathValues.API_APP_APPRELEASE_ID: ApiAppAppReleaseId,
        PathValues.API_APP_APPRELEASE_LATEST: ApiAppAppReleaseLatest,
        PathValues.API_APP_APPSDK: ApiAppAppSdk,
        PathValues.API_APP_APPSDK_ID: ApiAppAppSdkId,
        PathValues.API_APP_APPUSERSCORE: ApiAppAppUserScore,
        PathValues.API_APP_DEVICE_BIND: ApiAppDeviceBind,
        PathValues.API_APP_DEVICE: ApiAppDevice,
        PathValues.API_APP_DEVICE_REFRESH: ApiAppDeviceRefresh,
        PathValues.API_SETTINGMANAGEMENT_EMAILING: ApiSettingManagementEmailing,
        PathValues.API_SETTINGMANAGEMENT_EMAILING_SENDTESTEMAIL: ApiSettingManagementEmailingSendTestEmail,
        PathValues.API_FEATUREMANAGEMENT_FEATURES: ApiFeatureManagementFeatures,
        PathValues.API_APP_KEYVALUE_BOOL: ApiAppKeyValueBool,
        PathValues.API_APP_KEYVALUE_DATETIME: ApiAppKeyValueDateTime,
        PathValues.API_APP_KEYVALUE_DECIMAL: ApiAppKeyValueDecimal,
        PathValues.API_APP_KEYVALUE_DOUBLE: ApiAppKeyValueDouble,
        PathValues.API_APP_KEYVALUE_INT: ApiAppKeyValueInt,
        PathValues.API_APP_KEYVALUE_STRING: ApiAppKeyValueString,
        PathValues.API_APP_KEYVALUE_SETBOOL: ApiAppKeyValueSetBool,
        PathValues.API_APP_KEYVALUE_SETDATETIME: ApiAppKeyValueSetDateTime,
        PathValues.API_APP_KEYVALUE_SETDECIMAL: ApiAppKeyValueSetDecimal,
        PathValues.API_APP_KEYVALUE_SETDOUBLE: ApiAppKeyValueSetDouble,
        PathValues.API_APP_KEYVALUE_SETINT: ApiAppKeyValueSetInt,
        PathValues.API_APP_KEYVALUE_SETSTRING: ApiAppKeyValueSetString,
        PathValues.API_ACCOUNT_LOGIN: ApiAccountLogin,
        PathValues.API_ACCOUNT_LOGOUT: ApiAccountLogout,
        PathValues.API_ACCOUNT_CHECKPASSWORD: ApiAccountCheckPassword,
        PathValues.API_APP_MESSAGE_PUBLISH: ApiAppMessagePublish,
        PathValues.API_APP_MESSAGE_RECALL: ApiAppMessageRecall,
        PathValues.API_APP_MESSAGE_SUBSCRIBE: ApiAppMessageSubscribe,
        PathValues.API_APP_MESSAGE_UNSUBSCRIBE: ApiAppMessageUnsubscribe,
        PathValues.API_APP_MESSAGETEMPLATE: ApiAppMessageTemplate,
        PathValues.API_APP_MESSAGETEMPLATE_ID: ApiAppMessageTemplateId,
        PathValues.API_APP_MESSAGETEMPLATERELEASE: ApiAppMessageTemplateRelease,
        PathValues.API_APP_MESSAGETEMPLATERELEASE_ID: ApiAppMessageTemplateReleaseId,
        PathValues.API_APP_NOTIFICATION_BARK_API_KEY_MESSAGE: ApiAppNotificationBarkApiKeyMessage,
        PathValues.API_APP_NOTIFICATION: ApiAppNotification,
        PathValues.API_APP_NOTIFICATION_PUSH: ApiAppNotificationPush,
        PathValues.API_PERMISSIONMANAGEMENT_PERMISSIONS: ApiPermissionManagementPermissions,
        PathValues.API_ACCOUNT_MYPROFILE: ApiAccountMyProfile,
        PathValues.API_ACCOUNT_MYPROFILE_CHANGEPASSWORD: ApiAccountMyProfileChangePassword,
        PathValues.API_APP_PUUPEE_PULL: ApiAppPuupeePull,
        PathValues.API_APP_PUUPEE_PUSH: ApiAppPuupeePush,
        PathValues.API_IDENTITY_ROLES_ALL: ApiIdentityRolesAll,
        PathValues.API_IDENTITY_ROLES: ApiIdentityRoles,
        PathValues.API_IDENTITY_ROLES_ID: ApiIdentityRolesId,
        PathValues.API_APP_SETTINGS: ApiAppSettings,
        PathValues.API_APP_SETTINGS_SET: ApiAppSettingsSet,
        PathValues.API_APP_SIMPLEDATA_ID: ApiAppSimpleDataId,
        PathValues.API_APP_SIMPLEDATA: ApiAppSimpleData,
        PathValues.API_APP_SIMPLEDATA_SAVE: ApiAppSimpleDataSave,
        PathValues.API_APP_STORAGEOBJECT_FILE: ApiAppStorageObjectFile,
        PathValues.API_APP_STORAGEOBJECT_THUMB: ApiAppStorageObjectThumb,
        PathValues.API_APP_STORAGEOBJECT_FILEORCREDENTIALS: ApiAppStorageObjectFileOrCredentials,
        PathValues.API_APP_STORAGEOBJECT_PRESIGNURL: ApiAppStorageObjectPreSignUrl,
        PathValues.API_APP_SUBSCRIPTION_VERIFYAPPLE: ApiAppSubscriptionVerifyApple,
        PathValues.API_APP_SYNCSTATE: ApiAppSyncState,
        PathValues.API_APP_SYNCSTATE_PUUPEECHANGEDETO: ApiAppSyncStatePuupeeChangedEto,
        PathValues.API_MULTITENANCY_TENANTS_ID: ApiMultiTenancyTenantsId,
        PathValues.API_MULTITENANCY_TENANTS: ApiMultiTenancyTenants,
        PathValues.API_MULTITENANCY_TENANTS_ID_DEFAULTCONNECTIONSTRING: ApiMultiTenancyTenantsIdDefaultConnectionString,
        PathValues.API_TEST_DATETIME: ApiTestDatetime,
        PathValues.API_IDENTITY_USERS_ID: ApiIdentityUsersId,
        PathValues.API_IDENTITY_USERS: ApiIdentityUsers,
        PathValues.API_IDENTITY_USERS_ID_ROLES: ApiIdentityUsersIdRoles,
        PathValues.API_IDENTITY_USERS_ASSIGNABLEROLES: ApiIdentityUsersAssignableRoles,
        PathValues.API_IDENTITY_USERS_BYUSERNAME_USER_NAME: ApiIdentityUsersByUsernameUserName,
        PathValues.API_IDENTITY_USERS_BYEMAIL_EMAIL: ApiIdentityUsersByEmailEmail,
        PathValues.API_IDENTITY_USERS_LOOKUP_ID: ApiIdentityUsersLookupId,
        PathValues.API_IDENTITY_USERS_LOOKUP_BYUSERNAME_USER_NAME: ApiIdentityUsersLookupByUsernameUserName,
        PathValues.API_IDENTITY_USERS_LOOKUP_SEARCH: ApiIdentityUsersLookupSearch,
        PathValues.API_IDENTITY_USERS_LOOKUP_COUNT: ApiIdentityUsersLookupCount,
        PathValues.API_APP_USERSTORAGE: ApiAppUserStorage,
        PathValues.API_APP_VERIFICATION_SENDCODE: ApiAppVerificationSendCode,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_ABP_APIDEFINITION: ApiAbpApiDefinition,
        PathValues.API_ABP_APPLICATIONCONFIGURATION: ApiAbpApplicationConfiguration,
        PathValues.API_ABP_APPLICATIONLOCALIZATION: ApiAbpApplicationLocalization,
        PathValues.API_ABP_MULTITENANCY_TENANTS_BYNAME_NAME: ApiAbpMultiTenancyTenantsByNameName,
        PathValues.API_ABP_MULTITENANCY_TENANTS_BYID_ID: ApiAbpMultiTenancyTenantsByIdId,
        PathValues.API_ACCOUNT_REGISTER: ApiAccountRegister,
        PathValues.API_ACCOUNT_SENDPASSWORDRESETCODE: ApiAccountSendPasswordResetCode,
        PathValues.API_ACCOUNT_VERIFYPASSWORDRESETTOKEN: ApiAccountVerifyPasswordResetToken,
        PathValues.API_ACCOUNT_RESETPASSWORD: ApiAccountResetPassword,
        PathValues.API_APP_ACCOUNT: ApiAppAccount,
        PathValues.API_APP_APP: ApiAppApp,
        PathValues.API_APP_APP_ID: ApiAppAppId,
        PathValues.API_APP_APP_ID_WITHUSER: ApiAppAppIdWithUser,
        PathValues.API_APP_APP_BYNAME: ApiAppAppByName,
        PathValues.API_APP_APP_UPLOADCREDENTIALS: ApiAppAppUploadCredentials,
        PathValues.API_APP_APP_BYDEVELOPER: ApiAppAppByDeveloper,
        PathValues.API_APP_APP_PUBLIC: ApiAppAppPublic,
        PathValues.API_APP_APP_BYDEVELOPERALL: ApiAppAppByDeveloperAll,
        PathValues.API_APP_APPFEATURE: ApiAppAppFeature,
        PathValues.API_APP_APPFEATURE_ID: ApiAppAppFeatureId,
        PathValues.API_APP_APPPRICING: ApiAppAppPricing,
        PathValues.API_APP_APPPRICING_ID: ApiAppAppPricingId,
        PathValues.API_APP_APPPRICING_BYAPPID_APP_ID: ApiAppAppPricingByAppIdAppId,
        PathValues.API_APP_APPPRICINGITEM: ApiAppAppPricingItem,
        PathValues.API_APP_APPPRICINGITEM_ID: ApiAppAppPricingItemId,
        PathValues.API_APP_APPRELEASE: ApiAppAppRelease,
        PathValues.API_APP_APPRELEASE_ID: ApiAppAppReleaseId,
        PathValues.API_APP_APPRELEASE_LATEST: ApiAppAppReleaseLatest,
        PathValues.API_APP_APPSDK: ApiAppAppSdk,
        PathValues.API_APP_APPSDK_ID: ApiAppAppSdkId,
        PathValues.API_APP_APPUSERSCORE: ApiAppAppUserScore,
        PathValues.API_APP_DEVICE_BIND: ApiAppDeviceBind,
        PathValues.API_APP_DEVICE: ApiAppDevice,
        PathValues.API_APP_DEVICE_REFRESH: ApiAppDeviceRefresh,
        PathValues.API_SETTINGMANAGEMENT_EMAILING: ApiSettingManagementEmailing,
        PathValues.API_SETTINGMANAGEMENT_EMAILING_SENDTESTEMAIL: ApiSettingManagementEmailingSendTestEmail,
        PathValues.API_FEATUREMANAGEMENT_FEATURES: ApiFeatureManagementFeatures,
        PathValues.API_APP_KEYVALUE_BOOL: ApiAppKeyValueBool,
        PathValues.API_APP_KEYVALUE_DATETIME: ApiAppKeyValueDateTime,
        PathValues.API_APP_KEYVALUE_DECIMAL: ApiAppKeyValueDecimal,
        PathValues.API_APP_KEYVALUE_DOUBLE: ApiAppKeyValueDouble,
        PathValues.API_APP_KEYVALUE_INT: ApiAppKeyValueInt,
        PathValues.API_APP_KEYVALUE_STRING: ApiAppKeyValueString,
        PathValues.API_APP_KEYVALUE_SETBOOL: ApiAppKeyValueSetBool,
        PathValues.API_APP_KEYVALUE_SETDATETIME: ApiAppKeyValueSetDateTime,
        PathValues.API_APP_KEYVALUE_SETDECIMAL: ApiAppKeyValueSetDecimal,
        PathValues.API_APP_KEYVALUE_SETDOUBLE: ApiAppKeyValueSetDouble,
        PathValues.API_APP_KEYVALUE_SETINT: ApiAppKeyValueSetInt,
        PathValues.API_APP_KEYVALUE_SETSTRING: ApiAppKeyValueSetString,
        PathValues.API_ACCOUNT_LOGIN: ApiAccountLogin,
        PathValues.API_ACCOUNT_LOGOUT: ApiAccountLogout,
        PathValues.API_ACCOUNT_CHECKPASSWORD: ApiAccountCheckPassword,
        PathValues.API_APP_MESSAGE_PUBLISH: ApiAppMessagePublish,
        PathValues.API_APP_MESSAGE_RECALL: ApiAppMessageRecall,
        PathValues.API_APP_MESSAGE_SUBSCRIBE: ApiAppMessageSubscribe,
        PathValues.API_APP_MESSAGE_UNSUBSCRIBE: ApiAppMessageUnsubscribe,
        PathValues.API_APP_MESSAGETEMPLATE: ApiAppMessageTemplate,
        PathValues.API_APP_MESSAGETEMPLATE_ID: ApiAppMessageTemplateId,
        PathValues.API_APP_MESSAGETEMPLATERELEASE: ApiAppMessageTemplateRelease,
        PathValues.API_APP_MESSAGETEMPLATERELEASE_ID: ApiAppMessageTemplateReleaseId,
        PathValues.API_APP_NOTIFICATION_BARK_API_KEY_MESSAGE: ApiAppNotificationBarkApiKeyMessage,
        PathValues.API_APP_NOTIFICATION: ApiAppNotification,
        PathValues.API_APP_NOTIFICATION_PUSH: ApiAppNotificationPush,
        PathValues.API_PERMISSIONMANAGEMENT_PERMISSIONS: ApiPermissionManagementPermissions,
        PathValues.API_ACCOUNT_MYPROFILE: ApiAccountMyProfile,
        PathValues.API_ACCOUNT_MYPROFILE_CHANGEPASSWORD: ApiAccountMyProfileChangePassword,
        PathValues.API_APP_PUUPEE_PULL: ApiAppPuupeePull,
        PathValues.API_APP_PUUPEE_PUSH: ApiAppPuupeePush,
        PathValues.API_IDENTITY_ROLES_ALL: ApiIdentityRolesAll,
        PathValues.API_IDENTITY_ROLES: ApiIdentityRoles,
        PathValues.API_IDENTITY_ROLES_ID: ApiIdentityRolesId,
        PathValues.API_APP_SETTINGS: ApiAppSettings,
        PathValues.API_APP_SETTINGS_SET: ApiAppSettingsSet,
        PathValues.API_APP_SIMPLEDATA_ID: ApiAppSimpleDataId,
        PathValues.API_APP_SIMPLEDATA: ApiAppSimpleData,
        PathValues.API_APP_SIMPLEDATA_SAVE: ApiAppSimpleDataSave,
        PathValues.API_APP_STORAGEOBJECT_FILE: ApiAppStorageObjectFile,
        PathValues.API_APP_STORAGEOBJECT_THUMB: ApiAppStorageObjectThumb,
        PathValues.API_APP_STORAGEOBJECT_FILEORCREDENTIALS: ApiAppStorageObjectFileOrCredentials,
        PathValues.API_APP_STORAGEOBJECT_PRESIGNURL: ApiAppStorageObjectPreSignUrl,
        PathValues.API_APP_SUBSCRIPTION_VERIFYAPPLE: ApiAppSubscriptionVerifyApple,
        PathValues.API_APP_SYNCSTATE: ApiAppSyncState,
        PathValues.API_APP_SYNCSTATE_PUUPEECHANGEDETO: ApiAppSyncStatePuupeeChangedEto,
        PathValues.API_MULTITENANCY_TENANTS_ID: ApiMultiTenancyTenantsId,
        PathValues.API_MULTITENANCY_TENANTS: ApiMultiTenancyTenants,
        PathValues.API_MULTITENANCY_TENANTS_ID_DEFAULTCONNECTIONSTRING: ApiMultiTenancyTenantsIdDefaultConnectionString,
        PathValues.API_TEST_DATETIME: ApiTestDatetime,
        PathValues.API_IDENTITY_USERS_ID: ApiIdentityUsersId,
        PathValues.API_IDENTITY_USERS: ApiIdentityUsers,
        PathValues.API_IDENTITY_USERS_ID_ROLES: ApiIdentityUsersIdRoles,
        PathValues.API_IDENTITY_USERS_ASSIGNABLEROLES: ApiIdentityUsersAssignableRoles,
        PathValues.API_IDENTITY_USERS_BYUSERNAME_USER_NAME: ApiIdentityUsersByUsernameUserName,
        PathValues.API_IDENTITY_USERS_BYEMAIL_EMAIL: ApiIdentityUsersByEmailEmail,
        PathValues.API_IDENTITY_USERS_LOOKUP_ID: ApiIdentityUsersLookupId,
        PathValues.API_IDENTITY_USERS_LOOKUP_BYUSERNAME_USER_NAME: ApiIdentityUsersLookupByUsernameUserName,
        PathValues.API_IDENTITY_USERS_LOOKUP_SEARCH: ApiIdentityUsersLookupSearch,
        PathValues.API_IDENTITY_USERS_LOOKUP_COUNT: ApiIdentityUsersLookupCount,
        PathValues.API_APP_USERSTORAGE: ApiAppUserStorage,
        PathValues.API_APP_VERIFICATION_SENDCODE: ApiAppVerificationSendCode,
    }
)
