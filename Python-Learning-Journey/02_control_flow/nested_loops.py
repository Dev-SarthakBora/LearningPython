# nested_loops.py
for i in range(1, 6):          # outer loop for rows
    for j in range(1, 6):      # inner loop for columns
        print(i * j, end="\t") # print product in table format
    print()  # new line after each row

