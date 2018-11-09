ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasya",
        "age": 12,
    },{
        "name": "petya",
        "age": 10,
    }]
}
daria = {
    "name": "daria",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
        },{
        "name":"pavel",
        "age": 15,
    }]
}
emps = [ivan,daria]

#обратиться к элементу age, провести проверку, если проходит проверку -  печать имени из emps
if emps[0]['children'][0]['age'] >= 18:
    print(emps[0]['name'])
else:
    if emps[0]['children'][1]['age'] >= 18:
        print(emps[0]['name'])
    else:
        if emps[1]['children'][0]['age'] >=18:
            print(emps[1]['name'])
        else:
            if emps[1]['children'][1]['age'] >=18:
                print(emps[1]['name'])





#childrens = emps[0]['children'] + emps[1]['children']
#dc = daria['children']
#dc1 = daria['children'][0]
#dc2 = daria['children'][1]
#dc1v = daria['children'][0]['age'] #daria child 1 age value = 21
#dc2v = daria['children'][1]['age'] #daria child 2 age value = 15
#ic = ivan['children']
#ic1 = ivan['children'][0]
#ic2 = ivan['children'][1]
#ic1v = ivan['children'][0]['age'] #ivan child 1 age value = 12
#ic2v = ivan['children'][1]['age'] #ivan child 2 age value = 10
#ages = (ic1v, ic2v, dc2v, dc1v)
#print(childrens)


#print(emps[1]['children'][0]['age'])
#if dc1v >= 18:   if dc2v >= 18   if ic1v >= 18  if ic2v >= 18





#print(ivan.keys())
#for key, value in daria.items():
    #print(key, value)
