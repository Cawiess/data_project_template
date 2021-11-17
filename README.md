# data_project_template
A functional scaffolding for basic project setup.

Rationale:

My data related projects tend to follow the same general process as most other projects with regards to extraction, transformation, analysis and output. While the most intricate details differ between projects depending on requirements, the overarching implementation, that is the project structure remains very similar across projects. The goal of this repository is to implement a standardized, but basic infrastructure for future data analytical projects which includes:

    - A standardized directory structure: input, output, assets folders etc.
    - Logistical specifications: project name, author, date, authentication etc.
    - Data processing/analysis specifications: variables to include/exclude, their types and other parameters.
    - A set of tests: unit testing, but also data validation tests.
    - A clearly defined execution process: a preprocessing pipeline, analysis pipeline.
    - Logging functionality: package-wide logging to record each process from start to finish.

This list is by no means exhaustive, but represents a set of functionalities that can be standardized and to a large extent automated. These functionalities will be implemented in a way as to provide guidance and structure with flexibility in mind to accomodate for project-specific needs. As such, much of the functionality will be defined as classes which are easily modified with project specific information, very much like many small templates, ready to be filled in. These classes will be defined in separate modules with central main-function to collect and execute the project.

This approach has a number of advantages:

    - Time saving: there is no need to re-make the same or similar base setup for my upcoming projects.
    - Tidiness and acquaintance: Everything has its place in the project process and is documented. Deviations will be clear and the package could be further developed to accomodate these. 
      Other people will find it easier to read and understand the code and what the package does. This facilitates collaboration.
    - Validation: A defined process lends itself better to testing and is therefore more transparent and easily validated. Errors and mistakes, programmatic or logical, systematic or random, are more easily detected and corrected.
      Tracing and logging each process makes it easier to audit the whole process which generated the output at hand.


.. To be continued

I decided to use Cookiecutter in order to enable users to set up their project with custom directory names. To use this package simply run the following from the terminal:

cookiecutter https://github.com/Cawiess/data_project_template.git


Why use Tox?
Tox is a virtual environment manager and testing automation tool.
It facilitates the setup and running of the project code by:
  - Setting up virtual python environment which works across multiple operating systems.
  - Sets paths and home direcrtory
  - Installs requirements and runs all commands needed for the package.

To run the project code, the user only needs to execute the Tox.ini file.

What are config.py and config.yml?
Separate configuration files makes it easier and clearer to specify environment variables and parameters. As these specifications are outside of the operating source code, it is easier and faster for users to get an overview of, review and edit variables and parameters that the source code uses. 

Yaml files are much more simple than python files, and since they only specify parameter information, there is very little room for introducing possible bugs and other problems. For this reason, we specify variables and parameters pertaining to the dataset and filenames in the config.yml file.

Config.py is more complicated. It defines the package directory, and makes use of Pydantic BaseModel class to validate settings and input based on the information from the config.yml file. The classes in this module represent simple config objects which inherits from the Pydantic BaseModel. These config objects simply specify expected input information as class attributes. The config objects can be viewed as sub-config-objects which correspond to a specific theme, such as overall PackageConfig, PreprocessingConfig and ModelConfig. Each config object then validates its own specific set of configurations and settings. All sub-config-objects are then collected into a larger, overarching config-object.
Config.py has three helper functions which: (i) finds the config.yml, (ii) reads the config.yml and (iii) validates information and parameters specified in confg.yml.

Based on all above, config.py returns a config-object through which all variables and parameters are referred to. This way, the user is forced to be explicit with which variables will be used in the project and what to do with them. This also makes it easier to review, audit and debug any code. The program will stop early and alert with a validation error whenever any expectations regarding variable input are not met.

We can construct different types of tests around this configuration set up to make 
the package and its output as fail-safe, transparent and reproducible as possible.

### OBS ###
if you have an Anacondas installation of Python, make sure that it includes virtualenv.
conda install virtual env

Otherwise Tox will not be able to identify the virtual environment and get invocation errors as well as import errors, not finding modules.