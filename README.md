# CaCo
An objective image analysis method for estimation of canopy attributes from digital cover photography.

## Caco:
* is based on the paper of Alivernini, A., Fares, S., Ferrara, C. Chianucci, F., Trees 2018.
https://doi.org/10.1007/s00468-018-1666-3
* processes every file in the input directory as a photo
* returns an xls spreadsheet with the gap fraction of each photo
* is a Free and Open Source software released under MIT licence


## Getting started with CaCo!
===============================================

Do you get the feeling of a terminal interface?

    cd "folder where you extracted CaCo"

    in "setup" folder:
    > install -r requirements.txt

    in "code" folder:
    > python caco_cli

==============================================

Or...

Do you like to start from the results?

    > open caco_myprg folder

    > take a look at the input images

    > in the folder "output"  you can see an excel spreadsheet
    with the computed gap fraction and other statistics

    > right there, inside the "th_img" subfolder, have a peek
    at the thresholded images, ... closer... zoom one:
        - small gaps are identified in light grey
        - big gaps are white
        - vegetation is black

    > this output was given by the "test_myprj.py"

==============================================

Buona giornata,
Alessandro


