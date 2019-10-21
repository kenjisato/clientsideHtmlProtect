#' Wrapper for Clientside HTML Password Protect by Max Laumeister and Zoltan Galli.
#'
#' @param file Path to file to password protected
#' @param passphrase Single character string. Passphrase for open the file
#' @param template Template HTML file
#'
#' @return Character string of protected file.
#' @export
#'
#' @examples
#'\dontrun{
#'file <- system.file("sample", "hello.html", package = "clientsideHtmlProtect")
#'protected <- protect(file, "abc")
#'writeLines(protected, "protect.html")
#'file.remove("protect.html")
#'}
protect <- function(file, passphrase, template = NULL) {

  if (is.null(template)) {
    template <- system.file("template", "decryptTemplate.html",
                            package = "clientsideHtmlProtect")
  }

  file <- tools::file_path_as_absolute(file)

  encrypt <- reticulate::import_from_path(
                module = "encrypt",
                system.file("src", "python",
                            package = "clientsideHtmlProtect"))

  doc <- encrypt$protect_py(inputfile = file, passphrase = passphrase,
                            template = template)

}
