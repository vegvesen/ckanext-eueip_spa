# ckanext-eueip_spa

NB! This is still a work in progress, not ready for use yet!

This is a collection of stuff needed to make CKAN conform to EU EIP SPA.

## Requirements

Install the plugins `ckanext-dcat` and `ckanext-scheming` and configure them accordingly.

#### Note!


Until `ckanext-dcat` has merged [PR#66](https://github.com/ckan/ckanext-dcat/pull/66) you have to install from the fork using
    
    (pyenv) $ pip install -e git+https://github.com/vegvesen/ckanext-dcat.git@feature/dcat-ap11#egg=ckanext-dcat

## Installation


1.  Install the package

        (pyenv) $ pip install -e git+https://github.com/vegvesen/ckanext-eueip_spa.git#egg=ckanext-eueip_spa

2.  Set the dcat profile in your configuration file:

        ckanext.dcat.rdf.profiles = eueip_spa

3.  Enable the dataset schema in your configuration file:

        scheming.dataset_schemas = ckanext.eueip_spa:eueip_spa_schema.json
