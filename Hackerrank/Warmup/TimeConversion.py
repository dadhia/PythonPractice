
def convert(timestamp):
    # get the values from the timestamp for HH, MM, SS in values[0], values[1], and values[2]
    values = list(timestamp[:-2].split(':'))
    if timestamp.endswith("AM"):
        if values[0] == "12":
            values[0] = "00"
    elif values[0] != "12":
            values[0] = str(int(values[0]) + 12)
    return "%s:%s:%s" % tuple(values)


inputTimestamp = input().strip()
outputTimestamp = convert(inputTimestamp)
print(outputTimestamp)
