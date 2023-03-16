# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from puupee-api.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ABP_API_DEFINITION = "AbpApiDefinition"
    ABP_APPLICATION_CONFIGURATION = "AbpApplicationConfiguration"
    ABP_APPLICATION_LOCALIZATION = "AbpApplicationLocalization"
    ABP_TENANT = "AbpTenant"
    ACCOUNT = "Account"
    APP = "App"
    APP_FEATURE = "AppFeature"
    APP_PRICING = "AppPricing"
    APP_PRICING_ITEM = "AppPricingItem"
    APP_RELEASE = "AppRelease"
    APP_SDK = "AppSdk"
    APP_USER_SCORE = "AppUserScore"
    DEVICE = "Device"
    EMAIL_SETTINGS = "EmailSettings"
    FEATURES = "Features"
    KEY_VALUE = "KeyValue"
    LOGIN = "Login"
    PERMISSIONS = "Permissions"
    PROFILE = "Profile"
    PUUPEE = "Puupee"
    ROLE = "Role"
    SETTINGS = "Settings"
    SIMPLE_DATA = "SimpleData"
    STORAGE_OBJECT = "StorageObject"
    SUBSCRIPTION = "Subscription"
    SYNC_STATE = "SyncState"
    TENANT = "Tenant"
    TEST = "Test"
    USER = "User"
    USER_LOOKUP = "UserLookup"
    USER_STORAGE = "UserStorage"
    VERIFICATION = "Verification"
