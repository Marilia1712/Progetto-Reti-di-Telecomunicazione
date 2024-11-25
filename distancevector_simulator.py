class Node:
    def __init__(self, name, neighbors):
        """
        Inizializza un nodo con il suo nome e la lista di vicini.
        Ogni nodo ha una tabella di routing, inizialmente vuota.
        """
        self.name = name
        self.neighbors = neighbors
        self.routing_table = {name: 0}  # La distanza da sé stesso è 0
        for neighbor, dist in neighbors.items():
            self.routing_table[neighbor] = dist  # Distanza ai vicini

    def update_routing_table(self, all_nodes):
        """
        Aggiorna la tabella di routing utilizzando l'algoritmo Distance Vector.
        Recepisce le tabelle di routing dei nodi vicini.
        """
        updated = False
        for neighbor in self.neighbors:
            # Prendi la tabella di routing del vicino
            neighbor_table = all_nodes[neighbor].routing_table
            for node, distance in neighbor_table.items():
                if node not in self.routing_table:
                    self.routing_table[node] = self.neighbors[neighbor] + distance
                    updated = True
                else:
                    # Confronta se la nuova distanza è minore
                    new_distance = self.neighbors[neighbor] + distance
                    if new_distance < self.routing_table[node]:
                        self.routing_table[node] = new_distance
                        updated = True
        return updated

    def print_routing_table(self):
        """
        Stampa la tabella di routing del nodo.
        """
        print(f"Tabella di routing per il nodo {self.name}:")
        for destination, distance in self.routing_table.items():
            print(f"  Destinazione {destination}: {distance}")
        print()

def distance_vector_routing(nodes, iterations=5):
    """
    Simula l'algoritmo di routing Distance Vector per un dato numero di iterazioni.
    """
    for i in range(iterations):
        print(f"\nIterazione {i + 1}:")
        updated = False
        for node in nodes.values():
            if node.update_routing_table(nodes):
                updated = True
        
        # Stampa le tabelle di routing dopo ogni iterazione
        for node in nodes.values():
            node.print_routing_table()

        if not updated:
            print("Le tabelle di routing non sono più cambiate. Terminazione anticipata.")
            break

# Definiamo la rete come un dizionario di nodi
nodes = {
    'A': Node('A', {'B': 1, 'C': 4}),
    'B': Node('B', {'A': 1, 'C': 2, 'D': 5}),
    'C': Node('C', {'A': 4, 'B': 2, 'D': 1}),
    'D': Node('D', {'B': 5, 'C': 1})
}

# Eseguiamo l'algoritmo di routing per 5 iterazioni
distance_vector_routing(nodes, iterations=5)
