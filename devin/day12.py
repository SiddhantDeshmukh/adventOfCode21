"""Yikes, how do I format that data automatically"""
"""So, I've taken a dijkstra set of code from stack overflow,
I've changed the graph to be my data set, now I think I just need to
play around until it visits all the small paths only once?
I might just try to make my own code and use this as reference"""
def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths       

def min_path(graph, start, end):
    paths=find_all_paths(graph,start,end)
    print(len(paths))
    mt=10**99
    mpath=[]
    print('\tAll paths:',paths)
    for path in paths:
        t=sum(graph[i][j] for i,j in zip(path,path[1::]))
        print('\t\tevaluating:',path, t)
        if t<mt: 
            mt=t
            mpath=path

    e1=' '.join('{}->{}:{}'.format(i,j,graph[i][j]) for i,j in zip(mpath,mpath[1::]))
    e2=str(sum(graph[i][j] for i,j in zip(mpath,mpath[1::])))
    print('Best path: '+e1+'   Total: '+e2+'\n'  )

if __name__ == "__main__":
    graph = {'start': {'gm':1, 'IK':1, 'CV':1},
             'CV': {'mk':1, 'gm':1, 'start':1, 'kt':1, 'ml':1},
             'mk': {'CV':1, 'sx':1, 'IK':1, 'ml':1},
             'gm': {'IK':1, 'sk':1, 'CV':1, 'ml':1, 'start':1},
             'IK': {'gm':1, 'mk':1, 'ml':1, 'start':1},
             'sk': {'ca':1, 'end':1, 'gm':1, 'kt':1},
             'ca': {'sk':1, 'sx':1, 'VS':1, 'kt':1, 'end':1, 'ml':1},
             'sx': {'mk':1, 'ca':1, 'end':1, 'gy':1, 'kt':1},
             'kt': {'sk':1, 'ml':1, 'ca':1, 'sx':1, 'CV':1},
             'VS': {'ca':1},
             'ml': {'kt':1, 'ca':1, 'mk':1, 'CV':1, 'gm':1, 'IK':1},
             'end': {'sx':1, 'sk':1, 'ca':1},
             'gy': {'sx':1}
             }
    min_path(graph,'start','end')


