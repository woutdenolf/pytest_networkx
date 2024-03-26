import sys

if sys.version_info < (3, 9):
    from importlib_metadata import entry_points as _entry_points

    def iter_entry_points(group: str):
        return _entry_points(group=group)

elif sys.version_info < (3, 10):
    from importlib.metadata import entry_points as _entry_points

    def iter_entry_points(group: str):
        return _entry_points().get(group, [])

else:
    from importlib.metadata import entry_points as _entry_points

    def iter_entry_points(group: str):
        return _entry_points(group=group)


print()
print("==============networkx=============")
for ep in iter_entry_points("networkx.backends"):
    print("networkx.backends", ep)
for ep in iter_entry_points("networkx.backend_info"):
    print("networkx.backend_info", ep)
print("====================================")

import networkx
