import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-l10n-germany",
    description="Meta package for oca-l10n-germany Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-l10n_de_country_states',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
