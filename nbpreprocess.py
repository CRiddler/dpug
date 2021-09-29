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

    def from_notebook_node(self, nb, resources=None, **kw):
        rststr, resource = super().from_notebook_node(nb=nb, resources=resources, **kw)

        # Inject dpug metadata variables from notebook into rst representation
        if "dpug" in getattr(nb, "metadata", {}):
            dpug_meta = nb.metadata["dpug"]
            author_str = "*Authored by: {author}, on {date}*\n".format(**dpug_meta)

            rststr = rststr.split("\n", maxsplit=3)
            rststr.insert(2, author_str)
            rststr = "\n".join(rststr)

        return rststr, resource
