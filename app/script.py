import argparse
from random import randrange
from termcolor import colored
from os import path
import cv2
import numpy as np
from settings import DEFAULT_ARGS_VALUES

def greatings():
    print(''' 
        TODO /// 
    '''
    )
    print(colored('Generate an awesome console logo for your console app', 'yellow'))
    print(colored('Author: @Vald○R github.com/valdesche \n\n', 'yellow'))

def parse_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--image',
                        help = 'Path to the image',
                        required = True)
    parser.add_argument('-width', '--width',
                        help = 'Width of the ASCII Art result',
                        default=DEFAULT_ARGS_VALUES['width'],
                        required = False)
    parser.add_argument('-height', '--height',
                        help = 'Height of the ASCII Art result',
                        default=DEFAULT_ARGS_VALUES['height'],
                        required = False)
    parser.add_argument('-replace', '--replacement_str',
                        help = 'Replacement characters',
                        default=DEFAULT_ARGS_VALUES['replacement_str'],
                        required = False)                                          
    return parser.parse_args()

# Make art from a frame
def makeArt(frame, dictionnary = DEFAULT_ARGS_VALUES['replacement_str'],  cols = DEFAULT_ARGS_VALUES['width'], rows = DEFAULT_ARGS_VALUES['height'] ):
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  height, width = frame.shape
  cell_width = width / cols
  cell_height = height / rows
  if cols > width or rows > height:
    raise ValueError('Too many cols or rows.')
  result = ''
  for i in range(rows):
    for j in range(cols):
      gray = np.mean(
        frame[int(i * cell_height):min(int((i + 1) * cell_height), height), int(j * cell_width):min(int((j + 1) * cell_width), width)]
      )
      result += grayToChar(gray, dictionnary, len(dictionnary))
    result += '\n'
  return result

# Convert a gray scale to corresponding caracter according to the dictionnary
def grayToChar(gray, dict, dict_lenght):
  return dict[
    min(
      int(gray * dict_lenght / 255),
      dict_lenght - 1
    )
  ]

def main():
    greatings()
    args = parse_args()
    filename = args.image
    width = int(args.width)
    height = int(args.height)

    if (path.isfile(filename)):
        image = cv2.imread(filename)
        # Result art
        result = makeArt(image, args.replacement_str, width, height)
        print(colored(result, 'red'))
    else:
        raise ValueError('Image path is not correct.')
    

if __name__ == '__main__':
    main()