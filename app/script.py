import argparse
from random import randrange
from termcolor import colored
from os import path
import cv2
import numpy as np

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


def toASCII(frame, cols = 120, rows = 35):
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  height, width = frame.shape
  cell_width = width / cols
  cell_height = height / rows
  if cols > width or rows > height:
    raise ValueError('Too many cols or rows.')
  result = ""
  for i in range(rows):
    for j in range(cols):
      gray = np.mean(
        frame[int(i * cell_height):min(int((i + 1) * cell_height), height), int(j * cell_width):min(int((j + 1) * cell_width), width)]
      )
      result += grayToChar(gray)
    result += '\n'
  return result

def grayToChar(gray):
  CHAR_LIST = '  .-.:-=+*#i'
  num_chars = len(CHAR_LIST)
  return CHAR_LIST[
    min(
      int(gray * num_chars / 255),
      num_chars - 1
    )
  ]

def main():
    greatings()
    filename = parse_args().image

    if (path.isfile(filename)):
        image = cv2.imread(filename)
        print(colored(toASCII(image), 'red'))
    else:
        raise ValueError('Image path is not correct.')
    

if __name__ == "__main__":
    main()