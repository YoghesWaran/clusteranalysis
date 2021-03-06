"""
Authors: Wouter Van Gansbeke, Simon Vandenhende
Licensed under the CC BY-NC 4.0 license (https://creativecommons.org/licenses/by-nc/4.0/)
"""
import os


class MyPath(object):
    @staticmethod
    def db_root_dir(database=''):
        db_names = {'cifar-10', 'stl-10', 'cifar-20', 'imagenet', 'imagenet_50', 'imagenet_100', 'imagenet_200'}
        assert(database in db_names)

        if database == 'cifar-10':
            return '/path/to/cifar-10/'
        
        elif database == 'cifar-20':
            return '/path/to/cifar-20/'

        elif database == 'stl-10':
            return '/content/clusteranalysis/data/stl10_binary.tar.gz'
        
        elif database in ['imagenet', 'imagenet_50', 'imagenet_100', 'imagenet_200']:
            return '/path/to/imagenet/'
        
        else:
            raise NotImplementedError
