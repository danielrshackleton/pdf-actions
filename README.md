# PDF_Scanner

PDF_Scanner is a PDF action suite using Python, which takes a PDF file and modifies it with a number of useful actions to be migrated into an existing codebase rather than using the command line.


## Installation

User must have `pipenv` installed.

Run `pipenv install` in command line from within project folder.

## Usage
- **add_blank** - Add a blank page at the specified page.
- **encrypt** - Encrypt the PDF file.
- **decrypt** - Decrypt the PDF file.
- **get_range** - Return a new PDF file containing the pages specified.
- **merge** - Merge two PDF files together.
- **remove_blank** - Remove blank pages from the PDF file.
- **remove_page** - Remove the specified page number from the PDF file.
- **rotate** - Rotate the PDF file.
- **scan_form** - Scan a PDF form and output the results as key/value pairs.
