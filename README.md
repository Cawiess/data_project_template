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


### OBS ###
if you have an Anacondas installation of Python, make sure that it includes virtualenv.
conda install virtual env

Otherwise Tox will not be able to identify the virtual environment and get invocation errors as well as import errors, not finding modules.