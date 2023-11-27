def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badges = [badge_maker(name) for name in names]
    return badges

def assign_rooms(names):
    assignments = [f"Hello, {name}! You'll be in room {i}." for i, name in enumerate(names, start=1)]
    return assignments

def printer(names):
    badges = batch_badge_creator(names)
    assignments = assign_rooms(names)

    for badge in badges:
        print(badge)

    for assignment in assignments:
        print(assignment)