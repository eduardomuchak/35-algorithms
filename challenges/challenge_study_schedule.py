def study_schedule(permanence_period, target_time):
    try:
        students = 0
        for start_time, end_time in permanence_period:
            if start_time <= target_time and end_time >= target_time:
                students += 1
    except TypeError:
        return None

    return students
