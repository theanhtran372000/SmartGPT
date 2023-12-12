# Libs
import os
import yaml
import openai
import pprint
import argparse

from loguru import logger
from flask import Flask, request, make_response
from flask_cors import CORS


# Flask app
app = Flask(__name__)
cors = CORS(app) # Enable CORS
app.config['CORS_HEADERS'] = 'Content-Type'


# Preflight requests
@app.before_request
def before_request():
    
    # If the request method is OPTIONS (a preflight request)
    if request.method == 'OPTIONS':
        
        # Create a 200 response and add the necessary headers
        response = make_response('OK')
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', '*')
        response.headers.add('Access-Control-Allow-Methods', '*')
        
        # Return the response
        return response

# Ping route
@app.route('/ping', methods=['GET'])
def ping():
    return 'Hello World!'


# CLI Parser
def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='configs.yml', help='Path to config file')
    return parser


# Main function
def main():
    # Parse args
    parser = get_parser()
    args = parser.parse_args()
    logger.info('Configs file: {}'.format(args.config))
    
    # Load configs file
    with open(args.config, 'r') as f:
        configs = yaml.safe_load(f)
    logger.info('Configs: \n{}'.format(pprint.pformat(configs)))

    # Create dir
    os.makedirs(configs['app']['save_dir'], exist_ok=True)
    logger.info('All temporary files will be saved at {}'.format(
        configs['app']['save_dir']
    ))
    
    # Config OpenAI Key
    with open(configs['openai']['keypath'], 'r') as f:
        API_KEY = f.read().strip()
    openai.api_key = API_KEY
    
    # Start app
    logger.info('Server is listening at port {}...'.format(configs['app']['port']))
    app.run(host=configs['app']['host'], port=configs['app']['port'], threaded=configs['app']['multithread'])
    
    
if __name__ == '__main__':
    main()