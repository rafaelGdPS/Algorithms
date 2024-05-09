def study_schedule(permanence_period, target_time):
    if target_time is None or target_time == "":
        return None

    target_repeat = 0

    for period in permanence_period:

        if not isinstance(period[0], int) or not isinstance(period[1], int):
            return None

        start = period[0]
        end = period[1]

        if start <= target_time <= end:
            target_repeat += 1

    return target_repeat


period_permanence = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
target = 4

if __name__ == "__main__":
    print(f": {study_schedule(period_permanence, target)}")
