from fastapi import Depends

from fint_multiuser_example.config import get_config
from fint_multiuser_example.config import FintMultiuserConfig as Config
from fint_rtc_server.config import FintRTCServerConfig, get_config as get_server_config
from fint_rtc_server.multiuser.manager import UidMappedUserManager

from .logger import logger


def get_user_manager():
    def _(
        config: Config = Depends(get_config),
        server_config: FintRTCServerConfig = Depends(get_server_config),
    ):
        logger.info('example multi user')
        return UidMappedUserManager(server_config.content_dir)

    return _
