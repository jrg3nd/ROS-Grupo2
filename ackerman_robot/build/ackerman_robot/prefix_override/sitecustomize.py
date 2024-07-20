import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/danilinux/Escritorio/Robot_ackerman/src/ackerman_robot/install/ackerman_robot'
