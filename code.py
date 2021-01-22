def are_valid_groups(students, groups):
        
        newstudents = []
        for student in students:
                newstudents.append(str(student))
        students = newstudents

        newgroups = []
        for group in groups:
                newgroup = []
                for student in group:
                        newgroup.append(str(student))
                newgroups.append(newgroup)
        groups = newgroups


        for group in groups:
                if len(group) < 2 or len(group) > 3:
                        return False

        usedstudents = []
        for group in groups:
                for student in group:
                        if student in usedstudents:
                                return False
                        elif student not in students:
                                return False
                        elif student in students:
                                students.remove(student)
                                usedstudents.append(student)
        if not students:
                return True
        else:
                return False
