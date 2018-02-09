# -*- coding: utf-8 -*-

# ==========================================
# Interactive Command Line Interface of CaCo


'''
Canopy Cover (CaCo) V0.1

===========================================================
An objective image analysis method for estimation of canopy
attributes from digital cover photography

* author: Alessandro Alivernini <alessandro.alivernini@crea.gov.it>
* paper: https://doi.org/10.1007/s00468-018-1666-3
* git: https://github.com/alivernini/caco

CaCo:
    > processes every file in the input directory as a photo
    > returns an xls spreadsheet with the gap fraction of each photo
    > defines every procesing option in the PARAM3 dictionary
    > Free and Open Source software released under MIT licence

What features in the next releases?
    > graphical user interface

===========================================================

Canopy Cover (CaCo)
Copyright 2017-2018 Council for Agricultural Research and Economics

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:
The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

# CREDITS
# =======
# icon made by Roundicons from www.flaticon.com

import sys, os
from . import main_cc as cc
import yaml

# to check 1st image
import rawpy
import scipy
from scipy import misc
import pkg_resources

#--------------------------------------------------------------------------------
# Python 2/3 compatibility #

try:
   input = raw_input
except NameError:
   pass

#--------------------------------------------------------------------------------
# Input / output #

YML = pkg_resources.resource_filename('caco', 'caco.yml')

# load/restore default parameters
def load_caco_settings():
    ''' load settings '''
    param3 = None
    if os.path.exists(YML):
        try:
            with open(YML, 'r') as file0:
                param3 = code = yaml.load(file0)
        except Exception as e:  # file corrupted or deleted
            print(e)
            print('loading defaults')
            param3 = cc.get_param3()
    else:
        param3 = cc.get_param3()

    if param3 == None:
        raise ValueError
    return param3

def save_caco_settings(param3):
    ''' save settings '''

    with open(YML, 'w') as outfile:
        yaml.dump(param3, outfile, default_flow_style=False)


def restore_defaults():
    ''' restore and save settings '''

    param3 = cc.get_param3()
    save_caco_settings(param3)
    return param3


#--------------------------------------------------------------------------------
# Setting check #

def check_setting(choice, value, alternatives=None):
    ''' check setting from user input '''

    #--------------------------------------------------------------------------------
    '''
    CHECK SCHEME
    ============

    CHOICE | PAR TYPE    | CHECK/SOLUTION
    1      | input dir   | existing? Create. Not empty? 1 photo is readeble? Query user
    2      | output dir  | existing? Create
    3      | filename    | NONE
    4      | switch      | boolean?
    5      | alternative | in alternatives?
    6      | alternative | in alternatives?
    7      | switch      | boolean?
    8      | output dir  | existing? Create
    '''
    #--------------------------------------------------------------------------------

    check = [True, '']
    if choice == 1:
        check = ch_readable(value)  # perfoms all checks listed in the scheme
    elif choice in [2, 8]:
        check == ch_exists(value)  # directory is not exisiting
        if not check[0]:
            if (ch_mkdir):
                check == [True, 'directory created']
    elif choice in [4, 7]:
        if not type(value) == type(True):
            check = [False, 'value is not boolean']
    elif choice in [5, 6]:
        if not value in alternatives:
            check = [False, 'value is not between the alternatives']
    return check

# HELPING FUNCTIONS
def ch_exists(path0):
    ''' return True if path exists '''
    check = [True, '']
    if not os.path.exists(path0):
        check = [False, 'directory is not existing']
    return check

def ch_mkdir(path0):
    solved = False
    print('create new directory? y/[n]')
    choice = input(' >>  ')
    if choice == 'y':
        try:
            os.makedirs(path0)
            solved = True
        except Exception as e:
            print(e)
    return solved

def ch_empty(path0):
    ''' return True if no files in path '''
    empty = [False, 'directory is not empty']
    if len(os.listdir(path0)) == 0:
        empty = [True, 'directory is empty']
    return empty

def ch_readable(path0):
    '''
    check if 1st file in directory is readable
    '''

    readable = [False, None]

    check_exist = ch_exists(path0)
    if not check_exist[0]:
        return check_exist

    check_empty = ch_empty(path0)
    if check_empty[0]:
        return check_empty

    # take the first file
    test_file = (os.listdir(path0))[0]
    test_file = os.path.join(path0, test_file)

    test_raw = None
    # check if it is a photo
    try:
        try:  #read a raw image
            rawpy.imread(test_file)
        except Exception as e:
            test_raw = e
            scipy.misc.imread(test_file)
        readable[0] = True
    except Exception as e:  # at list 1 file in the directory is not a photo or CaCo is not able to read it
        print(test_raw)
        print(e)
        readable[1] = 'at list 1 file in the directory is not a photo or CaCo is not able to read it'
    return readable

def ch_isalternative(value, alternatives):
    check = [True, '']
    if not check in alternatives:
        check = [False, 'choice is not between alternatives']
    return check

#--------------------------------------------------------------------------------
# Interactive Command Line Interface #


def main():
    '''
    Command line interface of CaCo
    '''

    global param3
    left_margin = '      '

    param3 = load_caco_settings()

    mdiv = '-----------------------------------------------------------------'
    mdiv = left_margin + mdiv
    msg_main = (
    '''
       0 - exit CaCo
      ----------------------
       1 - print settings
       2 - modify setting
       3 - run CaCo
      ----------------------
       9 - save setting
      10 - restore default settings
    '''
    )

    print("\n\n\n"
        + left_margin + "Welcome to CaCo\n")
    print(
        left_margin + "CaCo is an objective image analysis method for estimation \n"
        + left_margin + "of canopy attributes from digital cover photography"
    )
    print(mdiv)

    while True:
        choices = [0, 1, 2, 3, 9, 10]
        # -->> begin of netested loop
        while True:
            print(msg_main)
            try:
                user_choice = int(input(" >>  "))
                if user_choice not in choices:
                    raise ValueError
                break
            except ValueError:
                continue
        # <<-- end of netested loop
        if user_choice == 0:
            break
        elif user_choice == 1:
            setting_show()
            input('\n\npress any key to continue')
        elif user_choice == 2:
            setting_show(True)
            print('')
        elif user_choice == 3:
            cc.caco_all(param3)
            # msg is already printed from CaCo main
            print('\n')
            input('press any key to continue')
        elif user_choice == 9:
            save_caco_settings(param3)
            print('CaCo settings saved\n')
        elif user_choice == 10:
            param3 = restore_defaults()
            print('CaCo defaults restored\n')
        print(mdiv)
    print('\n\n       Thank you for using CaCo!\n\n')
    return 0


def setting_show(modify_switch=False):
    ''' Show or modify current settings '''

    global param3

    menu_number = [x+1 for x in range(8)]
    param3_menu = {  #  key: param3 key, paramer, available choices
        1:['input_dir','input directory (only photos)'],
        2:['output_dir','output directory'],
        3:['output_xls','name of the output spreadsheet '],
        4:['raw_processing','switch for raw format input', '[True/False]'],
        5:['band','photo band used', '[red, green, blue, greeness, grey]'],
        6:['threshold','thresholding method', '[otzu, isodata, minimum]'],
        7:['th_switch','visual output',  '[True/False]'],
        8:['th_dir','directory of visual output'],
    }

    # --------------------------------------------------------------------------------
    # nested function #

    def show_menu():
        print('')
        # formatters
        left_margin = '      '
        fmt1 = '{:^16}'
        fmt2 = '{:<40}'

        # header
        header = []
        if modify_switch:
            header.append(fmt1.format('CHOICE'))
        header.extend([fmt2.format('PARAMETER'), 'VALUE'])
        header[0] = left_margin + header[0]
        print(' | '.join(header))

        # settings
        for ixx in menu_number:
            string0 = []
            if modify_switch:
                string0.append(fmt1.format(str(ixx)))
            string0.append(fmt2.format(param3_menu[ixx][1]))
            string0.append(str(param3[param3_menu[ixx][0]]))
            string0[0] = left_margin + string0[0]
            print(' | '.join(string0))
        if modify_switch:
            print(
                '''
            --------------------------------------------------------------------------------
             0 - exit from settings panel\n
            '''
            )

    # --------------------------------------------------------------------------------

    if not modify_switch:
        show_menu()
    else:
        divider = '---------------------------------'
        choices = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        while True:

            # -->> begin of nested loop
            while True:
                try:
                    # show choices
                    show_menu()
                    # select choice
                    choice = int(input(" >>>>  "))
                    if choice not in choices:
                        raise ValueError
                    break
                except ValueError:
                    continue
            # <<-- end of nested loop

            # check endcondition
            if choice == 0:
                break

            # show alternatives in any
            alternatives = None
            if choice in [4, 5, 6, 7]:
                if choice == 5:
                    alternatives = param3['band_choices']
                elif choice == 6:
                    alternatives = param3['th_choices']
                elif choice in [4, 7]:
                    alternatives = ['y (True) / n (False)']
                print("alternatives: {}".format(alternatives))

            new_val = input("new value: ")
            # translate bool values
            if choice in [4, 7]:
                if new_val == 'y' or new_val == 'True':
                    new_val = True
                elif new_val == 'n' or new_val == 'False':
                    new_val = False
            # run checks
            check = check_setting(choice, new_val, alternatives)
            if check[0]:
                # store option in param3
                keyp = param3_menu[choice][0]
                param3[keyp] = new_val
                print(divider)
                print("setting accepted")
                print(divider)
            else:
                print(divider)
                print("setting in not stored:")
                print(check[1])
                print(divider)

if __name__ == "__main__":
    main()



