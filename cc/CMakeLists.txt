cmake_minimum_required(VERSION 3.20)
project(algo_ds_cc LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(absl REQUIRED)
find_package(GTest REQUIRED)

enable_testing()

# myarrays / hello
add_library(hello
    myarrays/hello.cc
)
target_include_directories(hello PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/myarrays)
target_link_libraries(hello PUBLIC absl::strings)

add_executable(hello_main
    myarrays/hello_main.cc
)
target_link_libraries(hello_main PRIVATE hello)

add_executable(hello_test
    myarrays/hello_test.cc
)
target_link_libraries(hello_test PRIVATE hello GTest::gtest_main)
add_test(NAME hello_test COMMAND hello_test)
