import time
from datetime import timedelta

def check_time(elapsed):
    return str(timedelta(seconds=elapsed))

# decorator to trace execution of recursive function
# https://www.codementor.io/@dmitrybelaventsev/python-trace-recursive-function-tkq79m4so
def trace(func):

    # time1 = time.time()

    # cache func name, which will be used for trace print
    func_name = func.__name__
    # define the separator, which will indicate current recursion level (repeated N times)
    separator = '|   '

    # current recursion depth
    trace.recursion_depth = 0

    from functools import wraps
    @wraps(func)
    def traced_func(*args, **kwargs):

        # repeat separator N times (where N is recursion depth)
        # `map(str, args)` prepares the iterable with str representation of positional arguments
        # `", ".join(map(str, args))` will generate comma-separated list of positional arguments
        # `"x"*5` will print `"xxxxx"` - so we can use multiplication operator to repeat separator
        print(f'{separator * trace.recursion_depth}├-- {func_name}({", ".join(map(str, args))})')
        # we're diving in
        trace.recursion_depth += 1
        result = func(*args, **kwargs)
        # going out of that level of recursion
        trace.recursion_depth -= 1
        # result is printed on the next level
        print(f'{separator * (trace.recursion_depth + 1)}└-- return {result} (input: {", ".join(map(str, args))})')

        return result

    # time2 = time.time()
    # elapsed = time2 - time1
    # print('\nFunction took {} s'.format( check_time(elapsed)))
    return traced_func

def metatest(class_func=False):
    def decorator(f):
        def wrap(*args, **kwargs):
            print('=' * 64)
            print('Function: {:s}'.format(f.__name__))
            
            time1 = time.time()
            res = f(*args, **kwargs)
            time2 = time.time()
            elapsed = time2 - time1

            param_index = 1 if class_func else 0 
            print('\nInput:  {} '.format(','.join([str(i) for i in args[param_index:]])))
            print('Output: {} {}'.format(res, ','.join([str(i) for i in args[param_index:]])))
            print('Function took {} s'.format( check_time(elapsed)))
            return elapsed, res
        return wrap
    return decorator   
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        li_res = []
        node_cur = self
        for i in range(10):
            if node_cur is not None:
                li_res.append(str(node_cur.val))
                node_cur = node_cur.next
            else:
                break
        if node_cur is not None:
            li_res.append('...')
        return "({}) in {}".format(self.val, '->'.join(li_res))

def createList(li):
    if list is None:
        return None
    Li_res = node_cur = ListNode(0)
    for i in range(len(li)):
        if i == 0:
            node_cur.val = li[i]
        else:
            node_cur.next = ListNode(li[i])
            node_cur = node_cur.next
    return Li_res

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return str(self.val)

def createTree(li_treeNode):
    length = len(li_treeNode)
    if length == 0:
        return None
    else:
        li_treeNode2 = [TreeNode(val) if val is not None else None for val in li_treeNode]
        for i in range(length):
            if li_treeNode2[i] is None:
                continue
            if 2*i+1 < length and li_treeNode2[2*i+1] is not None:
                li_treeNode2[i].left = li_treeNode2[2*i+1]
            if 2*i+2 < length and li_treeNode2[2*i+2] is not None:
                li_treeNode2[i].right = li_treeNode2[2*i+2]
        
        return li_treeNode2[0]

def printTree(treeNode):
    # reference: MIT Introduction to Algorithm
    # https: // ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/readings/binary-search-trees/
    if treeNode is None:
        print('<empty tree>')

    def recurse(node):
        #                               pos                          ...1...
        #           |--------------------|                          /       \
        #             left_pos                      right_pos            ....46...
        #           |-----|                       |-----|               /         \
        #                 |---------  middle  ----------|              9.       ...48..
        # ------------------------------------------------------      /  \     /       \
        # 1st line: |'\s*'|            label            |'\s*' |     5    30  46       78
        # 2nd line: |'\s*'| /          '\s*'          \ |'\s*' |     /\  / \  /\      /  \
        #   ...     |           |                 |            |        18 38        76   78
        # nth line: | left_line |      '\s*'      | right_line |        /\ /\       /  \ / \
        #   ...     |           |                 |            |                   69       81
        # ------------------------------------------------------                  /  \     / \
        #           |left_width |                 |right_width |                 62  75   78 89
        #           |---------------   width   ----------------|                 /\  /\   /\ /\
        #                                                                           69        94
        #                                                                           /\        /\
        """ Recusive Call """
        if node is None:
            return [], 0, 0

        left_lines, left_pos, left_width = recurse(node.left)
        right_lines, right_pos, right_width = recurse(node.right)

        """ Add a new line to left_lines, right_lines """
        #           left_lines                 right_lines
        #     [                           [
        #       '    <space>    ',          '     <space>    ',
        #       '    <space>    ',          '     <space>    ',
        #              ...       ,                  ...       ,
        #  +++  '    <space>    '      +++  '     <space>    '
        #     ]                           ]
        #        |- left_width -|            |- right_width -|
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)

        label = str(node)
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)

        """ Padding the label(the string of node.val) with '.'s """
        # If node is the parent's left child, add one more '.' to the right,
        # so taht the node is closer the parent side
        # if (middle - len(label)) % 2 == 1 and node.parent is not None and \
        #     node is node.parent.left and len(label) < middle:
        #     label += '.'

        #        |-- middle --|
        # label [...node_val...]
        label = label.center(middle, '.')

        # label [ ..node_val.. ]
        if label[0] == '.':
            label = ' ' + label[1:]
        if label[-1] == '.':
            label = label[:-1] + ' '

        """ Caculate return results: lines, pos & width """
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),                         # 1st line
                 ' ' * left_pos + '/' + ' ' * (middle-2) + '\\' + ' ' * (right_width - right_pos)  # 2nd line
                    ] + \
                [left_line + ' ' * (width - left_width - right_width) + right_line                 # nth line
                    for left_line, right_line in zip(left_lines, right_lines)
                ]

        return lines, pos, width

    print('\n'.join(recurse(treeNode)[0]))

if __name__ == '__main__':
    @trace
    def factorial(n):
        if n == 1: return 1
        else: return n * factorial(n-1)

    # this will print all the recursion trace and the result at the bottom
    print(factorial(7))