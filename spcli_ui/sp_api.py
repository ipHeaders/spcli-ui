import yaml
from pathlib import Path
from pyedgeconnect import Orchestrator

class BaseConnection:

     def __init__(self):
        home = str(Path.home())
        with open(f"{home}/.spcli/creds.yml", "r") as stream:
            try:
                yml_vars = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)        
    
        self.url = yml_vars['url']
        self.token = yml_vars['token']


class APPLIANCE(BaseConnection):
    def __init__(self,):
        super().__init__()   

    def _get_appliances_all(self):
        try:
            orch = Orchestrator(self.url, verify_ssl=True, api_key=self.token)
            orch_return = orch.get_appliances()
            return orch_return
        except Exception as e:
            print(e)
