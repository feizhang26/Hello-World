
from setuptools import setup, find_packages

setup(
    name           = 'EggDemo',
    version        = '1.0',
    packages       = find_packages(),
    #package_dir    = {'':'src'},
    include_package_data = True,    # include everything in source control
    #other items of package managerment
    #http://peak.telecommunity.com/DevCenter/setuptools
    #package_data
    package_data = {
        #include all .sh, .sta, .ap, .conf, .json files
        '':['*.sh', '*.sta', '*.ap', '*.conf', '*.json'],
    },
    #include_package_data
    #exclude_package_data
    zip_safe=False,
    author      = 'feizhang',
    author_email = 'feizhangshare@outlook.com',
    url         = 'https://github.com/feizhang26',
    description = 'This is for egg test',
)