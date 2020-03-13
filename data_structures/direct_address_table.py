from data_structures.utils.data_structures_visualization import DataStructuresVisualization

class DirectAddressTable:

    """
    This class implements the Abstract Data Type (TAD'S) Direct Address Table, with it's main operations.

    Methods
    -------
    search(value)
        Searches for a value.

    insert(value)
        Insert a value.

    remove()
        Removes a value.
    """

    def __init__(self):

        self.table = []

    def __repr__(self):

        return "\nDirect Address Table:\n{0}".format(DataStructuresVisualization.direct_address_table(self.table))

    def insert(self, value):

        try:
            self.table[value-1] = value
        except IndexError:
            table_aux = [None] * (value-len(self.table))
            self.table = self.table + table_aux
            self.table[value-1] = value

    def delete(self, value):

        self.table[value] = None

    def search(self, value):

        return self.table[value-1]
