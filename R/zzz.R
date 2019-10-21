.onLoad <- function(libname, pkgname) {
  reticulate::use_python(python = Sys.which("python3"), required = TRUE)
}
