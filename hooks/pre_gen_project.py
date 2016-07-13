from shutil import copyfile
import os

#print os.listdir(os.getcwd())
copyfile('{{cookiecutter.project_name}}' + "./spec/datamodel.xml", "./template/{{cookiecutter.project_slug}}/datamodel.xml")