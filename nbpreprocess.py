from nbconvert.preprocessors import Preprocessor


class RemoveSlideShowNotesCells(Preprocessor):
    def preprocess(self, notebook, resources):
        executable_cells = []
        for cell in notebook.cells:
            if cell.metadata.get("slideshow", {}).get("slide_type") == "notes":
                continue
            executable_cells.append(cell)
        notebook.cells = executable_cells
        return notebook, resources
