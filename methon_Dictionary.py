dictionaty = {
     "Abu" : "A programmer",
     "book"  : "A reading material"
}
# print(dictionary["Abu"])

print(list(dictionaty.keys()))
print(dictionaty.values())
print(dictionaty.items)

updateDic = {
     "mango" : "fruit"
} 
dictionaty.update(updateDic)
print(dictionaty)
print(dictionaty.get("abu1"))
#print(dictionaty["abu1"] #error
