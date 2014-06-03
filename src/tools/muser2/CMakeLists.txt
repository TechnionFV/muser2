add_executable (muser2 muser2.cc)
target_link_libraries (muser2
  clset
  wraps-2
  wraps
  mus-2
  minisat_gh
  minisat22
  ${ZLIB_LIBRARY})
