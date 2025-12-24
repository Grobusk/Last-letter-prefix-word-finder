from flask import Flask, render_template, jsonify, request
from prefix_finder import PrefixWordFinder

app = Flask(__name__)
finder = PrefixWordFinder()

# Load word lists on startup
word_files = ['dinos (1).txt', 'word.txt', 'words_alpha.txt']
print("Loading word lists...")
finder.load_from_files(word_files)
print(f"Loaded {finder.get_stats()['total_words']:,} words")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search')
def search():
    prefix = request.args.get('prefix', '').strip()
    sort_order = request.args.get('sort', 'none')
    suffixes_str = request.args.get('suffixes', '').strip()
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 100))
    
    if not prefix:
        return jsonify({'words': [], 'total': 0, 'page': 1, 'total_pages': 0})
    
    # Parse preferred suffixes (comma-separated)
    preferred_suffixes = None
    if suffixes_str:
        preferred_suffixes = [s.strip() for s in suffixes_str.split(',') if s.strip()]
    
    words = finder.find_words_with_prefix_sorted(prefix, sort_order, preferred_suffixes)
    total = len(words)
    total_pages = (total + per_page - 1) // per_page
    
    start = (page - 1) * per_page
    end = start + per_page
    page_words = words[start:end]
    
    return jsonify({
        'words': page_words,
        'total': total,
        'page': page,
        'total_pages': total_pages,
        'has_more': page < total_pages
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

