import os
smb = os
res = []
def traverse(path):
    fs = {f:os.path.join(path, f) for f in smb.listdir(path)}
    for f in fs:
        cur_p = fs[f]
        if smb.path.isdir(cur_p) and not smb.path.islink(cur_p):
            traverse(cur_p)
        elif not smb.path.islink(cur_p) and smb.path.isfile(cur_p):
            res.append(cur_p)
    return
traverse(path_you_transfer)
print(res)

        