
import _trw
from _trw import MRFEnergy, TypeBinary, TypeGeneral

if __name__ == '__main__':
    import numpy as np
    
    # e = MRFEnergy[TypeBinary](TypeBinary.GlobalSize())
    # nodeid0 = e.add_node(TypeBinary.LocalSize(), TypeBinary.NodeData(2,5))
    # nodeid1 = e.add_node(TypeBinary.LocalSize(), TypeBinary.NodeData(10,1))
    # e.add_edge(nodeid0, nodeid1, TypeBinary.EdgeData(0, 3, 3, 0))
    # e.minimize_bp(printiter=1, printminiter=0, itermax=5)
    # print e.get_solution(np.array([nodeid0, nodeid1]))
    
    # e = MRFEnergy[TypeGeneral](TypeGeneral.GlobalSize())
    # nodeid0 = e.add_node(TypeGeneral.LocalSize(2), TypeGeneral.NodeData([2,5]))
    # nodeid1 = e.add_node(TypeGeneral.LocalSize(2), TypeGeneral.NodeData([10,1]))
    # e.add_edge(nodeid0, nodeid1, TypeGeneral.EdgeData(2))
    # e.minimize_trw(printiter=1, printminiter=0, itermax=5)
    # print e.get_solution(np.array([nodeid0, nodeid1]))
    
    e = MRFEnergy[TypeGeneral](TypeGeneral.GlobalSize())
    D = np.zeros((2,3))
    D[0,0] = 2
    D[1,0] = 5
    D[0,1] = 10
    D[1,1] = 2
    D[0,2] = 3
    D[1,2] = 3
    nodeids = e.add_grid_nodes(D)
    print nodeids.shape
    # ed = TypeGeneral.EdgeData([0, 3, 3, 0]);
    ed = np.ones((2,4))
    e.add_grid_edges_direction_local(nodeids, ed, 0, -1)
    e.minimize_bp(printiter=1, printminiter=0, itermax=10)
    labels = e.get_solution(nodeids)
    print labels
