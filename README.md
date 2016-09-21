# Src2markdown

## Description

`SrctoMarkdown.py` is a script which creates markdown and html documents using a source code file (`.js`,`.py`,`.pl`, `.R`,`.sh`).

Two mandatory parameters are requested:

- a script (This script should include between comments all markdown notes, see `SrctoMarkdown.py` file. Code does not have to be commented)
- output format (html)

And optional parameters:

- css


## Usage examples

```bash
Python SrctoMarkdown.py -s python_example.py  -o html -c github-markdown.css
```


## Notes

- Requires `pandoc` and `pypandoc` wrapper.

Install `pypandoc` via `pip`:

```bash
sudo pip install pypandoc
```

- See [marked style](http://markedstyle.com/) for more css files

## Contributors

- José Alquicira Hernández