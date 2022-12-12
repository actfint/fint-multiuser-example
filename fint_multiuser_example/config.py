from fps.config import PluginModel
from fps.config import get_config as fps_get_config
from fps.hooks import register_config, register_plugin_name


class FintMultiuserConfig(PluginModel):
    cluster: bool = False


def get_config():
    return fps_get_config(FintMultiuserConfig)


c = register_config(FintMultiuserConfig)
n = register_plugin_name("fint-multiuser")
