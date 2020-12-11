dt = 
def collect(dt, ls=[]):
    for k in dt:
        if k == 'collect':
            ls.append(dt[k])
        elif k == 'next':
            if isinstance(dt[k], dict):
                return collect(dt[k], ls)
            else:
                return ls


print(collect(dt))
