import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.api_abp_api_definition import ApiAbpApiDefinition
from openapi_client.apis.paths.api_abp_application_configuration import ApiAbpApplicationConfiguration
from openapi_client.apis.paths.api_abp_application_localization import ApiAbpApplicationLocalization
from openapi_client.apis.paths.api_abp_multi_tenancy_tenants_by_name_name import ApiAbpMultiTenancyTenantsByNameName
from openapi_client.apis.paths.api_abp_multi_tenancy_tenants_by_id_id import ApiAbpMultiTenancyTenantsByIdId
from openapi_client.apis.paths.api_account_register import ApiAccountRegister
from openapi_client.apis.paths.api_account_send_password_reset_code import ApiAccountSendPasswordResetCode
from openapi_client.apis.paths.api_account_verify_password_reset_token import ApiAccountVerifyPasswordResetToken
from openapi_client.apis.paths.api_account_reset_password import ApiAccountResetPassword
from openapi_client.apis.paths.api_app_app import ApiAppApp
from openapi_client.apis.paths.api_app_app_id import ApiAppAppId
from openapi_client.apis.paths.api_app_app_by_name import ApiAppAppByName
from openapi_client.apis.paths.api_app_app_upload_credentials import ApiAppAppUploadCredentials
from openapi_client.apis.paths.api_app_app_by_developer import ApiAppAppByDeveloper
from openapi_client.apis.paths.api_app_app_feature import ApiAppAppFeature
from openapi_client.apis.paths.api_app_app_feature_id import ApiAppAppFeatureId
from openapi_client.apis.paths.api_app_app_release import ApiAppAppRelease
from openapi_client.apis.paths.api_app_app_release_id import ApiAppAppReleaseId
from openapi_client.apis.paths.api_app_app_sdk import ApiAppAppSdk
from openapi_client.apis.paths.api_app_app_sdk_id import ApiAppAppSdkId
from openapi_client.apis.paths.api_app_app_user_score import ApiAppAppUserScore
from openapi_client.apis.paths.api_app_device_bind import ApiAppDeviceBind
from openapi_client.apis.paths.api_app_device import ApiAppDevice
from openapi_client.apis.paths.api_app_device_refresh import ApiAppDeviceRefresh
from openapi_client.apis.paths.api_setting_management_emailing import ApiSettingManagementEmailing
from openapi_client.apis.paths.api_setting_management_emailing_send_test_email import ApiSettingManagementEmailingSendTestEmail
from openapi_client.apis.paths.api_feature_management_features import ApiFeatureManagementFeatures
from openapi_client.apis.paths.api_app_key_value_bool import ApiAppKeyValueBool
from openapi_client.apis.paths.api_app_key_value_date_time import ApiAppKeyValueDateTime
from openapi_client.apis.paths.api_app_key_value_decimal import ApiAppKeyValueDecimal
from openapi_client.apis.paths.api_app_key_value_double import ApiAppKeyValueDouble
from openapi_client.apis.paths.api_app_key_value_int import ApiAppKeyValueInt
from openapi_client.apis.paths.api_app_key_value_string import ApiAppKeyValueString
from openapi_client.apis.paths.api_app_key_value_set_bool import ApiAppKeyValueSetBool
from openapi_client.apis.paths.api_app_key_value_set_date_time import ApiAppKeyValueSetDateTime
from openapi_client.apis.paths.api_app_key_value_set_decimal import ApiAppKeyValueSetDecimal
from openapi_client.apis.paths.api_app_key_value_set_double import ApiAppKeyValueSetDouble
from openapi_client.apis.paths.api_app_key_value_set_int import ApiAppKeyValueSetInt
from openapi_client.apis.paths.api_app_key_value_set_string import ApiAppKeyValueSetString
from openapi_client.apis.paths.api_account_login import ApiAccountLogin
from openapi_client.apis.paths.api_account_logout import ApiAccountLogout
from openapi_client.apis.paths.api_account_check_password import ApiAccountCheckPassword
from openapi_client.apis.paths.api_permission_management_permissions import ApiPermissionManagementPermissions
from openapi_client.apis.paths.api_account_my_profile import ApiAccountMyProfile
from openapi_client.apis.paths.api_account_my_profile_change_password import ApiAccountMyProfileChangePassword
from openapi_client.apis.paths.api_app_puupee_pull import ApiAppPuupeePull
from openapi_client.apis.paths.api_app_puupee_push import ApiAppPuupeePush
from openapi_client.apis.paths.api_identity_roles_all import ApiIdentityRolesAll
from openapi_client.apis.paths.api_identity_roles import ApiIdentityRoles
from openapi_client.apis.paths.api_identity_roles_id import ApiIdentityRolesId
from openapi_client.apis.paths.api_app_settings import ApiAppSettings
from openapi_client.apis.paths.api_app_settings_set import ApiAppSettingsSet
from openapi_client.apis.paths.api_app_simple_data_id import ApiAppSimpleDataId
from openapi_client.apis.paths.api_app_simple_data import ApiAppSimpleData
from openapi_client.apis.paths.api_app_simple_data_save import ApiAppSimpleDataSave
from openapi_client.apis.paths.api_app_storage_object_file import ApiAppStorageObjectFile
from openapi_client.apis.paths.api_app_storage_object_thumb import ApiAppStorageObjectThumb
from openapi_client.apis.paths.api_app_storage_object_file_or_credentials import ApiAppStorageObjectFileOrCredentials
from openapi_client.apis.paths.api_app_storage_object_pre_sign_url import ApiAppStorageObjectPreSignUrl
from openapi_client.apis.paths.api_app_sync_state import ApiAppSyncState
from openapi_client.apis.paths.api_app_sync_state_puupee_changed_eto import ApiAppSyncStatePuupeeChangedEto
from openapi_client.apis.paths.api_multi_tenancy_tenants_id import ApiMultiTenancyTenantsId
from openapi_client.apis.paths.api_multi_tenancy_tenants import ApiMultiTenancyTenants
from openapi_client.apis.paths.api_multi_tenancy_tenants_id_default_connection_string import ApiMultiTenancyTenantsIdDefaultConnectionString
from openapi_client.apis.paths.api_test_datetime import ApiTestDatetime
from openapi_client.apis.paths.api_identity_users_id import ApiIdentityUsersId
from openapi_client.apis.paths.api_identity_users import ApiIdentityUsers
from openapi_client.apis.paths.api_identity_users_id_roles import ApiIdentityUsersIdRoles
from openapi_client.apis.paths.api_identity_users_assignable_roles import ApiIdentityUsersAssignableRoles
from openapi_client.apis.paths.api_identity_users_by_username_user_name import ApiIdentityUsersByUsernameUserName
from openapi_client.apis.paths.api_identity_users_by_email_email import ApiIdentityUsersByEmailEmail
from openapi_client.apis.paths.api_identity_users_lookup_id import ApiIdentityUsersLookupId
from openapi_client.apis.paths.api_identity_users_lookup_by_username_user_name import ApiIdentityUsersLookupByUsernameUserName
from openapi_client.apis.paths.api_identity_users_lookup_search import ApiIdentityUsersLookupSearch
from openapi_client.apis.paths.api_identity_users_lookup_count import ApiIdentityUsersLookupCount
from openapi_client.apis.paths.api_app_user_storage import ApiAppUserStorage
from openapi_client.apis.paths.api_app_verification_send_code import ApiAppVerificationSendCode

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
        PathValues.API_APP_APP: ApiAppApp,
        PathValues.API_APP_APP_ID: ApiAppAppId,
        PathValues.API_APP_APP_BYNAME: ApiAppAppByName,
        PathValues.API_APP_APP_UPLOADCREDENTIALS: ApiAppAppUploadCredentials,
        PathValues.API_APP_APP_BYDEVELOPER: ApiAppAppByDeveloper,
        PathValues.API_APP_APPFEATURE: ApiAppAppFeature,
        PathValues.API_APP_APPFEATURE_ID: ApiAppAppFeatureId,
        PathValues.API_APP_APPRELEASE: ApiAppAppRelease,
        PathValues.API_APP_APPRELEASE_ID: ApiAppAppReleaseId,
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
        PathValues.API_APP_APP: ApiAppApp,
        PathValues.API_APP_APP_ID: ApiAppAppId,
        PathValues.API_APP_APP_BYNAME: ApiAppAppByName,
        PathValues.API_APP_APP_UPLOADCREDENTIALS: ApiAppAppUploadCredentials,
        PathValues.API_APP_APP_BYDEVELOPER: ApiAppAppByDeveloper,
        PathValues.API_APP_APPFEATURE: ApiAppAppFeature,
        PathValues.API_APP_APPFEATURE_ID: ApiAppAppFeatureId,
        PathValues.API_APP_APPRELEASE: ApiAppAppRelease,
        PathValues.API_APP_APPRELEASE_ID: ApiAppAppReleaseId,
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
