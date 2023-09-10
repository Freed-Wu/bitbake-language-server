cmake_minimum_required(VERSION 3.10)
include(FetchContent)
FetchContent_Declare(
  tree-sitter-bitbake
  URL https://github.com/amaanq/tree-sitter-bitbake/archive/refs/tags/v1.0.0.tar.gz
  URL_HASH SHA256=2ecddb6e00764fd0cecf7ad5aa732c5830147188f6f1a9bd6cbbaf328bf1bb79)
FetchContent_MakeAvailable(tree-sitter-bitbake)
include_directories(${tree-sitter-bitbake_SOURCE_DIR}/src)
add_library(parser SHARED ${tree-sitter-bitbake_SOURCE_DIR}/src/parser.c)
if(NOT DEFINED SKBUILD_PLATLIB_DIR)
  set(SKBUILD_PLATLIB_DIR ${CMAKE_SOURCE_DIR}/src)
endif()
set(CMAKE_INSTALL_LIBDIR ${SKBUILD_PLATLIB_DIR}/bitbake_language_server/data/lib)
install(TARGETS parser RUNTIME)
