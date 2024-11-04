# uuid, cuid nebo int

class Developer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"{self.name}"

class Estimate:
    def __init__(self, developer, value):
        self.developer = developer
        self.value = value

    # def __repr__(self):
    #     return f"{self.value}"

# [1, 3, 6, 2, 8]

# co se stane kdyz bude estimates prazdny list
# co kdyz bude vyvojar jenom jeden
# co kdyz vyjdou odhady jako stejne hodnoty

def identify_extremes(estimates):
    if estimates is None:
        raise Exception("Estimates cannot be None")

    if len(estimates) <= 1:
        raise Exception("Not enough developers")

    lowest_estimate = None
    highest_estimate = None # 16

    for estimate in estimates:
        if highest_estimate is None or estimate.value > highest_estimate.value:
            highest_estimate = estimate
        if lowest_estimate is None or estimate.value < lowest_estimate.value:
            lowest_estimate = estimate

    if lowest_estimate == highest_estimate:
        return ()

    return lowest_estimate.developer, highest_estimate.developer
