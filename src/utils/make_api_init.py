# Generates __init__.py at ./apps/<project_name>/api/__init__.py

import os
import textwrap

class ApiInit(object):

    BASE_IMPORT = """from flask_restplus import Api"""
    BASE_MODEL_IMPORT = """from .ns_[[MODEL]] import api as ns[[MODEL_INDEX]]"""
    BASE_INSTANCE = textwrap.dedent(
        """
        api = Api(
            title='[[TITLE]]',
            version='1.0',
            description='[[DESCRIPTION]]',
            doc='/api/v1'
        )
        """
    )
    BASE_MODEL_INSERT = """api.add_namespace(ns[[MODEL_INDEX]], path='/api/v1/[[MODEL]]s')"""

    def __init__(self, **kwargs):
        self.path = kwargs['api_path']
        self.title = kwargs['name']
        self.desc = kwargs['description']
        self.models = kwargs['models']

        self.part1 = ApiInit.BASE_IMPORT
        self.part2 = ApiInit.BASE_MODEL_IMPORT
        self.part3 = ApiInit.BASE_INSTANCE
        self.part4 = ApiInit.BASE_MODEL_INSERT

    def _build_ns_import(self, m_index, model):
        ns_import = self.part2.replace('[[MODEL]]', model)
        ns_import = ns_import.replace('[[MODEL_INDEX]]', str(m_index + 1))
        return ns_import

    def _build_instance_meta(self):
        ns_instance = self.part3.replace('[[TITLE]]', self.title)
        ns_instance = ns_instance.replace('[[DESCRIPTION]]', self.desc)
        return ns_instance

    def _build_ns_insert(self, m_index, model):
        ns_insert = self.part4.replace('[[MODEL]]', model)
        ns_insert = ns_insert.replace('[[MODEL_INDEX]]', str(m_index + 1))
        return ns_insert

    def create_file(self):
        content = []
        content.append(self.part1)
        content.append('\n')

        for i, m in enumerate(self.models):
            part2 = ApiInit._build_ns_import(self, m_index=i, model=m)
            content.append(part2)

        part3 = ApiInit._build_instance_meta(self)
        content.append(part3)

        for i, m in enumerate(self.models):
            part4 = ApiInit._build_ns_insert(self, m_index=i, model=m)
            content.append(part4)

        content_string = '\n'.join(content)

        new_file = open(self.path + '/__init__.py', 'a')
        new_file.write(content_string)
        new_file.close()

        print('SUCCESS: API __init__.py file created.')