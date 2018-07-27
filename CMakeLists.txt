project(Muser2)
cmake_minimum_required(VERSION 2.8.6)

if (CMAKE_SOURCE_DIR STREQUAL CMAKE_BINARY_DIR ) 
  message (FATAL_ERROR
    "In-source builds are not allowed. Please clean your source tree and try again.")  
endif()

# Add path for custom modules
set(CMAKE_MODULE_PATH
  ${CMAKE_MODULE_PATH}
  "${CMAKE_CURRENT_SOURCE_DIR}/cmake"
  )

include(GetGitRevisionDescription)
get_git_head_revision (GIT_REFSPEC GIT_SHA1)
message (STATUS "sha is ${GIT_SHA1}")
add_definitions(-DCOMMITID="${GIT_SHA1}")

include ("cmake/PackageOptions.cmake")

string(TIMESTAMP BUILDDATE "%Y-%m-%d %H:%M")
add_definitions(-DBUILDDATE="${BUILDDATE}")

add_definitions(-DTRACEVERB=0)

set (CUSTOM_BOOST_ROOT "" CACHE PATH "Path to custom boost installation.")
if (CUSTOM_BOOST_ROOT)
  set (BOOST_ROOT ${CUSTOM_BOOST_ROOT})
  set (Boost_NO_SYSTEM_PATHS "ON")
endif()
set (Boost_USE_STATIC_LIBS ON)
find_package (Boost 1.46.1 REQUIRED)
IF (Boost_FOUND)
  include_directories (${Boost_INCLUDE_DIRS})
endif ()

find_package(ZLIB REQUIRED)

# prefer linking with static libraries
set(CMAKE_FIND_LIBRARY_SUFFIXES ".a" ${CMAKE_FIND_LIBRARY_SUFFIXES})

# check for rt lib. Not needed on OSX.
find_library(RT_LIB NAMES rt)
if (NOT RT_LIB)
  set(RT_LIB "")
endif()
mark_as_advanced(RT_LIB)

include_directories(
  ${CMAKE_CURRENT_SOURCE_DIR}/src/include
  ${MUSER2_INCLUDE_DIR}
  ${CMAKE_CURRENT_BINARY_DIR}/include
  )

list (APPEND CMAKE_CXX_FLAGS "-std=c++11")


add_subdirectory (src)


