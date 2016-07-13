from shutil import copyfile

copyfile("./spec/datamodel.xml", "./template/{{cookiecutter.project_slug}}/datamodel.xml")