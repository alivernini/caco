# CaCo
An objective image analysis method for estimation of canopy attributes from digital cover photography.

## Caco:
* is based on the paper of Alivernini, A., Fares, S., Ferrara, C. Chianucci, F., Trees 2018.
https://doi.org/10.1007/s00468-018-1666-3
* processes every file in the input directory as a photo
* returns an xls spreadsheet with the gap fraction of each photo
* is a Free and Open Source software released under MIT licence


## GETTING STARTED with CaCo v0.2.4

===============================================

# Start installing CaCo... #

    LET'S HEAT UP THE ENVIRONMENTS:

    - for Windows, please check/install:
        * Microsoft build tools 2015
        http://landinghub.visualstudio.com/visual-cpp-build-tools
        * your favourite version of Python (recommended versions are: v2.7.8 or v3.6.4)
        https://www.python.org/downloads/windows/

    - For Mac OS, please check/install:
        * your favourite version of Python (recommended versions are: v2.7.8 or v3.6.4)
        https://www.python.org/downloads/mac-osx/

    - For Linux:
        * You are ready to go



    LET'S INSTALL AND USE CACO

    - In your terminal emulator (or command prompt):

        * install CaCo:
        > python -m pip install --user caco

        * run CaCo
        > python -m caco

    If you use python3 and you get an error, try typing "python3" instead of "python"


==============================================
# Starting from the results ... #


LET'S HAVE A LOOK AT THE RESULTS OF A TUTORIAL PROJECT

    * download and extract the tutorial project
    [caco_myprj](https://github.com/alivernini/caco/releases/download/v0.2.4/caco_myprj.zip)

    * take a look at the input images

    * in the folder "output"  you can see an excel spreadsheet
    with the computed gap fraction and other statistics

    * right there, inside the "th_img" subfolder, have a peek
    at the thresholded images, ... closer... zoom one:
        - small gaps are identified in light grey
        - big gaps are white
        - vegetation is black

    * this output was given by the "test_myprj.py"

    * can you set up caco to have the same results?


==============================================

Now you are ready to analyze your images with CaCo!

Just one tip to set up CaCo: copy the project paths from your file-manager


Buona giornata,
Alessandro


