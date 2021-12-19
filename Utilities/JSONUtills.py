import json


class JSONUtils:

    def load_data_from_file(self,filepath):
        with open(filepath) as f:
            json_data= json.load(f)
        return json_data