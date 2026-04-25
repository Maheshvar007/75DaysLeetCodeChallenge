class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        node = self.trie
        for ch in word:
            node = node.setdefault(ch, {})
        node['#'] = True   # end marker

    def search(self, word):
        def dfs(i, node):
            if i == len(word):
                return '#' in node           
            ch = word[i]
            if ch == '.':
                for child in node:
                    if child != '#' and dfs(i+1, node[child]):
                        return True
                return False
            else:
                if ch not in node:
                    return False
                return dfs(i+1, node[ch])
        return dfs(0, self.trie)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)