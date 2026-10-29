def participant_cost(attendees, food_per_person, trans_per_person):
    return attendees * (food_per_person + trans_per_person)

#Normal Cost
normal_cost = participant_cost(10, 800, 200)
print(normal_cost)

#Zero Cost
zero_cost = participant_cost(0, 800, 200)
print(zero_cost)

def event_total(normal_cost, venue_cost):
    return normal_cost + venue_cost

#Normal Event Total Cost
normal_event = event_total(normal_cost, 5000)
print(normal_event)

#Zero Event Total Cost
zero_event = event_total(zero_cost, 5000)
print(zero_event)

def budget_status(budget, normal_event):
    if normal_event <= budget:
        return "Within budget"
    else:
        return "Over budget"
    
budget = budget_status(16000, normal_event)
print(budget)

def event_summary(event_name, normal_event, budget):
    return f"{event_name} has a total cost of {normal_event} and it is {budget}."

study = event_summary("Study Day", normal_event, budget)
print(study)
