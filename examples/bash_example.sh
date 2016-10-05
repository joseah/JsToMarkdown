#' ---
#' title: Create, rename and remove files in terminal
#' author: José Alquicira Hernández
#' ---
#'
#' # Overview
#' 
#' Learn to create, rename and remove files using the terminal.
#'

#' # File operations
#'
#' ## Create a file
#'
#' You can use the 'touch' command to create an empty file.
#'
#' Here, we create a file called `file.txt`
#'

touch file.txt

#' Write some text content with `echo`:

echo "This is a string" >> file.txt

#' ## Rename a file
#'
#' You can rename a file using the `mv` command.
#'
#' Here we rename `file.txt` to `string`.
#'

mv file.txt string

#' ## Remove file
#'
#' Use `rm` to remove a file:
#'

rm string

#' > If you want to remove a directory, add the `-r` flag
