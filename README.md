# Src2markdown

## Description

`JStoMarkdown.py`, `PythontoMarkdown.py` and `PerltoMarkdown.py` are scripts which create markdown and html documents using a source code file (`.js`,`.py`, `.pl`).

All scripts receive two mandatory parameters:

- a script (This script should include between comments all markdown notes, see `js_example.js`. Code does not have to be commented)
- output format (html)

And optional parameters:

- css


## Usage example

```bash
python JStoMarkdown.py -s js_example.js -o html -c github-markdown.css
```

## Notes

- These scripts requires `pandoc` and `pypandoc` wrapper.

Install `pypandoc` via `pip`:

```bash
sudo pip install pypandoc
```

- See [marked style](http://markedstyle.com/) for more css files

