import logging
import unit_test_python
from unit_test_python.app import app
if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5640, debug=True, threaded=True)