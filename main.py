from pyamaze import maze, agent, textLabel

def dijkstra(m, inicio=None):

    nvisitado = {n:float('inf') for n in m.grid}
    nvisitado[inicio] = 0
    visitado = {}
    caminhoReverso = {}

    while nvisitado:
        atualCell = min(nvisitado, key=nvisitado.get) #procura a celula de valor minimo e coloca na celula atual
        visitado[atualCell] = nvisitado[atualCell] #copia os dados da não visitada para a visitada
        if atualCell == m._goal:
            break
        for d in 'EWNS': #explora os vizinhos
            if m.maze_map[atualCell][d] == True:
                if d == 'E':
                    visinhaCell=(atualCell[0], atualCell[1] + 1)
                elif d == 'W':
                    visinhaCell=(atualCell[0], atualCell[1] - 1)
                elif d == 'S':
                    visinhaCell=(atualCell[0] + 1, atualCell[1])
                elif d == 'N':
                    visinhaCell=(atualCell[0] - 1, atualCell[1])
                if visinhaCell in visitado:
                    continue
                distancia = nvisitado[atualCell] + 1
                if distancia < nvisitado[visinhaCell]: #nvisitado[visinhaCell] = inf
                    nvisitado[visinhaCell] = distancia # atualiza a distancia
                    caminhoReverso[visinhaCell] = atualCell 
        nvisitado.pop(atualCell)
    
    fwdPath = {}
    cell = m._goal
    while cell != inicio:
        fwdPath[caminhoReverso[cell]]=cell
        cell = caminhoReverso[cell]
    
    return fwdPath, visitado[(1,1)]

if __name__ =='__main__':
    widthMaze = 30
    heightMaze = 30

    m = maze(widthMaze, heightMaze) #size
    m.CreateMaze(theme="dark") #goal, patern(h, v) saveMaze = True
    a = agent(m, footprints=True) #filled, shape arrow

    inicio = (widthMaze, heightMaze)
    path, c = dijkstra(m, inicio=(widthMaze, heightMaze))

    textLabel(m, 'Custo total', c)

    l1 = textLabel(m, "Total Cells", m.rows*m.cols)

    m.tracePath({a:path}, delay= 100) #faz o caminho, basta passar o agente:caminho(tupla)

    m.run()