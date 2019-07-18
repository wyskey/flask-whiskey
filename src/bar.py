import os
import click
import textwrap

from utils.make_app import FlaskApp
from utils.make_whiskey_settings import WhiskeySettings
from utils.make_api_namespace import ApiNamespace
from utils.make_api_init import ApiInit

@click.group()
def main():
    """
    Flask-Whiskey: Smooth API generator for Flask-RESTPlus
    """
    pass


@main.command()
@click.option('--name', prompt='Name your service', 
                        help='Will be the name of the top-level folder')
@click.option('--description', prompt='Describe your API',
                        help='Summary description')
@click.option('--models', prompt='List your models (comma-separated)',
                        help='Enter a comma separated list, e.g. project,task,resource')
def create(name, description, models):
    """Scaffolds a new API"""
    model_list = models.replace(' ', '').split(',')
    project_folder_name = name.lower().replace(' ', '_')
    base_path = os.getcwd() + '/apps/' + project_folder_name
    directory_exists = os.path.isdir(base_path)

    if directory_exists:
        project_folder_name = project_folder_name + '_1'

    click.echo('\n')
    click.echo('Creating API called {} with {} resource(s)!'.format(name, len(model_list)))
    click.secho('--------------------', fg='blue')

    # Create directories in the apps subfolder
    new_dirs_to_create = os.getcwd() + '/apps/' + project_folder_name + '/apis'
    os.makedirs(new_dirs_to_create)

    # Generate Flask application
    FlaskApp(base_path).create_file()

    # Generate settings file
    data = {
        'base_path': base_path,
        'api_path': new_dirs_to_create,
        'name': name,
        'description': description,
        'models': model_list,
    }

    WhiskeySettings(**data).create_file()

    # Build namespace file(s)
    for m in model_list:
        ApiNamespace(path=data['api_path'], model=m).create_file()

    # Build init file
    ApiInit(**data).create_file()

    click.secho('--------------------', fg='blue')
    click.echo('\n')

    click.echo('Run the following commands to start your new API server:')
    click.echo('cd apps/{} && python app.py'.format(project_folder_name))

if __name__ == '__main__':
    main()
