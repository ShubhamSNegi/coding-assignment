units = { "XS": 10, "S": 20, "M": 40, "L": 80, "XL": 160, "XXL": 320}
 
prices = {
    "Delhi": { "XS": 12, "S": 23, "M": 45, "L": 77.4, "XL": 140, "XXL": 282},
    "Mumbai": { "XS": 14, "S": 0, "M": 41.3, "L": 89, "XL": 130, "XXL": 297},
    "Kolkata": { "XS": 11, "S": 20, "M": 0, "L": 67, "XL": 118, "XXL": 0}
}
 
def calculate_minimum(capacity, time):
    output = {"Output": []}
    unit_keys = ["XXL", "XL", "L", "M", "S", "XS"]
    for region in prices.keys():
        region_outputs = []
        for i in range(len(unit_keys)):
            input_capacity = capacity
            total_cost = 0
            boxes = []
            for j in range(i, len(unit_keys)):
                if prices[region][unit_keys[j]]:
                    no_of_boxes = input_capacity//units.get(unit_keys[j])
                    boxes_cost = no_of_boxes * prices[region][unit_keys[j]]
                    total_cost += boxes_cost
                    if no_of_boxes > 0:
                        boxes.append((unit_keys[j], no_of_boxes))
                        input_capacity -= no_of_boxes*units.get(unit_keys[j])

            region_outputs.append({
                "region": region,
                "total_cost": total_cost*time,
                "boxes": boxes
            })
        region_final_output = region_outputs[0]
        for region_output in region_outputs:
            if region_output.get('total_cost') < region_final_output.get('total_cost'):
                region_final_output = region_output
        output.get('Output').append(region_final_output)

    return output
