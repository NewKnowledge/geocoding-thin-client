from distutils.core import setup

setup(name='GoatD3MWrapper',
    version='1.0.5',
    description='A geocoding service from New Knowledge',
    packages=['GoatD3MWrapper'],
    install_requires=["requests","typing"],
    entry_points = {
        'd3m.primitives': [
            'data_cleaning.multitable_featurization.Goat.forward = GoatD3MWrapper:goat',
            'data_cleaning.multitable_featurization.Goat.reverse = GoatD3MWrapper:reverse_goat'
        ],
    },
)
