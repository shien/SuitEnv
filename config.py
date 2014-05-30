# encoding: utf8

import yaml

class YamlConfig:
    def open_yaml(self):
        str = open('conf.yaml').read()
        data = yaml.load(str)

        print(repr(data))
