import sys
import os



if len(sys.argv) == 2:
	run = os.system("shutdown {}".format(sys.argv[1]))
