from shutil import copyfile

copyfile("./spec/datamode.xml", "./template/{{cookiecutter.project_slug}}/datamodel.xml")