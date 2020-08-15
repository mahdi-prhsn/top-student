from STU import *
from tabulate import tabulate
from docopt import docopt

Usage = ''' 
Usage:
    STU_app.py --init
    STU_app.py --add <name> <family> <code> <math> <physics> <chemistry>
    STU_app.py --show <code>
    STU_app.py --MaxMin <code>
'''
args = docopt(Usage)

if args['--init']:
    init()
    print('='*50)
    print('your table created successfully.')
    print('='*50)

if args['--add']:
    try:
        code = int(args['<code>'])
        math = float(args['<math>'])
        physics = float(args['<physics>'])
        chemistry = float(args['<chemistry>'])
        add(args['<name>'],args['<family>'],code,math,physics,chemistry)
        print('='*50)
        print('Item added.')
        print('='*50)
    except:
        print(Usage)
        
if args['--show']:
    code = args['<code>']
    name, avg = show(code)
    print('='*50)
    print('stu. information: ',name.capitalize())
    print('Average: ',avg)
    print('='*50)
    

if args['--MaxMin']:
    code = args['<code>']
    name, maxx, miin = max_min(code)
    print('='*50)
    print('stu. information: ',name.capitalize())
    print('Max Mark: ',maxx)
    print('Min Mark: ',miin)
    print('='*50)
    
