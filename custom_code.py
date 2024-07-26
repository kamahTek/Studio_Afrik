# Identify duplicates
# Created a reusable function to help find duplicates in specified column.

def dup(data_frame, column_name):

    print("Checking for Duplicates")
    print("")
    for col in column_name:
        print(f"=> {col}")
        dup = data_frame[col].duplicated().value_counts()
        print(dup)
        dup_value = dup.index
        if dup_value.__contains__(True):
            print(" ***Found duplicates")
        else:
            print(" ***No duplicates")
        print("------------------")
        print("")


# Clean finance dataframe
def finance_col(dataframe, column_name):
    for money_col in column_name:
        dataframe[money_col] = dataframe[money_col].str.replace('$', '').str.replace(',', '').astype('int64')
    pass