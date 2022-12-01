import LinkedList as ll

ranking = ll.LinkedList()
ranking.add(ll.Node("Taxi 1", None))
ranking.add(ll.Node("Taxi 2", ranking.head))
ranking.add(ll.Node("Taxi 3", ranking.head))
ranking.add(ll.Node("Taxi 4", ranking.head))
print(ranking)
ranking.swap(ranking.node(0), ranking.node(2))
print(ranking)
ranking.swap(ranking.node(0), ranking.node(1))
print(ranking)
