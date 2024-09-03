import yaml
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config", "data.yaml")
f = open(path, encoding="utf-8")

data = yaml.safe_load(f)
print(data)
print(data["hero"])