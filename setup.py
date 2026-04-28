from setuptools import find_packages, setup

setup(
    name="ml_privacy_meter_local",
    version="0.1.0",
    py_modules=[
        "audit",
        "attacks",
        "get_signals",
        "util",
        "visualize", 
    ],
    packages=find_packages()
)