# Generates API namespace at ./apps/<project_name>/apis/<namespace>.py

import os

class ApiNamespace(object):
    
    with open(os.getcwd() + '/utils/namespace_template.txt', 'r') as ns_template:
        NAMESPACE_BASE = ns_template.read()

    def __init__(self, **kwargs):
        self.path = kwargs['path']
        self.ns_base = ApiNamespace.NAMESPACE_BASE
        self.model = kwargs['model']

    def create_file(self):

        MODEL_LOWERCASE = self.model.lower()
        MODEL_PROPERCASE = self.model[0].upper() + self.model[1:].lower()

        ns_content = self.ns_base
        ns_content = ns_content.replace('[[MODEL_LOWERCASE]]', MODEL_LOWERCASE)
        ns_content = ns_content.replace('[[MODEL_PROPERCASE]]', MODEL_PROPERCASE)
        ns_content = ns_content.replace('"""','').strip()

        new_file = open(self.path + '/ns_{}.py'.format(MODEL_LOWERCASE), 'a')
        new_file.write(ns_content)
        new_file.close()

        print('SUCCESS: {} namespace file created.'.format(MODEL_PROPERCASE))