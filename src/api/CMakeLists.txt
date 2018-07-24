add_library ( muser2_api STATIC 
	      muser2_api.cc 
	      muser2_impl.cc
            )
target_link_libraries (muser2_api
  wraps-2
  wraps
  mus-2
  clset
  minisat_gh
  minisat22
  glucose30
  ${ZLIB_LIBRARY} 
)
