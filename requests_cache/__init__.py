# flake8: noqa: E402,F401
from logging import getLogger

# Version is defined in pyproject.toml.
# It's copied here to make it easier for client code to check the installed version.
__version__ = '1.0.0'

try:
    from .backends import *
    from .cache_keys import *
    from .models import *
    from .patcher import *
    from .policy import *
    from .serializers import *
    from .session import *
# Log and ignore ImportErrors, if imported outside a virtualenv (e.g., just to check __version__)
except ImportError as e:
    getLogger('requests_cache').warning(e, exc_info=True)


__all__ = [
    # Constants
    'ALL_METHODS',
    'BACKEND_CLASSES',
    'DO_NOT_CACHE',
    'NEVER_EXPIRE',
    'EXPIRE_IMMEDIATELY',
    'SERIALIZERS',
    # Main classes
    'CachedHTTPResponse',
    'CachedRequest',
    'CachedResponse',
    'CachedSession',
    'CacheMixin',
    # Backends
    'BaseCache',
    'DynamoCache',
    'FileCache',
    'GridFSCache',
    'MongoCache',
    'RedisCache',
    'SQLiteCache',
    # Serializers
    'SerializerPipeline',
    'Stage',
    'CattrStage',
    'init_serializer',
    'bson_serializer',
    'json_serializer',
    'pickle_serializer',
    'safe_pickle_serializer',
    'yaml_serializer',
    # Patching/wrapper functions
    'clear',
    'disabled',
    'enabled',
    'get_cache',
    'install_cache',
    'is_installed',
    'remove_expired_responses',
    # Types & utility functions
    'AnyRequest',
    'AnyResponse',
    'CacheActions',
    'create_key',
]
