"""Quick test script to verify the prefix finder works correctly."""
from prefix_finder import PrefixWordFinder

def test_prefix_finder():
    """Test the prefix finder functionality."""
    finder = PrefixWordFinder()
    
    # Load all word lists
    word_files = ['dinos (1).txt', 'word.txt', 'words_alpha.txt']
    print("Loading word lists...")
    finder.load_from_files(word_files)
    
    stats = finder.get_stats()
    print(f"Loaded {stats['total_words']:,} words\n")
    
    # Test 1: Simple prefix search
    print("Test 1: Finding words starting with 'saur'")
    words = finder.find_words_with_prefix('saur')
    print(f"Found {len(words)} words")
    if words:
        print(f"Examples: {words[:5]}")
    print()
    
    # Test 2: Single letter search
    print("Test 2: Finding words starting with 'x'")
    words = finder.find_words_with_prefix('x')
    print(f"Found {len(words)} words")
    if words:
        print(f"Examples: {words[:5]}")
    print()
    
    # Test 3: Last Letter game helper
    print("Test 3: Last Letter game - finding words starting with last letter of 'dinosaur'")
    words = finder.get_last_letter_words('dinosaur')
    print(f"Last letter of 'dinosaur' is 'r'")
    print(f"Found {len(words)} words starting with 'r'")
    if words:
        print(f"Examples: {words[:5]}")
    print()
    
    # Test 4: Long prefix
    print("Test 4: Finding words starting with 'pneumono'")
    words = finder.find_words_with_prefix('pneumono')
    print(f"Found {len(words)} words")
    if words:
        print(f"Examples: {words[:5]}")
    print()
    
    print("All tests completed!")

if __name__ == "__main__":
    test_prefix_finder()

