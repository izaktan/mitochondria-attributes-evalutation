Evaluating attributes of Mitochondria
====================================

This script will help to evaluate volume, skeleton size and cable length of Mitochondria


Preparation
---------------------------------------------
To enable your computer to run the script, first install these applications:

- Install `Anaconda <https://www.anaconda.com/products/individual>`_
- Install `Git <https://git-scm.com/download/win>`_ (call `Anaconda Prompt <https://docs.anaconda.com/anaconda/install/verify-install/>`_ or `Command Prompt <https://www.dell.com/support/kbdoc/en-in/000130703/the-command-prompt-what-it-is-and-how-to-use-it-on-a-dell-system>`_ in your window search option)

>>> conda install -c anaconda git


Create the conda environment
---------------------------------------------
We need to create an environment for the script to run successfully, There is a ``environment.yml`` file in the parent directory in the repository, this file stores the infomation of package needed.

* Create the conda environment and install dependency packages as listed in ``environment.yml``
>>> conda env create -f environment.yml

* Activate the environment which just been created.
>>> conda activate evaluate


Run the script
---------------------------------------------
In ``main.py``, ``evaluate`` method takes three parameters
    * dataset directory, which is the directory of the source data you want to evaluate
    * output directory, which is the directory where you want the output file to be generated, this directory should not be exist at the time you run the script
    * data resolution, which is the resolution of the source data

Open up ``main.py``, modify the parameters dataset directory, output directory and the data resolution (optional) and save the modification. 

Then run ``main.py``. The output file ``out.csv`` will be generated in the output directory you defined.
>>> python main.py

.. note::

   The directory sould be passed in absolute path. So if you encounter error message like "directory does not exist", try to use `getcwd <https://docs.python.org/3/library/os.html#os.getcwd>`_ from `os libiary <https://docs.python.org/3/library/os.html>`_ for correct directory.


Reference
---------------------------------------------
* `kimimaro <https://github.com/seung-lab/kimimaro>`_
* `TIMISE <https://github.com/danifranco/TIMISE>`_