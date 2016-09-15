from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name='ckanext-eueip_spa',
    version=version,
    description="EU EIP SPA profile to be used with CKAN and the dcat plugin",
    long_description='''\
    ''',
    classifiers=[],
    keywords='',
    author='Erling Børresen',
    author_email='erling.borresen@gmail.com',
    url='https://github.com/vegvesen/ckanext-eueip_spa',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.eueip_spa'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
    [ckan.rdf.profiles]
    eueip_spa=ckanext.eueip_spa_schema.profiles:EUEIPSPAProfile
    ''',
    message_extractors={
        'ckanext': [
            ('**.py', 'python', None),
            ('**.js', 'javascript', None),
            ('**/templates/**.html', 'ckan', None),
        ],
    },
)
