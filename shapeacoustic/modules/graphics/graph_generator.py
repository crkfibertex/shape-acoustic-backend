class GraphGenerator:
    def __init__(self, data):
        self.data = data

    def generate(self, graph_type):

        if graph_type == "curve":
            return "Generated a curve graph"

        # Generate graph
        else:
            return "Could not generate graph : Graph type not recognized"