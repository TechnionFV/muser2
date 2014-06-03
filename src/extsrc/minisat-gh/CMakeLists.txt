add_subdirectory(core)
add_subdirectory(simp)
add_subdirectory(utils)
add_library(minisat_gh STATIC 
  $<TARGET_OBJECTS:minisat_gh_core>
  $<TARGET_OBJECTS:minisat_gh_simp>
  $<TARGET_OBJECTS:minisat_gh_utils>)