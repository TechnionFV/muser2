add_executable (muser2 muser2.cc)

target_link_libraries (muser2
  wraps-2
  wraps
  mus-2
  clset
  minisat_gh
  minisat22
  glucose30
  ${ZLIB_LIBRARY})

