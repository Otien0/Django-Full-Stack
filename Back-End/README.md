# Django Intro:
Django is a free and open source web framework.
It is used by many sites, including Pinterest, PBS, Instagram, BitBucket, Washington Times, Mozilla, and more!
Django was created in 2003 when the web developers at the Lawrence Journal-World newspaper started using Python for their development.
The fact that is originated at a newspaper is important!	
When encountering Django tutorials you will often read that you should create a virtual environment or an “venv”
A virtual environment allows you to have a virtual installation of Python and packages on your computer.
To use a virtual environment with conda we use these commands:
conda create --name myEnv django
Here we created an environment called “myEnv” with the latest version of Django.
You can then activate the environment:
activate myEnv 
Now, anything installed with pip or conda when this environment is activated, will only be installed for this environment.
You can then deactivate the environment 
deactivate myEnv 
Its encouraged to use virtual environments for your projects to keep them self-contained and not run into issues when packages update!

When you install Django, it actually also installed a command line tool called:
django-admin

>>>>>>before starting, Begin with: source activate MyDjangoEnv >>>>>>>>>>

# Useful Links:
#               https://docs.djangoproject.com/en/3.0/
#               https://docs.djangoproject.com/en/3.0/ref/models/fields/#foreignkey
#               https://docs.djangoproject.com/en/3.0/topics/auth/passwords/#password-validation

# Link to some features that previously were in django 1.9+, that were removed in Django 2.0 & Django 3.0;
#               https://docs.djangoproject.com/en/3.0/releases/1.9/#features-deprecated-in-1-9s
