import importlib
import pkgutil
import pathlib
import sys

PACKAGE_PATH = pathlib.Path(__file__).parent / "infrastructure"
PACKAGE_NAME = "ecSiteAnalysis.infrastructure"


def recursive_import_models(package_path: pathlib.Path, package_prefix: str):
    for finder, name, ispkg in pkgutil.iter_modules([str(package_path)]):
        full_module_name = f"{package_prefix}.{name}"
        try:
            importlib.import_module(full_module_name)
        except Exception as e:
            print(e, file=sys.stderr)

        sub_path = package_path / name
        if ispkg:
            recursive_import_models(sub_path, full_module_name)


recursive_import_models(PACKAGE_PATH, PACKAGE_NAME)