from nbconvert.preprocessors import Preprocessor
import nbsphinx


class RemoveSlideShowNotesCells(Preprocessor):
    def preprocess(self, notebook, resources):
        executable_cells = []
        for cell in notebook.cells:
            if cell.metadata.get("slideshow", {}).get("slide_type") == "notes":
                continue
            executable_cells.append(cell)
        notebook.cells = executable_cells
        return notebook, resources


class NbSphinxRST(nbsphinx.Exporter):
    def __init__(self, config=None):
        super().__init__()
        self.register_preprocessor(
            RemoveSlideShowNotesCells(config=config), enabled=True
        )
