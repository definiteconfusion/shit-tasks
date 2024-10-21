#   ---------------------------------------------------------------------------------
#   Copyright (c) Microsoft Corporation. All rights reserved.
#   Licensed under the MIT License. See LICENSE in project root for information.
#   ---------------------------------------------------------------------------------

from __future__ import annotations
import yaml


class Yaml:
    def __init__(self, path: str="./config.yaml"):
        self.path = path

    def load(self):
        with open(self.path, "r") as file:
            return yaml.safe_load(file)

    def dump(self, data: dict):
        with open(self.path, "w") as file:
            yaml.dump(data, file)

class Files:
    def __init__(self, path: str="./hello_world.txt"):
        self.path = path

    def read(self):
        with open(self.path, "r") as file:
            return file.read()

    def write(self, data: str):
        with open(self.path, "w") as file:
            file.write(data)

class Base64:
    def __init__(self, data: str):
        self.data = data

    def encode(self):
        return self.data.encode("utf-8")

    def decode(self):
        return self.data.encode("utf-8").decode("utf-8")