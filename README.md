# pytest_networkx

Reproduce the error

```
git clone https://github.com/woutdenolf/pytest_networkx.git
cd pytest_networkx

python setup.py build sdist
pip install dist/myproject-1.0.0.tar.gz[test]

pytest --pyargs myproject -W error
```

In python 3.9 there seem to be two entry points for `networkx.backends`.
This does not happen for python 3.8, 3.10 or 3.11.

```
=================================== test session starts ====================================
platform linux -- Python 3.9.18, pytest-8.1.1, pluggy-1.4.0
rootdir: /home/denolf/projects/pytest_networkx
configfile: pyproject.toml
collecting ... 
==============networkx=============
networkx.backends EntryPoint(name='nx-loopback', value='networkx.classes.tests.dispatch_interface:dispatcher', group='networkx.backends')
networkx.backends EntryPoint(name='nx-loopback', value='networkx.classes.tests.dispatch_interface:dispatcher', group='networkx.backends')
====================================
collected 0 items / 1 error                                                                

========================================== ERRORS ==========================================
__________________________________ ERROR collecting tests __________________________________
../../.pyenv/versions/3.9.18/lib/python3.9/importlib/__init__.py:127: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1030: in _gcd_import
    ???
<frozen importlib._bootstrap>:1007: in _find_and_load
    ???
<frozen importlib._bootstrap>:986: in _find_and_load_unlocked
    ???
<frozen importlib._bootstrap>:680: in _load_unlocked
    ???
../../virtualenvs/pybox_ssyjHF/lib/python3.9/site-packages/_pytest/assertion/rewrite.py:178: in exec_module
    exec(co, module.__dict__)
../../virtualenvs/pybox_ssyjHF/lib/python3.9/site-packages/myproject/tests/conftest.py:30: in <module>
    import networkx
../../virtualenvs/pybox_ssyjHF/lib/python3.9/site-packages/networkx/__init__.py:20: in <module>
    from networkx.utils.backends import _dispatch
../../virtualenvs/pybox_ssyjHF/lib/python3.9/site-packages/networkx/utils/backends.py:135: in <module>
    backends.update(_get_backends("networkx.backends"))
../../virtualenvs/pybox_ssyjHF/lib/python3.9/site-packages/networkx/utils/backends.py:110: in _get_backends
    warnings.warn(
E   RuntimeWarning: networkx backend defined more than once: nx-loopback
================================= short test summary info ==================================
ERROR tests - RuntimeWarning: networkx backend defined more than once: nx-loopback
!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!
===================================== 1 error in 0.14s =====================================
```
