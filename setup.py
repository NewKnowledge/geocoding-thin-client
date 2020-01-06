from distutils.core import setup

setup(
    name="GoatD3MWrapper",
    version="1.0.8",
    description="A geocoding service from New Knowledge",
    packages=["GoatD3MWrapper"],
    install_requires=["requests>=2.19.1,<=2.22.0", "typing==3.7.4.1"],
    entry_points={
        "d3m.primitives": [
            "data_cleaning.geocoding.Goat_forward = GoatD3MWrapper:goat",
            "data_cleaning.geocoding.Goat_reverse = GoatD3MWrapper:reverse_goat",
        ]
    },
)
