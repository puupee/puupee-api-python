# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from puupee-api.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from puupee-api.model.anv2 import ANV2
from puupee-api.model.abp_login_result import AbpLoginResult
from puupee-api.model.action_api_description_model import ActionApiDescriptionModel
from puupee-api.model.app_dto import AppDto
from puupee-api.model.app_dto_paged_result_dto import AppDtoPagedResultDto
from puupee-api.model.app_feature_dto import AppFeatureDto
from puupee-api.model.app_pricing_dto import AppPricingDto
from puupee-api.model.app_pricing_dto_paged_result_dto import AppPricingDtoPagedResultDto
from puupee-api.model.app_pricing_item_dto import AppPricingItemDto
from puupee-api.model.app_release_dto import AppReleaseDto
from puupee-api.model.app_release_dto_paged_result_dto import AppReleaseDtoPagedResultDto
from puupee-api.model.app_sdk_dto import AppSdkDto
from puupee-api.model.app_theme import AppTheme
from puupee-api.model.app_theme_mode import AppThemeMode
from puupee-api.model.app_user_score_dto import AppUserScoreDto
from puupee-api.model.app_with_user_dto import AppWithUserDto
from puupee-api.model.app_with_user_dto_paged_result_dto import AppWithUserDtoPagedResultDto
from puupee-api.model.application_api_description_model import ApplicationApiDescriptionModel
from puupee-api.model.application_auth_configuration_dto import ApplicationAuthConfigurationDto
from puupee-api.model.application_configuration_dto import ApplicationConfigurationDto
from puupee-api.model.application_feature_configuration_dto import ApplicationFeatureConfigurationDto
from puupee-api.model.application_global_feature_configuration_dto import ApplicationGlobalFeatureConfigurationDto
from puupee-api.model.application_localization_configuration_dto import ApplicationLocalizationConfigurationDto
from puupee-api.model.application_localization_dto import ApplicationLocalizationDto
from puupee-api.model.application_localization_resource_dto import ApplicationLocalizationResourceDto
from puupee-api.model.application_setting_configuration_dto import ApplicationSettingConfigurationDto
from puupee-api.model.bind_device_dto import BindDeviceDto
from puupee-api.model.boolean_key_value import BooleanKeyValue
from puupee-api.model.boolean_set_key_value_dto import BooleanSetKeyValueDto
from puupee-api.model.change_password_input import ChangePasswordInput
from puupee-api.model.clock_dto import ClockDto
from puupee-api.model.controller_api_description_model import ControllerApiDescriptionModel
from puupee-api.model.controller_interface_api_description_model import ControllerInterfaceApiDescriptionModel
from puupee-api.model.create_message_template_release_dto import CreateMessageTemplateReleaseDto
from puupee-api.model.create_open_iddict_application_dto import CreateOpenIddictApplicationDto
from puupee-api.model.create_or_update_app_dto import CreateOrUpdateAppDto
from puupee-api.model.create_or_update_app_feature_dto import CreateOrUpdateAppFeatureDto
from puupee-api.model.create_or_update_app_pricing_dto import CreateOrUpdateAppPricingDto
from puupee-api.model.create_or_update_app_pricing_item_dto import CreateOrUpdateAppPricingItemDto
from puupee-api.model.create_or_update_app_release_dto import CreateOrUpdateAppReleaseDto
from puupee-api.model.create_or_update_app_sdk_dto import CreateOrUpdateAppSdkDto
from puupee-api.model.create_or_update_app_user_score_dto import CreateOrUpdateAppUserScoreDto
from puupee-api.model.create_or_update_message_template_dto import CreateOrUpdateMessageTemplateDto
from puupee-api.model.create_or_update_puupee_dto import CreateOrUpdatePuupeeDto
from puupee-api.model.create_push_notification_dto import CreatePushNotificationDto
from puupee-api.model.current_culture_dto import CurrentCultureDto
from puupee-api.model.current_tenant_dto import CurrentTenantDto
from puupee-api.model.current_user_dto import CurrentUserDto
from puupee-api.model.date_time_format_dto import DateTimeFormatDto
from puupee-api.model.date_time_key_value import DateTimeKeyValue
from puupee-api.model.date_time_set_key_value_dto import DateTimeSetKeyValueDto
from puupee-api.model.decimal_key_value import DecimalKeyValue
from puupee-api.model.decimal_set_key_value_dto import DecimalSetKeyValueDto
from puupee-api.model.device_dto import DeviceDto
from puupee-api.model.device_dto_paged_result_dto import DeviceDtoPagedResultDto
from puupee-api.model.double_key_value import DoubleKeyValue
from puupee-api.model.double_set_key_value_dto import DoubleSetKeyValueDto
from puupee-api.model.email_settings_dto import EmailSettingsDto
from puupee-api.model.entity_extension_dto import EntityExtensionDto
from puupee-api.model.extension_enum_dto import ExtensionEnumDto
from puupee-api.model.extension_enum_field_dto import ExtensionEnumFieldDto
from puupee-api.model.extension_property_api_create_dto import ExtensionPropertyApiCreateDto
from puupee-api.model.extension_property_api_dto import ExtensionPropertyApiDto
from puupee-api.model.extension_property_api_get_dto import ExtensionPropertyApiGetDto
from puupee-api.model.extension_property_api_update_dto import ExtensionPropertyApiUpdateDto
from puupee-api.model.extension_property_attribute_dto import ExtensionPropertyAttributeDto
from puupee-api.model.extension_property_dto import ExtensionPropertyDto
from puupee-api.model.extension_property_ui_dto import ExtensionPropertyUiDto
from puupee-api.model.extension_property_ui_form_dto import ExtensionPropertyUiFormDto
from puupee-api.model.extension_property_ui_lookup_dto import ExtensionPropertyUiLookupDto
from puupee-api.model.extension_property_ui_table_dto import ExtensionPropertyUiTableDto
from puupee-api.model.feature_dto import FeatureDto
from puupee-api.model.feature_group_dto import FeatureGroupDto
from puupee-api.model.feature_provider_dto import FeatureProviderDto
from puupee-api.model.find_tenant_result_dto import FindTenantResultDto
from puupee-api.model.get_feature_list_result_dto import GetFeatureListResultDto
from puupee-api.model.get_permission_list_result_dto import GetPermissionListResultDto
from puupee-api.model.i_string_value_type import IStringValueType
from puupee-api.model.i_value_validator import IValueValidator
from puupee-api.model.iana_time_zone import IanaTimeZone
from puupee-api.model.identity_role_create_dto import IdentityRoleCreateDto
from puupee-api.model.identity_role_dto import IdentityRoleDto
from puupee-api.model.identity_role_dto_list_result_dto import IdentityRoleDtoListResultDto
from puupee-api.model.identity_role_dto_paged_result_dto import IdentityRoleDtoPagedResultDto
from puupee-api.model.identity_role_update_dto import IdentityRoleUpdateDto
from puupee-api.model.identity_user_create_dto import IdentityUserCreateDto
from puupee-api.model.identity_user_dto import IdentityUserDto
from puupee-api.model.identity_user_dto_paged_result_dto import IdentityUserDtoPagedResultDto
from puupee-api.model.identity_user_update_dto import IdentityUserUpdateDto
from puupee-api.model.identity_user_update_roles_dto import IdentityUserUpdateRolesDto
from puupee-api.model.int32_key_value import Int32KeyValue
from puupee-api.model.int32_set_key_value_dto import Int32SetKeyValueDto
from puupee-api.model.interface_method_api_description_model import InterfaceMethodApiDescriptionModel
from puupee-api.model.language_info import LanguageInfo
from puupee-api.model.localizable_string_dto import LocalizableStringDto
from puupee-api.model.login_result_type import LoginResultType
from puupee-api.model.message_publish_dto import MessagePublishDto
from puupee-api.model.message_recall_dto import MessageRecallDto
from puupee-api.model.message_subscribe_dto import MessageSubscribeDto
from puupee-api.model.message_template_dto import MessageTemplateDto
from puupee-api.model.message_template_release_dto import MessageTemplateReleaseDto
from puupee-api.model.message_unsubscribe_dto import MessageUnsubscribeDto
from puupee-api.model.method_parameter_api_description_model import MethodParameterApiDescriptionModel
from puupee-api.model.module_api_description_model import ModuleApiDescriptionModel
from puupee-api.model.module_extension_dto import ModuleExtensionDto
from puupee-api.model.multi_tenancy_info_dto import MultiTenancyInfoDto
from puupee-api.model.name_value import NameValue
from puupee-api.model.notification_info_dto import NotificationInfoDto
from puupee-api.model.notification_info_dto_paged_result_dto import NotificationInfoDtoPagedResultDto
from puupee-api.model.object_extensions_dto import ObjectExtensionsDto
from puupee-api.model.parameter_api_description_model import ParameterApiDescriptionModel
from puupee-api.model.permission_grant_info_dto import PermissionGrantInfoDto
from puupee-api.model.permission_group_dto import PermissionGroupDto
from puupee-api.model.profile_dto import ProfileDto
from puupee-api.model.property_api_description_model import PropertyApiDescriptionModel
from puupee-api.model.provider_info_dto import ProviderInfoDto
from puupee-api.model.puupee_changed_eto import PuupeeChangedEto
from puupee-api.model.puupee_dto import PuupeeDto
from puupee-api.model.puupee_dto_paged_result_dto import PuupeeDtoPagedResultDto
from puupee-api.model.refresh_device_status_dto import RefreshDeviceStatusDto
from puupee-api.model.register_dto import RegisterDto
from puupee-api.model.remote_service_error_info import RemoteServiceErrorInfo
from puupee-api.model.remote_service_error_response import RemoteServiceErrorResponse
from puupee-api.model.remote_service_validation_error_info import RemoteServiceValidationErrorInfo
from puupee-api.model.reset_password_dto import ResetPasswordDto
from puupee-api.model.return_value_api_description_model import ReturnValueApiDescriptionModel
from puupee-api.model.send_password_reset_code_dto import SendPasswordResetCodeDto
from puupee-api.model.send_test_email_input import SendTestEmailInput
from puupee-api.model.send_verification_code_dto import SendVerificationCodeDto
from puupee-api.model.settings_dto import SettingsDto
from puupee-api.model.simple_data_dto import SimpleDataDto
from puupee-api.model.simple_data_dto_paged_result_dto import SimpleDataDtoPagedResultDto
from puupee-api.model.storage_object_credentials import StorageObjectCredentials
from puupee-api.model.storage_object_dto import StorageObjectDto
from puupee-api.model.storage_object_or_credentials_dto import StorageObjectOrCredentialsDto
from puupee-api.model.string_key_value import StringKeyValue
from puupee-api.model.string_set_key_value_dto import StringSetKeyValueDto
from puupee-api.model.sync_state_dto import SyncStateDto
from puupee-api.model.tenant_create_dto import TenantCreateDto
from puupee-api.model.tenant_dto import TenantDto
from puupee-api.model.tenant_dto_paged_result_dto import TenantDtoPagedResultDto
from puupee-api.model.tenant_update_dto import TenantUpdateDto
from puupee-api.model.test_date_time import TestDateTime
from puupee-api.model.time_zone import TimeZone
from puupee-api.model.timing_dto import TimingDto
from puupee-api.model.todo_order_by import TodoOrderBy
from puupee-api.model.todo_settings_dto import TodoSettingsDto
from puupee-api.model.type_api_description_model import TypeApiDescriptionModel
from puupee-api.model.update_email_settings_dto import UpdateEmailSettingsDto
from puupee-api.model.update_feature_dto import UpdateFeatureDto
from puupee-api.model.update_features_dto import UpdateFeaturesDto
from puupee-api.model.update_permission_dto import UpdatePermissionDto
from puupee-api.model.update_permissions_dto import UpdatePermissionsDto
from puupee-api.model.update_profile_dto import UpdateProfileDto
from puupee-api.model.user_data import UserData
from puupee-api.model.user_data_list_result_dto import UserDataListResultDto
from puupee-api.model.user_login_info import UserLoginInfo
from puupee-api.model.user_storage_dto import UserStorageDto
from puupee-api.model.user_storage_item_dto import UserStorageItemDto
from puupee-api.model.verify_password_reset_token_input import VerifyPasswordResetTokenInput
from puupee-api.model.windows_time_zone import WindowsTimeZone
