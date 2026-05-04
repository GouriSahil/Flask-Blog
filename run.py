import os
from flaskblog import app

if __name__ == '__main__':
    # Default 5001: macOS often reserves 5000 for AirPlay Receiver.
    port = int(os.environ.get('PORT', 5001))
    # Templates still reload from disk (see TEMPLATES_AUTO_RELOAD in flaskblog/__init__.py).
    # Set FLASK_DEBUG=1 for the code reloader during development.
    debug = os.environ.get('FLASK_DEBUG', '').strip().lower() in ('1', 'true', 'yes')
    app.run(host='0.0.0.0', port=port, debug=debug, use_reloader=debug)

