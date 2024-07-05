
def deep_update(d, u):
    for k, v in u.items():
        if isinstance(v, dict):
            bvalue = d.get(k)
            if isinstance(bvalue, dict):
                deep_update(bvalue, v)
            else:
                d[k] = v
        else:
            d[k] = v
    return d