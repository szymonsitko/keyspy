def replace_surroundings(char, target):
    first_target_index = 0
    last_target_index = len(target) - 1
    if target[first_target_index] == char and target[last_target_index] == char:
        return target[first_target_index + 1:last_target_index]
    else:
        return target
