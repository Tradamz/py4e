x = [1, 2, 3, 4, 5, 6]
t = [1, 2, 3, 4, 5, 6]
t.append([x])          # WRONG!
t = t.append(x)        # WRONG!
t + [x]                # WRONG!
t = t + x              # WRONG!

print(t)
