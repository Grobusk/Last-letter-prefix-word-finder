import random

class TrieNode:
    """Node in a Trie data structure for fast prefix matching."""
    __slots__ = ['children', 'is_end_of_word']  # Reduces memory overhead
    
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class PrefixWordFinder:
    """Fast prefix word finder using Trie data structure."""
    
    def __init__(self):
        self.root = TrieNode()
        self.word_count = 0
    
    def insert(self, word):
        """Insert a word into the Trie."""
        node = self.root
        word_lower = word.lower().strip()
        
        if not word_lower:
            return
        
        for char in word_lower:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
        self.word_count += 1
    
    def find_words_with_prefix(self, prefix):
        """Find all words that start with the given prefix."""
        prefix_lower = prefix.lower().strip()
        node = self.root
        
        # Navigate to the prefix node
        for char in prefix_lower:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # Collect all words with this prefix
        words = []
        self._collect_words(node, prefix_lower, words)
        return words
    
    def _collect_words(self, node, prefix, words):
        """Recursively collect all words from a node."""
        if node.is_end_of_word:
            words.append(prefix)  # Reconstruct word from prefix
        
        for char, child_node in node.children.items():
            self._collect_words(child_node, prefix + char, words)
    
    def load_from_file(self, filename):
        """Load words from a text file (one word per line)."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    word = line.strip()
                    if word:
                        self.insert(word)
        except FileNotFoundError:
            print(f"Warning: File '{filename}' not found.")
        except Exception as e:
            print(f"Error loading '{filename}': {e}")
    
    def load_from_files(self, filenames):
        """Load words from multiple files."""
        for filename in filenames:
            self.load_from_file(filename)
    
    def get_stats(self):
        """Get statistics about loaded words."""
        return {
            'total_words': self.word_count,
            'unique_prefixes': len(self.root.children)
        }
    
    def find_words_with_prefix_sorted(self, prefix, sort_order='none', preferred_suffixes=None):
        """Find words with prefix and optionally sort them.
        
        Args:
            prefix: The prefix to search for
            sort_order: 'longest' to sort by longest first, 'shortest' to sort by shortest first, 
                       'random' for random order, 'none' for alphabetical (default)
            preferred_suffixes: List of suffixes to prioritize (words with these suffixes appear first)
        """
        words = self.find_words_with_prefix(prefix)
        
        # Normalize preferred suffixes
        if preferred_suffixes:
            preferred_suffixes = [s.lower().strip() for s in preferred_suffixes if s.strip()]
        
        # Separate words into groups based on suffix priority (order matters)
        suffix_groups = []
        other_words = []
        
        if preferred_suffixes:
            # Create a group for each suffix in order
            for suffix in preferred_suffixes:
                suffix_groups.append([])
            
            # Assign each word to the first matching suffix group
            for word in words:
                word_lower = word.lower()
                assigned = False
                for i, suffix in enumerate(preferred_suffixes):
                    if word_lower.endswith(suffix):
                        suffix_groups[i].append(word)
                        assigned = True
                        break
                if not assigned:
                    other_words.append(word)
        else:
            other_words = words
        
        # Apply sorting to each group
        if sort_order == 'longest':
            for group in suffix_groups:
                group.sort(key=lambda x: (-len(x), x))
            other_words.sort(key=lambda x: (-len(x), x))
        elif sort_order == 'shortest':
            for group in suffix_groups:
                group.sort(key=lambda x: (len(x), x))
            other_words.sort(key=lambda x: (len(x), x))
        elif sort_order == 'random':
            for group in suffix_groups:
                random.shuffle(group)
            random.shuffle(other_words)
        # For 'none' (alphabetical), words are already in alphabetical order from Trie
        
        # Combine: suffix groups in order, then others
        result = []
        for group in suffix_groups:
            result.extend(group)
        result.extend(other_words)
        return result
