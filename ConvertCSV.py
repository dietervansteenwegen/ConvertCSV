"""
Dieter Vansteenwegen (vansteenwegen.org)
MIT License
Converts a CSV: colums separator from semicolon to comma, decimal symbol from comma to point
"""

import sys  # access to arguments
import getopt  # tool to parse arguments
from time import sleep
# import pdb
# pdb.set_trace()

success = True
filesCreated = list()

try:
    opts, arg = getopt.getopt(sys.argv[1:], "")  # returns a list with each option,argument combination
    
    if len(arg) == 0:
        raise getopt.GetoptError('')

    for i in arg:
        with open(i) as input:
            outputFileName = i+'.csv'
            with open(outputFileName, 'w') as output:
                for line in input:
                    line = line.replace(',', '.')
                    line = line.replace(';', ',')
                    output.write(line)
                filesCreated.append(outputFileName)

 
 
except getopt.GetoptError:  # invalid arguments have been provided at the command line.
    print("""
    Warning: not doing anything. Add file to be converted as argument when calling this script.
    """)
    success = False

except KeyboardInterrupt:
    print("(QUEUE) Keyboard interrupt (CTRL+C) detected, now exiting...")
    exit()
    success = False

except Exception as e:
    print(e)
    success = False

finally:
    if len(filesCreated) > 0:
        written=',\n\r'.join(filesCreated)
        print('Files written:')
        print(written)
        print('\n\r')
    print('DONE' if success else 'ERROR OCCURED')
    sleep(5)