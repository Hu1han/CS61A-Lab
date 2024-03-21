def delete(t, x):

    new_branches = []
    for b in t.branches:
        n=b.branches
        if b.label == x:
            new_branches.extend(n)
        else: 
            delete(b,x)
            new_branches.extend([b])

    
    t.branches = new_branches