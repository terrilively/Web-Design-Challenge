import pandas as pd
tabledf=pd.read_csv("resources/cities.csv")
print(tabledf.head)
table=tabledf.to_html(index=False)
with open("table.html", "w") as file:
    file.write(table)