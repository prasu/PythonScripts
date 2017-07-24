print('executing the module {}'.format(__name__))

import sys
import FirstProject.creator

r = sys.argv[1]
try:
    printItems(r)
except:
    pass
finally:
    print('executed')