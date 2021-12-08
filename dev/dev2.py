
def solution(n, recipes, orders):
    recipes = [r.split(" ") for r in recipes]
    orders = [o.split(" ") for o in orders]

    recipeD = {}
    fireD = {}
    for menu, time in recipes:
        recipeD[menu] = int(time)

    for i, (ord, t) in enumerate(orders):
        
        if len(fireD) != n:
            fire = i % n
            fireD[fire] = int(t)+recipeD[ord]
        
        else:
            fire = list(fireD.values()).index(min(fireD.values()))
            fireD[fire] = fireD[fire] + recipeD[ord]
        if i == len(orders)-1:
            return fireD[fire]



n = 3
recipes = ["SPAGHETTI 3", "FRIEDRICE 2", "PIZZA 8"]
orders = ["PIZZA 1", "FRIEDRICE 2", "SPAGHETTI 4", "SPAGHETTI 6", "PIZZA 7", "SPAGHETTI 8"]
print(solution(n, recipes, orders))
#results = 7