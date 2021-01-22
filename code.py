def are_valid_groups(students, groups):
        for group in groups:
                for student in group:
                        if student in students:
                                students.remove(student)
        if not students:
                return True
        else:
                return False
