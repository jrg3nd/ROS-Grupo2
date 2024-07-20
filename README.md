
# ROS-Grupo2
En el presente github se encuentran los paquetes de ROS para la simulación de un robot tipo ackerman.
La estructura del carrito es: dos ruedas delanteras (encargadas de la dirección del carrito), dos ruedas traseras y un chasis de forma rectangular.

Con el objetivo de crear un espacio de trabajo claro y ordenado se creo el espacio de trabajo con el comando:

ros2 pkg create --build-type ament_python ackerman_robot


En los codigos presentes se encuentra el "ackerman.urdf", encargado de la descripción del robot con todos los respectivos links (uno para cada rueda y chasis) y joints (encargados de la union entre estructuras, junto con la ubicación de la unión).

Con el comando "ros2 launch urdf_tutorial display.launch.py model:=(directorio de ubicacion del archivo)/ackerman.urdf

se logra visualizar el carrito en el programa "RVIZ", junto con el "joint_state_publisher" que permite manipular y comprobar que las ruedas avanzan y las delanteras logran girar de izquierda a derecha.
![movimiento izquierda](https://github.com/user-attachments/assets/c3439a4e-796a-41dc-beef-581c560ee937)

![movimiento derecha](https://github.com/user-attachments/assets/c7106e4a-1ba7-457e-8c25-482d91a1d0e9)



El siguiente código es el llamado "ackerman.xacro", que corresponde a la modularización del urdf anterior.

La vizualicación de los tópicos se hace posible con los siguientes comandos:

ros2 run robot_state_publisher robot_state_publisher /home/usuario/Escritorio/Robot_ackerman/src/ackerman_robot/urdf/Robot_ackerman.urdf

Lo que hace es publicar las características sobre el estado del robot

El siguiente comando publica las caracteristicas de los joint que tiene el robot, en este caso se encargan del movimiento de las ruedas:

ros2 run joint_state_publisher_gui joint_state_publisher_guiros2 run robot_state_publisher robot_state_publisher /home/usuario/Escritorio/Robot_ackerman/src/ackerman_robot/urdf/Robot_ackerman.urdf

Si se quiere visualizar de forma gráfica los topicos se utiliza el comando:

rqt_gui rqt_gui

![topicos](https://github.com/user-attachments/assets/feef5db7-3f89-4e1f-b5ef-680114a36d7b)
