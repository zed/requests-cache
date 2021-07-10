% Note: backend module docs are auto-generated with apidoc; the remaining modules are manually
% added here for more custom formatting.

# API Reference
This section covers all the public interfaces of requests-cache.

## Sessions
% Explicitly show inherited method docs on CachedSession instead of CachedMixin
```{eval-rst}
.. autoclass:: requests_cache.session.CachedSession
    :members: send, request, cache_disabled, remove_expired_responses
    :show-inheritance:
```

```{eval-rst}
.. autoclass:: requests_cache.session.CacheMixin
```

## Patching
```{eval-rst}
.. automodule:: requests_cache.patcher
    :members:
```

## Responses
```{eval-rst}
.. autoclass:: requests_cache.response.CachedResponse
    :members:
    :inherited-members:
    :show-inheritance:
```

```{eval-rst}
.. autoclass:: requests_cache.response.CachedHTTPResponse
    :members:
    :inherited-members:
    :show-inheritance:
```

## Utilities
```{eval-rst}
.. automodule:: requests_cache.cache_keys
    :members:
```

```{eval-rst}
.. automodule:: requests_cache.cache_control
    :members:
```

## Cache Backends
% Sources for this sub-package will be autogenerated by sphinx-apidoc
```{toctree}
modules/requests_cache.backends
```