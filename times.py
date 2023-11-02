import datetime


# Takes a start_time,
# end_time,
# number of time intervals desired (which splits the time period into multiple time periods),
# the gap between the intervals (which decides the space between the end of 1 time period to
# the start of another)
def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time,
                                              "%Y-%m-%d %H:%M:%S")  # strptime converts the string to a datetime object
    end_time_s = datetime.datetime.strptime(end_time,
                                            "%Y-%m-%d %H:%M:%S")  # strptime converts the string to a datetime object
    d = (end_time_s - start_time_s).total_seconds() / number_of_intervals + gap_between_intervals_s \
        * (1 / number_of_intervals - 1)
    sec_range = [(start_time_s + datetime.timedelta(seconds=i * d + i * gap_between_intervals_s),
                  start_time_s + datetime.timedelta(seconds=(i + 1) * d + i * gap_between_intervals_s))
                 for i in range(number_of_intervals)]
    return [(ta.strftime("%Y-%m-%d %H:%M:%S"), tb.strftime("%Y-%m-%d %H:%M:%S")) for ta, tb in sec_range]


def compute_overlap_time(range1, range2):
    overlap_time = []
    for start1, end1 in range1:
        for start2, end2 in range2:
            low = max(start1, start2)
            high = min(end1, end2)
            overlap_time.append((low, high))
    return overlap_time


if __name__ == "__main__":
    # print(compute_overlap_time(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 ""15:00:00", "2010-01-12 ""17:00:00")))
    # print(compute_overlap_time(time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60), time_range("2010-01-12 09:00:00", "2010-01-12 12:00:00", 2, 120)))
    #print(compute_overlap_time(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),time_range("2010-01-12 ""12:00:00", "2010-01-12 ""15:00:00")))
    pass
