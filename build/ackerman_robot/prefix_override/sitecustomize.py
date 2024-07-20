import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/danilinux/Escritorio/Robot_ackerman/src/install/ackerman_robot'
