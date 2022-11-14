from urllib import request
from project import Project
from toml import loads

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(loads(content))
        toml_parsed = loads(content)
        toml_project = Project(
            toml_parsed['tool']['poetry']['name'],
            toml_parsed['tool']['poetry']['description'],
            toml_parsed['tool']['poetry']['dependencies'],
            toml_parsed['tool']['poetry']['dev-dependencies']
        )
        return toml_project

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        #return Project("Test name", "Test description", [], [])
