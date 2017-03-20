# Exploit the import mechanism in Python.
import importlib.abc
import logging
import sys

logging.getLogger().setLevel(logging.INFO)

if sys.version_info.major == 2:
    class LoggingImporter(importlib.abc.Finder):
        def find_module(self, name, path=None):
            msg = "importing {} on {}".format(name, path)
            logging.info(msg)
            return None  # None means "didn't match", move on to the next path Finder
    sys.meta_path.append(LoggingImporter())

    class BlockingFinder(importlib.abc.Finder):
        def find_module(self, name, path=None):
            if name in ['numpy']:
                return BlockingLoader()
    class BlockingLoader(importlib.abc.Loader):
        def load_module(self, fullname):
            if fullname not in sys.modules:
                raise ImportError("Can't import excluded module {}".format(fullname))
            return sys.modules[fullname]
    sys.meta_path.append(BlockingFinder())

    # combined in one single class:
    class BlockingImporter(importlib.abc.Finder, importlib.abc.Loader):
        def find_module(self, name, path=None):
            if name in ['numpy']:
                return self
        def load_module(self, fullname):
            if fullname not in sys.modules:
                raise ImportError("Can't import excluded module {}".format(fullname))
            return sys.modules[fullname]
    sys.meta_path.append(BlockingImporter())
