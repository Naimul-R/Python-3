def Http_status (status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internet Error"
        case _:
            return "Unknown status"
        
print (Http_status (200))
print (Http_status (500))
print (Http_status (5232))


##Merge Dictonary 
dict1 = {"a":10, "b":20, "c":30}
dict2 = {"d":40, "e":50}

merged = dict1 | dict2
print (merged)
