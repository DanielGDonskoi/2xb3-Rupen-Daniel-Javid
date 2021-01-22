samplestudents = ["4","3","5"]
samplegroups = [ ["2","6","7"], ["4","3","5"] ]
def are_valid_groups(groups,students):
    for i in students:
        current = i
        for lists in groups:
            if current not in lists:
                return 
    return True

print(are_valid_groups(samplegroups,samplestudents))
