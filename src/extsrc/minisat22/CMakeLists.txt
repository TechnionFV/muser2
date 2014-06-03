include_directories (inc)
add_library (minisat22 STATIC
  core/solver.cc
  simp/simp_solver.cc
  utils/options.cc
  utils/system.cc)
  
  