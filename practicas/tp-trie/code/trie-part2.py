from trie import *


def withPrefix(T: Trie, prefix: str, size: int) -> list:
    """Returns a list with all words with -prefix- and length -size-."""

    def withPrefixR(node, size, finalList, remaining):
        if size == 0 and node.isEndOfWord:
            finalList.append(remaining)

        for child in node.children:
            withPrefixR(child, size - 1, finalList, remaining + child.key)  # decrease remaining while adding key
        return finalList  # return when loop finishes (all possible situations where verified)

    wordFound, lastLetterNode = searchWordLastLetterNode(T, prefix)
    if not wordFound or size <= 0 or size <= len(prefix):
        return []  # prefix not found or input errors

    remainingSize = size - len(prefix)  # so to see when it reaches zero
    return withPrefixR(lastLetterNode, remainingSize, [], prefix)


def sameDocument(T1: Trie, T2: Trie) -> bool:
    """Tells if T1 and T2 have all same words, iow, they are the same Trie.
    El costo es de O(m*n*log(n)), donde m es el número total de nodos y n es el número de hijos por cada nodo m.
    El costo n*log(n) se debe a que cada llamada aplica dos ordenamientos de listas."""

    def nodeKey(node):
        return node.key

    def sameDocumentR(node1, node2):
        if len(node1.children) != len(  # here are all the logical cases where a doc-node is considered != from another
                node2.children) or node1.key != node2.key or node1.isEndOfWord != node2.isEndOfWord:
            return False
        keySorted1 = sorted(node1.children, key=nodeKey)
        keySorted2 = sorted(node2.children, key=nodeKey)
        for i in range(len(keySorted1)):  # checks that all nodes satisfy sameDocument condition
            if not sameDocumentR(keySorted1[i], keySorted2[i]):  # only if a False condition is found, return
                return False
        return True  # else, continue up to here - all nodes and their children checked

    if T1 and T2:
        return sameDocumentR(T1.root, T2.root)
    return False


def hasReversedStrings(T):
    node = T.root
    stack = [(node, '')]
    while stack:  # while there is still a node to be searched
        node, word = stack.pop()  # bring back the last node
        if node.isEndOfWord and search(T, word[::-1]):  # when an EOW was found, search its reversed form
            return True
        for child in node.children:
            stack.append((child, word + child.key))  # append a node so to analyze it
    return False


if __name__ == "__main__":
    T = Trie()
    for palabra in ["dsa", "asd"]:
        insert(T, palabra)
    print(hasReversedStrings(T))
