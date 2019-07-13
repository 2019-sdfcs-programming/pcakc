def calc(d):
    if d['__init__'] != 'calc':
        raise NoRequiredData

    if d['__type__'] == 'svt' or d['__type__'] == 'fma' or d['__type__'] == 'p1mv1' or d['__type__'] == 'ift' or d['__type__'] == 'p2mv2' :
        # [s, v, t] [f, m, a] [p, m, v] [i, f, t] 순서대로
        if d['__requ__'] == 's' or d['__requ__'] == 'f' or d['__requ__'] == 'p1' or d['__requ__'] == 'i' or d['__requ__'] == 'p2':
            calced = d['data'][0] * d['data'][1]
        elif d['__requ__'] == 'v' or d['__requ__'] == 'm' or d['__requ__'] == 'm' or d['__requ__'] == 'f' or d['__requ__'] == 'm':
            calced = d['data'][0] / d['data'][1]
        elif d['__requ__'] == 't' or d['__requ__'] == 'a' or d['__requ__'] == 'v1' or d['__requ__'] == 't' or d['__requ__'] == 'v2':
            calced = d['data'][0] / d['data'][1]
        else:
            raise NoRequiredData
    elif d['__type__'] == '2asvv':
        #[a,s,v1,v2] 순서대로
        if d['__requ__'] == 'a':
            calced = ((d['data'][2]**2)-(d['data'][1]**2))/(2*d['data'][0])
        elif d['__requ__'] == 's':
            calced = (d['data'][2]**2-d['data'][1]**2)/(2*d['data'][0])
        elif d['__requ__'] =='v2':
            calced = ((2*d['data'][0]*d['data'][1])+(d['data'][2]**2))**0.5
        elif d['__requ__'] =='v1':
            calced = ((d['data'][2]**2)-(2*d['data'][0]*d['data'][1]))**0.5
    elif d['__type__'] == 'vvat':
        #[v1,v2,a,t] 순서대로
        if d['__requ__'] == 'v2':
            calced = d['data'][0]+(d['data'][1]*d['data'][2])
        elif d['__requ__'] == 'v1':
            calced = d['data'][0]-(d['data'][1]*d['data'][2])
        elif d['__requ__'] == 'a':
            calced = (d['data'][1]-d['data'][0])/d['data'][2] 
        elif d['__requ__'] == 't':
            calced = (d['data'][1]-d['data'][0])/d['data'][2] 
    elif d['__type__'] == 'svtat':
        #[s,v1,a,t] 순서대로
        if d['__requ__'] == 's':
            calced = (d['data'][0]*d['data'][2])+((d['data'][1])*(d['data'][2]**2))/2
        elif d['__requ__'] == 'v1':
            calced = (d['data'][0]-(d['data'][1]*(d['data'][2]**2))/2)/d['data'][2]
        elif d['__requ__'] == 'a':
            calced = (2/(d['data'][2]**2))*(d['data'][0]-(d['data'][1]*d['data'][2]))
    elif d['__type__'] == 'ip1p2':
        #[i,p1,p2] 순서대로
        if d['__requ__'] == 'i':
            calced = d['data'][1]-d['data'][0]
        elif d['__requ__'] == 'p1':
            calced = d['data'][1]-d['data'][0]
        elif d['__requ__'] == 'p2':
            calced = d['data'][0]+d['data'][1]
    
    result = {
        '__init__' : 'calced',
        '__type__' : d['__type__'],
        'received' : d['data'],
        'result' : calced
    }
    return result

if __name__ == '__main__':
    dtemplate = {
        '__init__' : 'calc',
        '__type__' : 'svtat',
        '__requ__' : 'a',
        'data' : [16, 2, 4]
    }
    print(calc(dtemplate))