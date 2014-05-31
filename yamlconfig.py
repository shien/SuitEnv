# encoding: utf8

import yaml

default_filename = 'sample.yaml'

class YamlConfig:
    def open_yaml(self):
        str = open(default_filename).read()
        self.data = yaml.load(str)

    def get_data(self):
        return self.data

if __name__ == "__main__":
    yc = YamlConfig()
    yc.open_yaml()
    data = yc.get_data()
    print(data)
