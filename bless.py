
def event_summary(event_name, normal_event, budget):
    return f"{event_name} has a total cost of {normal_event} and it is {budget}."

study = event_summary("Study Day", normal_event, budget)
print(study)