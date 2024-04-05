End to End Machine Learning Project - 
[https://obesitypredictor.azurewebsites.net/predictdata](https://obese-predictor.azurewebsites.net/predictdata)



Explanation for my reference - 
1. Create a git Repository on github - copy the HTTP link
2. Create a local directory
3. Navigate to the project directory in the command line, and type in **code .** which creates a VSCode instance of the directory
4. Follow this specific list of commands to link a remote repository with a local repository and push changes
	1. **git init**
	    - Initialises the local repository to be tracked by git
	    - Adds a .git directory to the project folder, which contains all the metadata for version control
	    - It is considered a hidden folder, so won't be visible in the folder structure
	    - Can be viewed by using the command **ls -a**
	    - Metadata contained in the .git directory includes -
		    - Configuration files - include confiuration settings such as remote repository URLs, branch tracking information, etc.
		    - Object Database - stores data of my repository including commits, trees, blobs (file contents), and tags
		    - References- pointers to commits, branches, and tags. Most important reference is HEAD, which points to the currently checked out commit
		    - Index (staging area) - binary file that stores information about what will go to the next commit
     2. Create a README.md file in local directory
        - The markdown file.
        - To sync these changes with the remote repository, you would need to push these changes to it.
    3.  **git add README.md**
         - This command is used to stage the README.md file for the next commit in your git repository
         - Staging is the process of preparing changes to be included in next commits
         - When one stages a file, one tells git that they want to include the current state of that file in the next commit
         - Staging area is a temporary area where git keeps track of changes to be commited - also known as the index(refer above)
         - when **git commit** is run, the files in the staging area will be included in the new commit
     4. **git commit -m 'message'** 
         - used to save changes to the local repository
         - a commit is a snapshot of the project at a specific point in time. Each commit has a unique identifier(a hash), a message describing the changes, and a reference to the commit that came before it
     5. **git branch -m main**
         - used to rename the branch to main
         - traditionally called master branch
         - this operation is performed locally, and it only affects the local repository
     6. **git remote add origin 'HTTP Link of remote repository'**
         - adds a new remote repository reference to the .git/config file in the local repository
         - this entry consists of the name of the remote rep(origin) and the URL of the remote repository
         - It establishes a connection between the local and remote repositories and is used for fetching changes from the remote, pushing changes to the remote etc.
     7. **git push origin main**
         - updates the remote master branch with the new commits from the local master branch
         - need to have necessary permissions to push changes to the remote repository, else the operation will fail
         - if permissions do not allow push, create a pull request and wait for an admin to merge if no conflicts are present
5. Create a new environment - using virtualenv, which is pip installable, and pip upgradeable
	1. **virtualenv venv**
		 - creates a new virtual environment called venv
		 - this command creates a directory which contains the virtual environment in the project directory(assuming this is where the command was run)
		 - if one wants to use a different version of python than the one installed in your system, it can be specified as follows
			 - **virtualenv -p /usr/bin/python3.x  myenv**
	 1. **source venv/bin/activate**
	     - activates the virtual environment for the first time
	     - subsequent activations involves the **workon** command
	 2. **deactivate**
	     - deactivates the virtual environment
 6. create setup.py and requirements.txt
	 - setup.py is a build script for setuptools
	 - It tells the setupttols about the name and version of your package and any packages and modules it includes
	 - It might look like -
		 - from setuptools import setup, find_packages
		   setup(
			    name='YourPackageName',
			    version='0.1',
			    packages=find_packages(),
			    install_requires=[
			        'requests',
			        'numpy',
			    ],
			)
	 - It can also spcify dependencies, scripts, and other metadata
	 - requirements.txt is a plain text file that lists all the python packages the project depends on.
	 - it might look like - 
		 - requests == 2.25.1
		  numpy  == 1.20.3
	  - **`setup.py`** is used for packaging your project and can include dependencies directly in the `install_requires` parameter. This is useful for specifying dependencies that are required for your package to work.
	  - **`requirements.txt`** is used for specifying dependencies that are required for development, testing, or running your project. It's often used in conjunction with `setup.py` to ensure that all necessary dependencies are installed.
	  - While `setup.py` is essential for packaging Python projects, using a `requirements.txt` file alongside it offers several advantages in terms of clarity, flexibility, compatibility, reproducibility, and ease of use. It's a best practice to include both files in your project, especially for projects that are intended to be used by others or deployed in various environments.
	  - The `setup.py` script can also be used to create distribution packages that can be uploaded to the Python Package Index (PyPI) or other package repositories. This makes your package easily installable by others using `pip install YourPackageName`.
	  - while `setup.py` does not directly support specifying the path to a `requirements.txt` file for automatic installation of dependencies, you can easily achieve this by reading the `requirements.txt` file within your `setup.py` script and passing its contents to the `install_requires` parameter. This approach ensures that your package's dependencies are automatically installed when your package is installed.
		  - from setuptools import setup, find_packages
			import os
			with open('requirements.txt') as f:
			    required = f.read().splitlines()
			
			setup(
			    name='YourPackageName',
			    version='0.1',
			    packages=find_packages(),
			    install_requires=required
			)
	 - find_packages() function
		 - The `packages=find_packages()` argument in a `setup.py` file is used to automatically discover and include all Python packages and subpackages in your project when you're packaging your project for distribution. This is particularly useful for projects with a complex directory structure that includes multiple packages and subpackages.
		 - `find_packages()` scans the directory where `setup.py` is located and finds all Python packages. A Python package is a directory that contains an `__init__.py` file. This file can be empty, but it must be present for Python to recognize the directory as a package.
		 - Using `packages=find_packages()` in your `setup.py` file is a convenient way to automatically include all packages and subpackages in your project when packaging it for distribution. It simplifies the process of creating a distribution by automatically handling the discovery and inclusion of packages, making your `setup.py` file cleaner and more maintainable.
		 - While `packages=find_packages()` in your `setup.py` file is used to automatically discover and include all Python packages and subpackages in your project when you're packaging your project for distribution, `install_requires` serves a different purpose: it specifies the dependencies that your project needs to run. These dependencies are external Python packages that your project relies on, but are not part of your project's source code.
		 - including -e . in requirements.txt automatically triggers the setup.py script
	 - The `projectname.egg-info` directory is automatically generated by Python's setuptools when you package your project using `setup.py`. This directory contains metadata about your project, such as the project's name, version, and dependencies. The metadata is stored in a file named `PKG-INFO` within the `projectname.egg-info` directory.
		 - **`PKG-INFO`**: This file contains metadata about the project, such as the project's name, version, author, and dependencies. This metadata is specified in the `setup.py` file of your project.
		- **`SOURCES.txt`**: This file lists the source files that were included in the distribution.
		- **`dependency_links.txt`**: This file lists any URLs where the package's dependencies can be found. This is useful for packages that have dependencies that are not available on PyPI.
		- **`requires.txt`**: This file lists the project's dependencies. It's similar to the `install_requires` parameter in `setup.py`, but it's generated automatically when you package your project.
		- **`top_level.txt`**: This file lists the top-level modules of your project. Top-level modules are those that can be imported directly without needing to import any submodules first.
 7. create a 'components' subfolder within src directory under the project directory. This contains all the modules of our project
	 1. include `__init__.py` under both so they are recognised as packages by find_packages() function in setup.py
	 2. The `__init__.py` file plays a crucial role in Python's module system, marking directories as packages and allowing for the organization of code into a logical and reusable structure.
		 1. Suppose you have the following directory structure: 
				mypackage/
				    __init__.py
				    module1.py
				    module2.py
		  2. In this case, `mypackage` is a package because it contains an `__init__.py` file. You can import `mypackage` in a Python script like this:
			     **import mypackage**
          3. And you can access its modules like this:
			     import mypackage.module1
	3. May include components such as data_ingestion.py, data_transformation.py, train_pipeline.py, predict_pipelilne.py and model_trainer.py.

 8.  Include logger.py, utils.py and exception.py scripts in components
	  - The `logger.py` module is typically used for setting up and configuring logging for a Python application. Python's built-in `logging` module provides a flexible framework for emitting log messages from Python programs. The `logger.py` module can define a logger configuration that includes the log level, output format, and where the logs should be directed (e.g., console, file, or external logging services).
	  - The `utils.py` module is a common place to store utility functions that are used across different parts of your application. These functions can perform various tasks such as data validation, string manipulation, file handling, or any other operations that are not specific to the main functionality of your application but are needed for its operation. 
	  - Eg: can be used to create a mongo client to read data from a mongo database. OR  save model into the cloud
	  - The `exception.py` module is used to define custom exceptions that are specific to your application. Python allows you to define your own exception classes, which can inherit from the built-in `Exception` class or any other exception class. Custom exceptions can be used to signal specific error conditions that are unique to your application's domain.
  9. exception.py code includes-
	   - import sys - The `sys` module in Python provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter. It is always available and provides a variety of functions and variables that can be used to manipulate different parts of the Python runtime environment.
		   - The `sys.argv` list is used to access command line arguments passed to the script. The first item in the list, `sys.argv[0]`, is the script name itself.
		   - The `sys.path` list contains the directories that Python searches for modules. You can modify this list to add new directories to the search path.
		   - You can use `sys.exit()` to exit a script. You can also pass an argument to `sys.exit()` to indicate an exit status. A zero status indicates success, while a non-zero status indicates an error.
		   - The `sys.version` string contains the version of Python that is currently running the script.
	   - from src.logger import logging
	   -  `exc_info` is a function in Python's `sys` module that returns information about the exception being handled. It's often used in logging or debugging to get detailed information about an exception that has been caught.
	   - it returns a tuple containing three parameters:
		   - **Exception Type (`exc_type`)**: This is the type of the exception that was raised. It's a class that inherits from the base `Exception` class. For example, if a `ZeroDivisionError` was raised, `exc_type` would be `ZeroDivisionError`.
		   - **Exception Value (`exc_value`)**: This is the instance of the exception that was raised. It contains the specific details about the error. For a `ZeroDivisionError`, `exc_value` would contain the message "division by zero".
		   - **Traceback (`exc_traceback`)**: This is a traceback object encapsulating the call stack at the point where the exception was raised. It provides a detailed stack trace, showing the sequence of function calls that led to the exception. This can be very useful for debugging, as it allows you to see exactly where in the code the error occurred.
	   - error_message_detail() method
		   - collects error traceback which includes details like where the error occured, and the error message
		   - formats the error message including all the information received from the traceback method
	   - CustomException class - inherits from the base class Exceptions
		   - has __str__() method which outputs strings in a friendly, human readable format
		   - fetches data from the error_message detail
		   - class CustomError(Exception): 
			   def __init__(self, message, error_code): 
				   super().__init__(message) self.error_code = error_code
		  - common to all classes. when CustomException is raised, the error message will be displayed and logged
		  - if __name__=="__main__":
				try:
					a=1/0
				except Exception as e:
					logging.info("divide by zero")
		 - when i execute the above code, it should display error message in the console, as well as create a log file as per the specified format as i have previously imprted logger.py in the exception.py file

raise CustomException(e,sys)
1. logger.py code includes-
	  - any execution that happens gets logged, this includes when CustomException error is raised
	  - import logging, import os, import date_time
	  - The `logging` module in Python is a powerful built-in module for event logging. It provides a flexible framework for emitting log messages from Python programs. Logging is a way to track events that happen when some software runs. The software's developer adds logging calls to their code at various points where they want to record what the software is doing.
	  - The `logging` module is highly configurable. You can set the level of logging (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL), and you can specify different handlers (e.g., writing to a file, sending emails, or logging to a remote server) for different log levels.
	  - My code uses INFO level for logging and stores it in a log file
	  - The `logging.basicConfig` function in Python's `logging` module is a convenient method for configuring the logging system with basic settings. It allows you to set up the logging system with a single call, specifying the level of logging, the format of the log messages, and where the log messages should be output (e.g., to a file, the console, or elsewhere).
	  - import logging # Configure the logging module logging.basicConfig(level=logging.DEBUG, format='%   (
	                     asctime)s - %(levelname)s - %(message)s', filename='app.log', filemode='w')
	 - So now, wherever I use logging.info, it will output the format specified in basicConfig(location, lineno etc. of where logging.info was present), to a log file in the specified LOG_FILE_PATH
	 - you can also optionally pass a message along with logging.info() which the logger outputs in the file
  11. EDA + Model training notebooks
	   - self explanatory. I trust all those kaggle competitions have done their job.
   12. data_ingestion.py
	  - The primary purpose of a data ingestion script, like `data_ingestion.py`, is to retrieve data from various data sources.
	  - main aim is to read data from some kind of source(database, web API, local file, etc.)
 13. data_transformation.py
	   - used to preprocess the data and convert it into a form which can be fed into a machine learning model
	   - consists of pipelines, which are ways of combining functions
	   - also consists of column transformers, which combine pipelines into one neat little object
	   - save preprocessing as a pkl file(more info needed)
