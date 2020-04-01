Problem Summary

Oh no! Commander Lambda's latest experiment to improve the efficiency of her LAMBCHOP doomsday device has backfired spectacularly. She had been improving the structure of the ion flux converter tree, but something went terribly wrong and the flux chains exploded. Some of the ion flux converters survived the explosion intact, but others had their position labels blasted off. She's having her henchmen rebuild the ion flux converter tree by hand, but you think you can do it much more quickly - quickly enough, perhaps, to earn a promotion!

Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one. To label them, she performed a post-order traversal of the tree of converters and labeled each converter with the order of that converter in the traversal, starting at 1. For example, a tree of 7 converters would look like the following:

      7
    /   \
  3      6
 /  \   / \
1   2  4   5

Write a function answer(h, q) - where h is the height of the perfect tree of converters and q is a list of positive integers representing different flux converters - which returns a list of integers p where each element in p is the label of the converter that sits on top of the respective converter in q, or -1 if there is no such converter. For example, answer(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7 in a perfect binary tree of height 3, which is [3, 6, -1].

The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root, h = 2 represents a perfect binary tree with the root and two leaf nodes, h = 3 represents a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above), and so forth. The lists q and p contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.

Solution Discussion

The key phrase in this problem is "postorder traversal". Let's take another look at that tree.

       7
     /   \
   3      6
  /  \   / \
 1   2  4   5
There are a few useful properties.

The label on the top node of the tree is equal to the number of nodes in the tree.
For a tree of height h, the total number of nodes in the tree is 2^h - 1.
Each subtree has ((n-1)/2) nodes in it, where n is the number of nodes in the tree.
There is no node in the tree with a number greater than the top node in the tree.
In order to find the solution, I'll need to do a postorder traversal search of this binary tree. Essentialy, at each step of the traversal, I need to check the left and right children of a given node, and if either of them match the input, return the calculated value. Complicating matters a bit is the stipulation that my input array can have up to 10,000 distinct integers in it (yikes!). This means that I can't build this datastructure. So, starting at the top of the tree, I have to answer the following questions:

What is the value of my left child?
What is the value of my right child?
Which branch do I need to continue my search using?
If one of my children is a match, how do I determine my own value?
Predicting the left child
This one's pretty straightforward. If I know that the top node in a tree has a label equal to the number of nodes in the tree, and I know that each subtree has ((n - 1)/2) nodes in it, I can know that the left child of the top node will be labeled ((n-1)/2).

Sweet! We're partway there.

Predicting the right child
Unfortunately, the right child is a little more involved. It's going to require us to examine the postorder traversal. Now, as a reminder, postorder traversal works like so.

function post_order_traversal(node) {
    post_order(node.left)
    post_order(node.right)
    visit(node)
}
For every node, we traverse the left subtree, then the right subtree, then we label then node itself. Following this algorithm, it's easy to see that the leftmost node in the tree gets visited first. Starting at the node, we visit its left child, and then we visit that node's left child. Since there are no more children to visit, we label that node "1" and move back to the parent. Then, we visit the right child, and similarly find no children below it, and label that node "2". Finally, we end up at the parent of the now-labeled "1" and "2", and label it "3".

It should follow logically that we'll repeat this same process for the right subtree of this tree, and then finally label the top node in the tree "7". We should note that we traverse nodes in exactly the same order for both subtrees. That's important, because it means that, given what the left subtree looks like, we can predict what the right subtree looks like.

Here's the left subtree from the previous example.

   3   
  /  \ 
 1    2  
There are 3 nodes in this tree. Now, if I add 3 to each label in this tree, I get this:

   6   
  /  \ 
 4    5  
Which happens to be my right subtree! Intuitively, this makes sense because in order to count these nodes, I have to first count all the nodes in the left subtree. Because I know that I traverse nodes in the exact same order, I know that I'll traverse the top node last. So, I know that for a given top node, I know that the right child will have a value equal to the left child plus the number of nodes in its subtree (including itself).

You can prove this to yourself by looking at any pair of siblings in the tree above. The leaf nodes all have a subtree of 1 node, so you can see that 1 and 2 and 4 and 5 both differ by 1. Similarly, 3 and 6 both have subtrees of size 3, so they differ by 3.

Groovy! But in order to apply this recursively, I need to figure out which subtree to set as my new tree when I'm traversing.

Picking the branch to search down
Because we always visit the top node last, we know that it will always get labeled last. That means for a given subtree, there will be no element in the subtree with a label greater than that of the top node. So, if we're searching for a specific index, we need only check the value against the left child. If the value we're looking for is less than the left child, we proceed down using the left child as the new top node. Otherwise, we use the right child.

Determining my own value
Looking at the tree above, every right child has a label exactly 1 smaller than its parent. This is no accident. It happens because in postorder, the right child gets visited just before the parent does. That means if either my left or right child is a match, the parent will have a label equal to 1 plus the right child.