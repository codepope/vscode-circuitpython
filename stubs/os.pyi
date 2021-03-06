from typing import Any

"""
os
"""


# shared-bindings/os/__init__.c:52
def uname() -> Any: ...

# shared-bindings/os/__init__.c:62
def chdir(path: Any) -> Any: ...

# shared-bindings/os/__init__.c:73
def getcwd() -> Any: ...

# shared-bindings/os/__init__.c:82
def listdir(dir: Any) -> Any: ...

# shared-bindings/os/__init__.c:97
def mkdir(path: Any) -> Any: ...

# shared-bindings/os/__init__.c:108
def remove(path: Any) -> Any: ...

# shared-bindings/os/__init__.c:119
def rmdir(path: Any) -> Any: ...

# shared-bindings/os/__init__.c:131
def rename(old_path: Any, new_path: Any) -> Any: ...

# shared-bindings/os/__init__.c:142
def stat(path: Any) -> Any: ...

# shared-bindings/os/__init__.c:157
def statvfs(path: Any) -> Any: ...

# shared-bindings/os/__init__.c:184
def sync() -> Any: ...

# shared-bindings/os/__init__.c:197
def urandom(size: Any) -> Any: ...
    sep: Any = ...
