import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/danilinux/Escritorio/Robot_ackerman/install/ackerman_robot'
