import pprint

nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'g', 'h'],
	[1, 2, None],
]

def FlatGenerator(nested_lister):
    list_cursor = 0
    element_cursor = 0
    lists_ind = len(nested_lister[-1])-1
    curr_list_ind = len(nested_lister[list_cursor])-1

    yield "--START---"
    while element_cursor < curr_list_ind and list_cursor <= lists_ind:
        yield nested_lister[list_cursor][element_cursor]
        element_cursor +=1
        curr_list_ind = len(nested_lister[list_cursor]) - 1
        if element_cursor == curr_list_ind and list_cursor <= lists_ind:
            yield nested_lister[list_cursor][element_cursor]
            list_cursor +=1
            element_cursor=0
    yield "---END---"



for item in FlatGenerator(nested_list):
	print(item)