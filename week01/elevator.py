from itertools import groupby


def elevator_steps(people_weight, floors, elevator_floors,
                   max_persons, max_weight):
    if not people_weight or not floors:
        return 0

    if sorted(floors)[-1] > elevator_floors:
        raise Exception("The elevator max floor is {}".format(elevator_floors))

    steps = 0
    while(len(people_weight) > 0):
        for i in range(max_persons):
            if sum(people_weight[:max_persons-i]) > max_weight:
                if len(people_weight[:max_persons-i]) == 1:
                    raise Exception("Elevator overweight!")
                continue
            else:
                current_list = people_weight[:max_persons-i]
                current_floors = floors[:max_persons-i]
                people_weight = people_weight[max_persons-i:]
                floors = floors[max_persons-i:]
                break

        steps += len([list(j) for i, j in groupby(current_floors)]) + 1

    return steps
