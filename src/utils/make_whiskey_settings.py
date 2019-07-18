# Generates JSON settings file at ./apps/<project_name>/whiskey.json

import json

class WhiskeySettings(object):

    DATA = {
        'meta' : {
            'name' : None,
            'description' : None,
            'version' : None,
        },
        'models' : [],   
    }

    def __init__(self, **kwargs):
        self.settings = WhiskeySettings.DATA

        self.path = kwargs['base_path'] #str

        self.name = kwargs['name']
        self.description = kwargs['description']
        self.version = '1.0' #default for now

        self.models = kwargs['models'] #list

    def _update_settings(self):
        self.settings['meta']['name'] = self.name
        self.settings['meta']['version'] = self.version
        self.settings['meta']['description'] = self.description

        self.settings['models'].append(self.models)

    def create_file(self):
        WhiskeySettings._update_settings(self)

        with open(self.path + '/whiskey.json', 'w') as new_file:  
            json.dump(self.settings, new_file)

        print('SUCCESS: Whiskey settings file created.')