cmake_minimum_required(VERSION 3.5)
project(route_executor2)


find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(plansys2_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(mavros_msgs REQUIRED)
find_package(lifecycle_msgs REQUIRED)
#[[
find_package(nav2_msgs REQUIRED)
]]
find_package(plansys2_domain_expert REQUIRED)
find_package(plansys2_executor REQUIRED)
find_package(plansys2_planner REQUIRED)
find_package(plansys2_problem_expert REQUIRED)
find_package(plansys2_pddl_parser REQUIRED)

set(CMAKE_CXX_STANDARD 17)

set(dependencies
    rclcpp
    rclcpp_action
    plansys2_msgs
    #[[
    nav2_msgs
    ]]
    geometry_msgs
    plansys2_domain_expert
    plansys2_executor
    plansys2_planner
    plansys2_problem_expert
    plansys2_pddl_parser
    mavros_msgs
    lifecycle_msgs
)

add_executable(move_action_node src/move_action_node.cpp)
ament_target_dependencies(move_action_node ${dependencies})

add_executable(get_waypoints_node src/get_waypoints_node.cpp)
ament_target_dependencies(get_waypoints_node ${dependencies})
#[[
add_executable(patrol_action_node src/patrol_action_node.cpp)
ament_target_dependencies(patrol_action_node ${dependencies})

add_executable(patrolling_controller_node src/patrolling_controller_node.cpp)
ament_target_dependencies(patrolling_controller_node ${dependencies})
]]
install(DIRECTORY launch pddl DESTINATION share/${PROJECT_NAME})

install(TARGETS
  move_action_node
  get_waypoints_node
  #[[
  patrol_action_node
  patrolling_controller_node
  ]]
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION lib/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()

  find_package(ament_cmake_gtest REQUIRED)
endif()

ament_export_dependencies(${dependencies})

ament_package()
