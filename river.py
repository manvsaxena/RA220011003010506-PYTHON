rivers = {}

rivers["nile"] = "egpyt"
rivers['ganga'] = 'india'
rivers["yamuna"] = 'india'
rivers["amazon"] = 'america'
rivers["missippi"] = 'america'

for key,value in rivers.items():
    print("The "+ key.title() + " runs through " +  value.title())

for keys in rivers.keys():
    print(keys+" River")

for values in rivers.values():
    print("Country: "+values)