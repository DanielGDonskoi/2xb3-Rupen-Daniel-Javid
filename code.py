
def are_valid_groups(studNums, groups):
        inGroup = False
        for num in studNums:
                for group in groups:
                        if (num in group):
                                inGroup = True
                                break
                        else:
                                inGroup = False
		
                if (inGroup):
                        return True
                else:
                        return
