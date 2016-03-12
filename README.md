# js2markdown

## Description

`JStoMarkdown.py` is a script which creates a markdown and html document using a javascript code file.

`JStoMarkdown.py` receives two mandatory parameters:

- `.js` script (This script should include between comments all markdown notes, see `functions.js`. Code does not have to be commmented)
- output format (html)

And optional paramenters:

- css


## Usage example

```bash
python JStoMarkdown.py functions.js html style.css
```

## Notes

This script requires `pypandoc` wrapper.

