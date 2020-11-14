import argparse
from random import randrange
from termcolor import colored
from os import path
import cv2

def greatings():
    print(""" 
        TODO /// 
    """
    )
    print(colored("Generate an awesome console logo for your console app", 'yellow'))
    print(colored("Author: @Vald○R github.com/valdesche \n\n", 'yellow'))

def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--image",
                        help = "Path to the image",
                        required = True)
    return parser.parse_args()



def main():
    greatings()
    filename = parse_args().image
    if (path.isfile(filename)):
        image = cv2.imread(filename)
    else:
        raise ValueError('Image path is not correct.')
    
    

if __name__ == "__main__":
    main()