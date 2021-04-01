def count_items_matching_a_rule(items, ruleKey, ruleValue):
    category = {"type": 0, "color": 1, "name": 2}
    count = 0
    for item in items:  # O(n)
        if item[category[ruleKey]] == ruleValue:
            count += 1

    return count


# Complexity: O(n) for time as we loop over entire array and O(1) space complexity as no additional space required

items1 = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
ruleKey1 = "type"
ruleValue1 = "phone"

print(count_items_matching_a_rule(items1, ruleKey1, ruleValue1))
