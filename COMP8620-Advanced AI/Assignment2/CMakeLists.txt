cmake_minimum_required(VERSION 3.8)
project(Assignment2)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES
        agent.cpp
        agent.hpp
        grid.cpp
        grid.hpp
        maze1d.cpp
        maze1d.hpp
        cheesemaze.cpp
        cheesemaze.hpp
        environment.cpp
        environment.hpp
        main.cpp
        main.hpp
        predict.cpp
        predict.hpp
        rockpaperscissor.hpp
        search.cpp
        search.hpp
        tictactoe.cpp
        tictactoe.hpp
        util.cpp
        util.hpp rockpaperscissor.cpp)

add_executable(Assignment2 ${SOURCE_FILES})