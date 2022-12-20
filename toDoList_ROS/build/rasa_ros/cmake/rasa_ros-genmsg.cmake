# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "rasa_ros: 0 messages, 6 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(rasa_ros_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Dialogue.srv" NAME_WE)
add_custom_target(_rasa_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rasa_ros" "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Dialogue.srv" ""
)

get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Text2Speech.srv" NAME_WE)
add_custom_target(_rasa_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rasa_ros" "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Text2Speech.srv" ""
)

get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/WakeUp.srv" NAME_WE)
add_custom_target(_rasa_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rasa_ros" "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/WakeUp.srv" ""
)

get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Rest.srv" NAME_WE)
add_custom_target(_rasa_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rasa_ros" "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Rest.srv" ""
)

get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/ExecuteJS.srv" NAME_WE)
add_custom_target(_rasa_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rasa_ros" "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/ExecuteJS.srv" ""
)

get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/LoadUrl.srv" NAME_WE)
add_custom_target(_rasa_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rasa_ros" "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/LoadUrl.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Dialogue.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rasa_ros
)
_generate_srv_cpp(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Text2Speech.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rasa_ros
)
_generate_srv_cpp(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/WakeUp.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rasa_ros
)
_generate_srv_cpp(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Rest.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rasa_ros
)
_generate_srv_cpp(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/ExecuteJS.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rasa_ros
)
_generate_srv_cpp(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/LoadUrl.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rasa_ros
)

### Generating Module File
_generate_module_cpp(rasa_ros
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rasa_ros
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(rasa_ros_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(rasa_ros_generate_messages rasa_ros_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Dialogue.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_cpp _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Text2Speech.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_cpp _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/WakeUp.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_cpp _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Rest.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_cpp _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/ExecuteJS.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_cpp _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/LoadUrl.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_cpp _rasa_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rasa_ros_gencpp)
add_dependencies(rasa_ros_gencpp rasa_ros_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rasa_ros_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Dialogue.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rasa_ros
)
_generate_srv_eus(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Text2Speech.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rasa_ros
)
_generate_srv_eus(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/WakeUp.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rasa_ros
)
_generate_srv_eus(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Rest.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rasa_ros
)
_generate_srv_eus(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/ExecuteJS.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rasa_ros
)
_generate_srv_eus(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/LoadUrl.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rasa_ros
)

### Generating Module File
_generate_module_eus(rasa_ros
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rasa_ros
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(rasa_ros_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(rasa_ros_generate_messages rasa_ros_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Dialogue.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_eus _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Text2Speech.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_eus _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/WakeUp.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_eus _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Rest.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_eus _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/ExecuteJS.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_eus _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/LoadUrl.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_eus _rasa_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rasa_ros_geneus)
add_dependencies(rasa_ros_geneus rasa_ros_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rasa_ros_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Dialogue.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rasa_ros
)
_generate_srv_lisp(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Text2Speech.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rasa_ros
)
_generate_srv_lisp(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/WakeUp.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rasa_ros
)
_generate_srv_lisp(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Rest.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rasa_ros
)
_generate_srv_lisp(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/ExecuteJS.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rasa_ros
)
_generate_srv_lisp(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/LoadUrl.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rasa_ros
)

### Generating Module File
_generate_module_lisp(rasa_ros
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rasa_ros
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(rasa_ros_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(rasa_ros_generate_messages rasa_ros_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Dialogue.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_lisp _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Text2Speech.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_lisp _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/WakeUp.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_lisp _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Rest.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_lisp _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/ExecuteJS.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_lisp _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/LoadUrl.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_lisp _rasa_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rasa_ros_genlisp)
add_dependencies(rasa_ros_genlisp rasa_ros_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rasa_ros_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Dialogue.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rasa_ros
)
_generate_srv_nodejs(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Text2Speech.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rasa_ros
)
_generate_srv_nodejs(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/WakeUp.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rasa_ros
)
_generate_srv_nodejs(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Rest.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rasa_ros
)
_generate_srv_nodejs(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/ExecuteJS.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rasa_ros
)
_generate_srv_nodejs(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/LoadUrl.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rasa_ros
)

### Generating Module File
_generate_module_nodejs(rasa_ros
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rasa_ros
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(rasa_ros_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(rasa_ros_generate_messages rasa_ros_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Dialogue.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_nodejs _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Text2Speech.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_nodejs _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/WakeUp.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_nodejs _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Rest.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_nodejs _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/ExecuteJS.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_nodejs _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/LoadUrl.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_nodejs _rasa_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rasa_ros_gennodejs)
add_dependencies(rasa_ros_gennodejs rasa_ros_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rasa_ros_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Dialogue.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rasa_ros
)
_generate_srv_py(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Text2Speech.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rasa_ros
)
_generate_srv_py(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/WakeUp.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rasa_ros
)
_generate_srv_py(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Rest.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rasa_ros
)
_generate_srv_py(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/ExecuteJS.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rasa_ros
)
_generate_srv_py(rasa_ros
  "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/LoadUrl.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rasa_ros
)

### Generating Module File
_generate_module_py(rasa_ros
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rasa_ros
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(rasa_ros_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(rasa_ros_generate_messages rasa_ros_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Dialogue.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_py _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Text2Speech.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_py _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/WakeUp.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_py _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/Rest.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_py _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/ExecuteJS.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_py _rasa_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/ski-nex/Cognitive-Robotics/toDoList_ROS/src/rasa_ros/srv/LoadUrl.srv" NAME_WE)
add_dependencies(rasa_ros_generate_messages_py _rasa_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rasa_ros_genpy)
add_dependencies(rasa_ros_genpy rasa_ros_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rasa_ros_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rasa_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rasa_ros
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(rasa_ros_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rasa_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rasa_ros
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(rasa_ros_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rasa_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rasa_ros
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(rasa_ros_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rasa_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rasa_ros
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(rasa_ros_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rasa_ros)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rasa_ros\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rasa_ros
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(rasa_ros_generate_messages_py std_msgs_generate_messages_py)
endif()
