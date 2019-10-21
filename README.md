
# clientsideHtmlProtect

<!-- badges: start -->
<!-- badges: end -->

**clientsideHtmlProtect** R package provides a wrapper function for 
Client-Side HTML Password Protect by Max Laumeister and Zoltán Gálli  <https://www.maxlaumeister.com/clientside-html-password/>.
Function `protect()` simply calls a modified version of the original
Python script. 

## Dependency

R packages:

- reticulate to run Python from within R

Python Environment:

1. Python3
1. [pycrypto](https://pypi.org/project/pycrypto/) for AES: `pip3 install pycrypto`
1. Python version of [pbkdf2](https://pypi.org/project/pbkdf2/: `pip3 install pbkdf2`

## Installation

You can install the development version of clientsideHtmlPassword from [GitHub](https://CRAN.R-project.org) with:

``` r
remotes::install_github("kenjisato/clientsideHtmlProtect")
```

## Example

This is a basic example which shows you how to solve a common problem:

``` r
library(clientsideHtmlPassword)

# path to a file you want to protect
file <- system.file("sample", "hello.html", package = "clientsideHtmlProtect")

# Protect
passphrase <- "strongpassword"
protected <- protect(file, passphrase)

# save protected file as a HTML file
writeLines(protected, "protect.html")
```

