def study_schedule(permanence_period, target_time):
    cont = 0
    for entry, exit in permanence_period:
        try:
            if entry <= target_time <= exit:
                cont += 1
        except TypeError:
            return None

    return cont

# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# permanence_period = [(2, None), (1, 2)]
# target_time = 1
