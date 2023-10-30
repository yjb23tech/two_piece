from data_structures import dict_action_horiz_vector_options, dict_action_vertical_vector_options

print(" ")
for k in dict_action_horiz_vector_options:
    for v in dict_action_horiz_vector_options[k]:
        print(f"[{k},{v}]")
        print(dict_action_horiz_vector_options[k][v])
    print(" ")

print(" ")
for k in dict_action_vertical_vector_options:
    for v in dict_action_vertical_vector_options[k]:
        print(f"[{k}, {v}]")
        print(dict_action_vertical_vector_options[k][v])
        print(" ")














