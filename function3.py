def display_result(students):
    total_percentage=0
    for s in students:
        total=sum(s["marks"])
        percentage=round(total/len(s["marks"]),2)
        s["total"]=total
        s["percentage"]=percentage
        print(s)
        total_percentage+=s["percentage"]
    return round(total_percentage/len(students),2)

list_of_students=[{"name":"Sarim","marks":[45,74,85,85,65,65]},
{"name":"Adeem","marks":[65,84,80,81,65,55]},
{"name":"Aneeque","marks":[98,94,80,89,69,85]},
{"name":"saadan","marks":[95,44,73,85,67,45]}
]
avg=display_result(list_of_students)
print("average percentage of all students are:",avg)