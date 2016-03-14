
import codecs
import distutils.core

version = '0.1'

distutils.core.setup(
    name="AMAN_Synthetic_Data",
    version=version,
    packages=['aman_py', 'aman_py.Synthetic_Data'],
    package_data={
        'aman_py': [
            'DATA/cities',
            'DATA/colors',
            'DATA/company_names',
            'DATA/continents',
            'DATA/countries',
            'DATA/country_code_top_level_domains',
            'DATA/currency_codes',
            'DATA/currency_descriptions',
            'DATA/female_first_names',
            'DATA/frequencies',
            'DATA/genders',
            'DATA/industries',
            'DATA/job_title_suffixes',
            'DATA/job_titles',
            'DATA/languages',
            'DATA/last_names',
            'DATA/locations',
            'DATA/lorem_ipsum',
            'DATA/male_first_names',
            'DATA/name_suffixes',
            'DATA/name_titles',
            'DATA/province_abbrevs',
            'DATA/provinces',
            'DATA/races',
            'DATA/shirt_sizes',
            'DATA/state_abbrevs',
            'DATA/states',
            'DATA/street_names',
            'DATA/street_suffixes',
            'DATA/top_level_domains',
            'DATA/zones'
        ]
    },
    author=u'AMAN OMKAR',
    author_email='iitp.aman@gmail.com',
    description='An easy to use synthetic data generator for Python',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ]
)
