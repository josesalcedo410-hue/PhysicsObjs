# PhysicsObjs

This is the README for the PhysicsObjs project.

Description:

Features:

Installation:

Installation can be done through the terminal with git
    -git clone https/github.com/josesalcedo410-hue/PhysicsObjs
    
The package can be installed through pip by using in the command window.
With the terminal at the location of the pyproject.toml run
    -pip install .
    
If this results in an UNKOWN package the setuptools or pip is outdated this can be fixed by upgrading pip
This can be done by running the command 
    -pip install --upgrade pip
    
This will allow pip and the setuptools to read the toml file correctly.
In an unwanted UNKOWN package was installed it can be unistalled by running 
    -pip uninstall UNKOWN -y
    
This will remove the UNKOWN package
Now with the updated pip, and the terminal at the location of the pyproject.toml file
    pip install .
    
This shold give you a python package that can now be imported from any where by this users
The package can be imported as 
import PhysicsObjs

This gives the users access to 
PhysicsObjs.PhysicsObjs and PhysicsObjs.c_objs

c_objs is a collection of c files and python files. The python class are mirrored as structs in h files. 
The shared_object(dll) leaves here as well as the functions that are ran in c_objs
The functionaility of the objects are described here, but are used in PhysicsObjs.PhysicsObjs to provide the main functionaility of the app
If a GUI object is available it can be run through the function run_app(). 

If the GUI object is available it takes in a Tk() as root, or if none is given it will create its own root. The GUI is meant to 
be plug and play with other tkinter GUI objects. The elements themselve are contained within a Frame object.
Requires:

Contributions:
josesalcedo410@gmail.com
