def can_attend_all(events):
    events = sorted(events)

    for i in range(1, len(events)):
        if events[i][0] < events[i - 1][1]:
            return False

    return True


print(can_attend_all([(9, 10), (10, 11), (11, 12)]))


print(can_attend_all([(9, 11), (10, 12)]))



def min_rooms_required(events):
    if not events:
        return 0

    starts = sorted(start for start, end in events)
    ends = sorted(end for start, end in events)

    rooms = 0
    max_rooms = 0
    i = 0
    j = 0

    while i < len(events):
        if starts[i] < ends[j]:
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            i += 1
        else:
            rooms -= 1
            j += 1

    return max_rooms



events = [(9, 10), (9, 11), (10, 12)]

print(min_rooms_required(events))


