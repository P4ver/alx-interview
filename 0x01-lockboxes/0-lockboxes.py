#!/usr/bin/python3
'''A module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    total_boxes = len(boxes)
    unlocked_boxes = set([0])
    keys_to_use = set(boxes[0]).difference(set([0]))

    while len(keys_to_use) > 0:
        current_key = keys_to_use.pop()
        if not current_key or current_key >= total_boxes or current_key < 0:
            continue
        if current_key not in unlocked_boxes:
            keys_to_use = keys_to_use.union(boxes[current_key])
            unlocked_boxes.add(current_key)

    return total_boxes == len(unlocked_boxes)
