# ROS-Grupo2
En el presente github se encuentran los paquetes de ROS para la simulación de un robot tipo ackerman.
La estructura del carrito es: dos ruedas delanteras (encargadas de la dirección del carrito), dos ruedas traseras y un chasis de forma rectangular.

En los codigos presentes se encuentra el "ackerman.urdf", encargado de la descripción del robot con todos los respectivos links (uno para cada rueda y chasis) y joints (encargados de la union entre estructuras, junto con la ubicación de la unión).

Con el comando "ros2 launch urdf_tutorial display.launch.py model:=(directorio de ubicacion del archivo)/ackerman.urdf

se logra visualizar el carrito en el programa "RVIZ", junto con el "joint_state_publisher" que permite manipular y comprobar que las ruedas avanzan y las delanteras logran girar de izquierda a derecha.

El siguiente código es el llamado "ackerman.xacro", que corresponde a la modularización del urdf anterior.

Para la visualización en gazeboo
