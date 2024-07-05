from core.core.utils import deep_update
from core.core.utils.settings import get_settings_from_env

deep_update(globals(),get_settings_from_env(ENVVAR_SETTINGS_PREFIX))