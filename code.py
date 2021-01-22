
def are_valid_groups(studNum, groups):
        inGroup = False
        for num in studNum:
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
