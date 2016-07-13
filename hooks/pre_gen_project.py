from shutil import copyfile
import os

#print os.listdir(os.getcwd())
copyfile('{{cookiecutter.app_name}}' + "./spec/datamodel.xml", "./template/{{cookiecutter.project_slug}}/datamodel.xml")