add_executable (muser2 muser2.cc)
target_link_libraries (muser2
  clset
  minisat_gh
  wraps-2
  wraps
  mus-2
  z)