14. utils.py
	   - used for defining reusable utility functions
	   - import os, import sys, import numpy, import pandas etc.
	   - used to make the code cleaner
	   - uses dill module to save pkl files
	   - define save_object function in utils and use in data_transformation.py to save preprocessor as a pkl file
	   - A `.pkl` file is a file format used for serializing and de-serializing Python objects. The term "pkl" stands for "pickle," which is a module in Python that implements binary protocols for serializing and de-serializing a Python object structure. This means you can save almost any Python object to a file and then load it back into your program later. The `.pkl` file format is widely used in machine learning applications for several reasons:
	   - - **Model Persistence**: One of the most common uses of `.pkl` files in machine learning is to save trained models. After training a model, you can save it to a `.pkl` file. Later, you can load this file to use the model for making predictions without having to retrain it. This is particularly useful for large models that take a long time to train.
	   - **Data Sharing**: `.pkl` files can be used to share data between different parts of a machine learning pipeline or between different projects. For example, you might train a model on one machine and then want to use it on another machine. By saving the model to a `.pkl` file, you can easily transfer
	   - **Data Preparation**: In machine learning, data often needs to be preprocessed before it can be used for training models. This preprocessing can include tasks like normalization, encoding categorical variables, or splitting the data into training and test sets. By saving the preprocessed data to a `.pkl` file, you can reuse it in future projects or experiments without having to preprocess the data again.
	   - utils has a load_object pkl file to load pkl files which is used in predict_pipeline class
	   - it basically opens the file specified by file_path in readby mode, and loading the pickle file by using dill.load() method
## EVERY COMPONENT NEEDS A CONFIG CLASS
15. prediction_pipeline, app.py and training_pipeline
	 - most important part
	 - create a web application that interacts with the .pkl files wrt any input data that is given
	 - create a new file called app.py which is used to create a flask application
	 - from flask import Flak, requests, render_template
	 - import numpy, pandas, sklearn in app.py
	 - create routes to home.html and index.html
	 - create a CustomData class in predict_pipeline which is important in mapping all the data we get in HTML to the backend
	 - this class has a constructor which defines all the input fields and their data types, so it creates one object that represents one instance of the class
	 - define s method which returns the data as a dataframe which can be fed into the ML model
	 - define the file paths to model.pkl and preprocessor.pkl files
	 - model = load_object(file_path)
	 - after loading the model, as well as the preprocessor in similar fashion, use the transform method from preprocessor to transform the features, and then model witll predict values with the preprocessed data
