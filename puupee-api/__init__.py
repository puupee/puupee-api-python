# coding: utf-8

# flake8: noqa

"""
    Puupee API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "${VERSION}"

# import apis into sdk package
from puupee-api.api.abp_api_definition_api import AbpApiDefinitionApi
from puupee-api.api.abp_application_configuration_api import AbpApplicationConfigurationApi
from puupee-api.api.abp_application_localization_api import AbpApplicationLocalizationApi
from puupee-api.api.abp_tenant_api import AbpTenantApi
from puupee-api.api.account_api import AccountApi
from puupee-api.api.app_api import AppApi
from puupee-api.api.app_feature_api import AppFeatureApi
from puupee-api.api.app_pricing_api import AppPricingApi
from puupee-api.api.app_pricing_item_api import AppPricingItemApi
from puupee-api.api.app_release_api import AppReleaseApi
from puupee-api.api.app_sdk_api import AppSdkApi
from puupee-api.api.app_user_score_api import AppUserScoreApi
from puupee-api.api.avatar_api import AvatarApi
from puupee-api.api.device_api import DeviceApi
from puupee-api.api.email_settings_api import EmailSettingsApi
from puupee-api.api.features_api import FeaturesApi
from puupee-api.api.key_value_api import KeyValueApi
from puupee-api.api.login_api import LoginApi
from puupee-api.api.message_api import MessageApi
from puupee-api.api.message_source_api import MessageSourceApi
from puupee-api.api.message_source_category_api import MessageSourceCategoryApi
from puupee-api.api.message_source_route_api import MessageSourceRouteApi
from puupee-api.api.message_source_route_sub_api import MessageSourceRouteSubApi
from puupee-api.api.message_template_api import MessageTemplateApi
from puupee-api.api.message_template_release_api import MessageTemplateReleaseApi
from puupee-api.api.notification_api import NotificationApi
from puupee-api.api.permissions_api import PermissionsApi
from puupee-api.api.profile_api import ProfileApi
from puupee-api.api.puupee_api import PuupeeApi
from puupee-api.api.role_api import RoleApi
from puupee-api.api.settings_api import SettingsApi
from puupee-api.api.simple_data_api import SimpleDataApi
from puupee-api.api.storage_object_api import StorageObjectApi
from puupee-api.api.subscription_api import SubscriptionApi
from puupee-api.api.sync_state_api import SyncStateApi
from puupee-api.api.tenant_api import TenantApi
from puupee-api.api.test_api import TestApi
from puupee-api.api.user_api import UserApi
from puupee-api.api.user_lookup_api import UserLookupApi
from puupee-api.api.user_storage_api import UserStorageApi
from puupee-api.api.verification_api import VerificationApi

# import ApiClient
from puupee-api.api_client import ApiClient
from puupee-api.configuration import Configuration
from puupee-api.exceptions import OpenApiException
from puupee-api.exceptions import ApiTypeError
from puupee-api.exceptions import ApiValueError
from puupee-api.exceptions import ApiKeyError
from puupee-api.exceptions import ApiAttributeError
from puupee-api.exceptions import ApiException
# import models into sdk package
from puupee-api.models.abp_login_result import AbpLoginResult
from puupee-api.models.action_api_description_model import ActionApiDescriptionModel
from puupee-api.models.app_dto import AppDto
from puupee-api.models.app_dto_paged_result_dto import AppDtoPagedResultDto
from puupee-api.models.app_feature_dto import AppFeatureDto
from puupee-api.models.app_pricing_dto import AppPricingDto
from puupee-api.models.app_pricing_dto_paged_result_dto import AppPricingDtoPagedResultDto
from puupee-api.models.app_pricing_item_dto import AppPricingItemDto
from puupee-api.models.app_release_dto import AppReleaseDto
from puupee-api.models.app_release_dto_paged_result_dto import AppReleaseDtoPagedResultDto
from puupee-api.models.app_run_dto import AppRunDto
from puupee-api.models.app_run_record_dto import AppRunRecordDto
from puupee-api.models.app_run_record_update_dto import AppRunRecordUpdateDto
from puupee-api.models.app_sdk_dto import AppSdkDto
from puupee-api.models.app_theme import AppTheme
from puupee-api.models.app_theme_mode import AppThemeMode
from puupee-api.models.app_user_score_dto import AppUserScoreDto
from puupee-api.models.app_with_user_dto import AppWithUserDto
from puupee-api.models.app_with_user_dto_paged_result_dto import AppWithUserDtoPagedResultDto
from puupee-api.models.apple_notificaion_dto import AppleNotificaionDto
from puupee-api.models.apple_verify_recceipt_status import AppleVerifyRecceiptStatus
from puupee-api.models.apple_verify_receipt_result import AppleVerifyReceiptResult
from puupee-api.models.application_api_description_model import ApplicationApiDescriptionModel
from puupee-api.models.application_auth_configuration_dto import ApplicationAuthConfigurationDto
from puupee-api.models.application_configuration_dto import ApplicationConfigurationDto
from puupee-api.models.application_feature_configuration_dto import ApplicationFeatureConfigurationDto
from puupee-api.models.application_global_feature_configuration_dto import ApplicationGlobalFeatureConfigurationDto
from puupee-api.models.application_localization_configuration_dto import ApplicationLocalizationConfigurationDto
from puupee-api.models.application_localization_dto import ApplicationLocalizationDto
from puupee-api.models.application_localization_resource_dto import ApplicationLocalizationResourceDto
from puupee-api.models.application_setting_configuration_dto import ApplicationSettingConfigurationDto
from puupee-api.models.avatar_dto import AvatarDto
from puupee-api.models.bind_device_dto import BindDeviceDto
from puupee-api.models.boolean_key_value import BooleanKeyValue
from puupee-api.models.boolean_set_key_value_dto import BooleanSetKeyValueDto
from puupee-api.models.change_password_input import ChangePasswordInput
from puupee-api.models.clock_dto import ClockDto
from puupee-api.models.controller_api_description_model import ControllerApiDescriptionModel
from puupee-api.models.controller_interface_api_description_model import ControllerInterfaceApiDescriptionModel
from puupee-api.models.create_avatar_dto import CreateAvatarDto
from puupee-api.models.create_message_template_release_dto import CreateMessageTemplateReleaseDto
from puupee-api.models.create_open_iddict_application_dto import CreateOpenIddictApplicationDto
from puupee-api.models.create_or_get_subscription_order_dto import CreateOrGetSubscriptionOrderDto
from puupee-api.models.create_or_update_app_dto import CreateOrUpdateAppDto
from puupee-api.models.create_or_update_app_feature_dto import CreateOrUpdateAppFeatureDto
from puupee-api.models.create_or_update_app_pricing_dto import CreateOrUpdateAppPricingDto
from puupee-api.models.create_or_update_app_pricing_item_dto import CreateOrUpdateAppPricingItemDto
from puupee-api.models.create_or_update_app_release_dto import CreateOrUpdateAppReleaseDto
from puupee-api.models.create_or_update_app_sdk_dto import CreateOrUpdateAppSdkDto
from puupee-api.models.create_or_update_app_user_score_dto import CreateOrUpdateAppUserScoreDto
from puupee-api.models.create_or_update_message_template_dto import CreateOrUpdateMessageTemplateDto
from puupee-api.models.create_or_update_puupee_dto import CreateOrUpdatePuupeeDto
from puupee-api.models.create_push_notification_dto import CreatePushNotificationDto
from puupee-api.models.create_update_message_source_dto import CreateUpdateMessageSourceDto
from puupee-api.models.create_update_message_source_route_dto import CreateUpdateMessageSourceRouteDto
from puupee-api.models.create_update_message_source_route_sub_dto import CreateUpdateMessageSourceRouteSubDto
from puupee-api.models.current_culture_dto import CurrentCultureDto
from puupee-api.models.current_tenant_dto import CurrentTenantDto
from puupee-api.models.current_user_dto import CurrentUserDto
from puupee-api.models.date_time_format_dto import DateTimeFormatDto
from puupee-api.models.date_time_key_value import DateTimeKeyValue
from puupee-api.models.date_time_set_key_value_dto import DateTimeSetKeyValueDto
from puupee-api.models.decimal_key_value import DecimalKeyValue
from puupee-api.models.decimal_set_key_value_dto import DecimalSetKeyValueDto
from puupee-api.models.device_dto import DeviceDto
from puupee-api.models.device_dto_paged_result_dto import DeviceDtoPagedResultDto
from puupee-api.models.double_key_value import DoubleKeyValue
from puupee-api.models.double_set_key_value_dto import DoubleSetKeyValueDto
from puupee-api.models.email_settings_dto import EmailSettingsDto
from puupee-api.models.entity_extension_dto import EntityExtensionDto
from puupee-api.models.extension_enum_dto import ExtensionEnumDto
from puupee-api.models.extension_enum_field_dto import ExtensionEnumFieldDto
from puupee-api.models.extension_property_api_create_dto import ExtensionPropertyApiCreateDto
from puupee-api.models.extension_property_api_dto import ExtensionPropertyApiDto
from puupee-api.models.extension_property_api_get_dto import ExtensionPropertyApiGetDto
from puupee-api.models.extension_property_api_update_dto import ExtensionPropertyApiUpdateDto
from puupee-api.models.extension_property_attribute_dto import ExtensionPropertyAttributeDto
from puupee-api.models.extension_property_dto import ExtensionPropertyDto
from puupee-api.models.extension_property_ui_dto import ExtensionPropertyUiDto
from puupee-api.models.extension_property_ui_form_dto import ExtensionPropertyUiFormDto
from puupee-api.models.extension_property_ui_lookup_dto import ExtensionPropertyUiLookupDto
from puupee-api.models.extension_property_ui_table_dto import ExtensionPropertyUiTableDto
from puupee-api.models.feature_dto import FeatureDto
from puupee-api.models.feature_group_dto import FeatureGroupDto
from puupee-api.models.feature_provider_dto import FeatureProviderDto
from puupee-api.models.find_tenant_result_dto import FindTenantResultDto
from puupee-api.models.get_feature_list_result_dto import GetFeatureListResultDto
from puupee-api.models.get_permission_list_result_dto import GetPermissionListResultDto
from puupee-api.models.i_string_value_type import IStringValueType
from puupee-api.models.i_value_validator import IValueValidator
from puupee-api.models.iana_time_zone import IanaTimeZone
from puupee-api.models.identity_role_create_dto import IdentityRoleCreateDto
from puupee-api.models.identity_role_dto import IdentityRoleDto
from puupee-api.models.identity_role_dto_list_result_dto import IdentityRoleDtoListResultDto
from puupee-api.models.identity_role_dto_paged_result_dto import IdentityRoleDtoPagedResultDto
from puupee-api.models.identity_role_update_dto import IdentityRoleUpdateDto
from puupee-api.models.identity_user import IdentityUser
from puupee-api.models.identity_user_claim import IdentityUserClaim
from puupee-api.models.identity_user_create_dto import IdentityUserCreateDto
from puupee-api.models.identity_user_dto import IdentityUserDto
from puupee-api.models.identity_user_dto_paged_result_dto import IdentityUserDtoPagedResultDto
from puupee-api.models.identity_user_login import IdentityUserLogin
from puupee-api.models.identity_user_organization_unit import IdentityUserOrganizationUnit
from puupee-api.models.identity_user_role import IdentityUserRole
from puupee-api.models.identity_user_token import IdentityUserToken
from puupee-api.models.identity_user_update_dto import IdentityUserUpdateDto
from puupee-api.models.identity_user_update_roles_dto import IdentityUserUpdateRolesDto
from puupee-api.models.in_app import InApp
from puupee-api.models.int32_key_value import Int32KeyValue
from puupee-api.models.int32_set_key_value_dto import Int32SetKeyValueDto
from puupee-api.models.interface_method_api_description_model import InterfaceMethodApiDescriptionModel
from puupee-api.models.language_info import LanguageInfo
from puupee-api.models.latest_receipt_info import LatestReceiptInfo
from puupee-api.models.localizable_string_dto import LocalizableStringDto
from puupee-api.models.login_result_type import LoginResultType
from puupee-api.models.message_publish_dto import MessagePublishDto
from puupee-api.models.message_recall_dto import MessageRecallDto
from puupee-api.models.message_source_category_dto import MessageSourceCategoryDto
from puupee-api.models.message_source_dto import MessageSourceDto
from puupee-api.models.message_source_route_dto import MessageSourceRouteDto
from puupee-api.models.message_source_route_sub_dto import MessageSourceRouteSubDto
from puupee-api.models.message_subscribe_dto import MessageSubscribeDto
from puupee-api.models.message_template_dto import MessageTemplateDto
from puupee-api.models.message_template_release_dto import MessageTemplateReleaseDto
from puupee-api.models.message_unsubscribe_dto import MessageUnsubscribeDto
from puupee-api.models.method_parameter_api_description_model import MethodParameterApiDescriptionModel
from puupee-api.models.module_api_description_model import ModuleApiDescriptionModel
from puupee-api.models.module_extension_dto import ModuleExtensionDto
from puupee-api.models.multi_tenancy_info_dto import MultiTenancyInfoDto
from puupee-api.models.name_value import NameValue
from puupee-api.models.notification_info_dto import NotificationInfoDto
from puupee-api.models.notification_info_dto_paged_result_dto import NotificationInfoDtoPagedResultDto
from puupee-api.models.object_extensions_dto import ObjectExtensionsDto
from puupee-api.models.parameter_api_description_model import ParameterApiDescriptionModel
from puupee-api.models.pending_renewal_info import PendingRenewalInfo
from puupee-api.models.permission_grant_info_dto import PermissionGrantInfoDto
from puupee-api.models.permission_group_dto import PermissionGroupDto
from puupee-api.models.profile_dto import ProfileDto
from puupee-api.models.property_api_description_model import PropertyApiDescriptionModel
from puupee-api.models.provider_info_dto import ProviderInfoDto
from puupee-api.models.puupee_changed_eto import PuupeeChangedEto
from puupee-api.models.puupee_dto import PuupeeDto
from puupee-api.models.puupee_dto_paged_result_dto import PuupeeDtoPagedResultDto
from puupee-api.models.receipt import Receipt
from puupee-api.models.refresh_device_status_dto import RefreshDeviceStatusDto
from puupee-api.models.register_dto import RegisterDto
from puupee-api.models.remote_service_error_info import RemoteServiceErrorInfo
from puupee-api.models.remote_service_error_response import RemoteServiceErrorResponse
from puupee-api.models.remote_service_validation_error_info import RemoteServiceValidationErrorInfo
from puupee-api.models.reset_password_dto import ResetPasswordDto
from puupee-api.models.return_value_api_description_model import ReturnValueApiDescriptionModel
from puupee-api.models.send_password_reset_code_dto import SendPasswordResetCodeDto
from puupee-api.models.send_test_email_input import SendTestEmailInput
from puupee-api.models.send_verification_code_dto import SendVerificationCodeDto
from puupee-api.models.settings_dto import SettingsDto
from puupee-api.models.simple_data_dto import SimpleDataDto
from puupee-api.models.simple_data_dto_paged_result_dto import SimpleDataDtoPagedResultDto
from puupee-api.models.storage_object_credentials import StorageObjectCredentials
from puupee-api.models.storage_object_dto import StorageObjectDto
from puupee-api.models.storage_object_or_credentials_dto import StorageObjectOrCredentialsDto
from puupee-api.models.string_key_value import StringKeyValue
from puupee-api.models.string_set_key_value_dto import StringSetKeyValueDto
from puupee-api.models.subscription_dto import SubscriptionDto
from puupee-api.models.subscription_order_dto import SubscriptionOrderDto
from puupee-api.models.subscription_order_status import SubscriptionOrderStatus
from puupee-api.models.subscription_order_type import SubscriptionOrderType
from puupee-api.models.sync_state_dto import SyncStateDto
from puupee-api.models.tenant_create_dto import TenantCreateDto
from puupee-api.models.tenant_dto import TenantDto
from puupee-api.models.tenant_dto_paged_result_dto import TenantDtoPagedResultDto
from puupee-api.models.tenant_update_dto import TenantUpdateDto
from puupee-api.models.test_date_time import TestDateTime
from puupee-api.models.time_zone import TimeZone
from puupee-api.models.timing_dto import TimingDto
from puupee-api.models.todo_order_by import TodoOrderBy
from puupee-api.models.todo_settings_dto import TodoSettingsDto
from puupee-api.models.type_api_description_model import TypeApiDescriptionModel
from puupee-api.models.update_email_settings_dto import UpdateEmailSettingsDto
from puupee-api.models.update_feature_dto import UpdateFeatureDto
from puupee-api.models.update_features_dto import UpdateFeaturesDto
from puupee-api.models.update_permission_dto import UpdatePermissionDto
from puupee-api.models.update_permissions_dto import UpdatePermissionsDto
from puupee-api.models.update_profile_dto import UpdateProfileDto
from puupee-api.models.user_data import UserData
from puupee-api.models.user_data_list_result_dto import UserDataListResultDto
from puupee-api.models.user_login_info import UserLoginInfo
from puupee-api.models.user_storage_dto import UserStorageDto
from puupee-api.models.user_storage_item_dto import UserStorageItemDto
from puupee-api.models.verify_password_reset_token_input import VerifyPasswordResetTokenInput
from puupee-api.models.verify_receipt_dto import VerifyReceiptDto
from puupee-api.models.verify_receipt_result import VerifyReceiptResult
from puupee-api.models.windows_time_zone import WindowsTimeZone

