from logging import root
from pickle import FALSE
from re import X


def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    return [[i, fn(i)] for i in seq if (fn(i) <= upper and fn(i) >= lower)]
#region: Editor's Note:
# At first, my answer is:
#       return [[X, fn(X)] for X in seq if (fn(X) <= upper & fn(X) >= lower)]
# and it prints [[1, 1], [3, 9]] without [-2, 4], but why?
# 
# Firstly, the operator "&" is bitwise operator and "and" is logical operators. 
# In my previous training when the operands of "&" and "and" are boolean 
# varibles, there's almost no difference between them. But when the operands 
# are not 1&0 but other numbers, things will change:
#       x = 10 & 7 = 2    
# 10 is binary 1010, 7 is binary 0111, after binary AND operation, the result 
# is 0010, namely 2.
#       x = 10 and 7 = 7
# 
# Besides, the precedence of these two operators differs. The logical 
# comparison operators"<"and">" is prior to "and", but secondary to 
# bitwise AND "&". So in the given condition the outcomes of 
#       fn(X) <= upper and fn(X) >= lower
# and
#       fn(X) <= upper & fn(X) >= lower
# are different:
#
#      >>> print(4 <= 9 & 4 >= 1)
#     False
#     #9 & 4 = 0
#
#      >>> print(4 <= 9 and 4 >= 1)
#     True
# And that's why wrong function won't print [-2, 4]
#endregion 


def riffle(deck):
    """Produces a single, perfect riffle shuffle of DECK, consisting of
    DECK[0], DECK[M], DECK[1], DECK[M+1], ... where M is position of the
    second half of the deck.  Assume that len(DECK) is even.
    >>> riffle([3, 4, 5, 6])
    [3, 5, 4, 6]
    >>> riffle(range(20))
    [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]
    """
    "*** YOUR CODE HERE ***"
    return [deck[ i//2 + (i%2) * len(deck)//2 ] for i in range(len(deck))]


def berry_finder(t):
    """Returns True if t contains a node with the value 'berry' and 
    False otherwise.

    >>> scrat = tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
    >>> berry_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = tree(1, [tree('berry',[tree('not berry')])])
    >>> berry_finder(t)
    True
    """
    if label(t) == 'berry':
      return True
    else: 
      for i in branches(t):
        if berry_finder(i):
          return True
      return False


def sprout_leaves(t, leaves):
    """Sprout new leaves containing the data in leaves at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    if is_leaf(t):
      return tree( label(t), [tree(j) for j in leaves] )
    else:
      NewBranches = [sprout_leaves(i, leaves) for i in branches(t)]
      return tree( label(t), NewBranches )
#region: Editor's Note:
# Refer to the "Creating Trees Problems"(Page 16) in Lecture10.
#endregion


# Abstraction tests for sprout_leaves and berry_finder
def check_abstraction():
    """
    There's nothing for you to do for this function, it's just here for the extra doctest
    >>> change_abstraction(True)
    >>> scrat = tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
    >>> berry_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = tree(1, [tree('berry',[tree('not berry')])])
    >>> berry_finder(t)
    True
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    >>> change_abstraction(False)
    """


def add_trees(t1, t2):
    """
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(add_trees(numbers, numbers))
    2
      4
        6
        8
      10
        12
          14
        16
    >>> print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
    5
      4
      5
    >>> print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
    4
      6
      4
    >>> print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]), \
    tree(2, [tree(3, [tree(4)]), tree(5)])))
    4
      6
        8
        5
      5
    """
      
    NewLabel = label(t1)+label(t2)
    if is_leaf(t1) and is_leaf(t2): #two leaves
      return tree(NewLabel)
    if is_leaf(t1) and not is_leaf(t2): #only tree2 has branches
      return tree(NewLabel, branches(t2))
    if is_leaf(t2) and not is_leaf(t1): #only tree1 has branches
      return tree(NewLabel, branches(t1))
    
    #tree1 and tree2 both have branches:
    
    branchlen1 = len( branches(t1) )
    branchlen2 = len( branches(t2) )
    if branchlen1 < branchlen2:
      newbranch1 = branches(t1) + [[0]]* (branchlen2 - branchlen1)
      newbranch2 = branches(t2)
    else:
      newbranch1 = branches(t1)
      newbranch2 = branches(t2) + [[0]]* (branchlen1 - branchlen2)
    return tree(NewLabel, [add_trees(i[0], i[1]) for i in list(zip( newbranch1, newbranch2 ))])
#region: Editor's Note:
# 
# 1. Recursion Strategy:
# 1) base case: leave1 + leave2; leave1(No leave2); leave2(No leave1)
# 2) recursive step: 
#     Firstly, the arguments passed into Function "add_trees" in recursion are 2 trees.
#   so it needs to return a tree data structure to complete the recursion.
#     The new root node is easy. About branches, if they're not in the same length, we 
#   need to make uo the difference at the beginning. After that, use zip function to 
#   iterate over the same-length branches, and recursively pass every tuple ([],[]) 
#   into Function "add_trees". 
# 
# 2. Some key points in coding:
# 1) We wanna add an list[ [0], [0], [0], ... ], so notice the double brackets.If 
#   there's a single bracket, it will be [0, 0, ...] 
#         newbranch1 = branches(t1) + [[0]]* (branchlen2 - branchlen1)
#    also true if [[0]] replaced by [[None]].
# 2) The final return is:
#         return tree(NewLabel, [add_trees(i[0], i[1]) for i in list(zip( newbranch1, newbranch2 ))])
#    i is a tuple here.
#    also true like this:
#         ... [add_trees(i,j) for i,j in zip( newbranch1, newbranch2 )]...
#    but notice that 'zip' object is not callable
#endregion


def build_successors_table(tokens):
    """Return a dictionary: keys are words; values are lists of successors.

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = [word]
        else:
            table[prev].append(word)
        prev = word
    return table

def construct_sent(word, table):
    """Prints a random sentence starting with word, sampling from
    table.

    >>> table = {'Wow': ['!'], 'Sentences': ['are'], 'are': ['cool'], 'cool': ['.']}
    >>> construct_sent('Wow', table)
    'Wow!'
    >>> construct_sent('Sentences', table)
    'Sentences are cool.'
    """
    import random
    result = ''
    while word not in ['.', '!', '?']:
        
        result = result + word + ' '
        nextword = random.choice(table[word])
        word = nextword

    return result.strip() + word

def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

# Uncomment the following two lines
# tokens = shakespeare_tokens()
# table = build_successors_table(tokens)

def random_sent():
    import random
    return construct_sent(random.choice(table['.']), table)



# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def change_abstraction(change):
    change_abstraction.changed = change

change_abstraction.changed = False


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

