import shelve

s = shelve.open('test_shelf.txt', writeback=True)
try:
    s['01'] = { 'int': 10, 'float':9.5, 'string':"Sample data" }

    s['01']['string'] = 'Isaac Murisa'
    existing = s['01']
    d = s['01']['string']

    s['usr'] = { 'password': '***' }
    m = s['usr']['password']

    del s['01']['int']

    klist = list(s.keys())
    n = []
    n.append('me')
    n.append('you')
    
    m = ['a', 'b', 'd', 'c', 'v']
    

finally:
    s.close()

print existing
print d
print klist
print n