import argparse, sys
from app.app import App

def main():
    parser = argparse.ArgumentParser(description="A script to process web scraping to get universities and degrees information.")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--get', choices=['universities', 'degrees'], help="Specify the process to execute: 'universities' or 'degrees'.")
    group.add_argument('--tools', choices=['reset', 'clean'], help="Specify the tool to use: 'reset' or 'clean'.")
    
    if len([arg for arg in sys.argv if arg.startswith('--get')]) > 1 or \
       len([arg for arg in sys.argv if arg.startswith('--tools')]) > 1:
        parser.error("Multiple --get or --tools arguments are not allowed.")
    
    args = parser.parse_args()

    app = App()
    
    if args.get:
        if args.get == 'universities':
            app.universities()
        elif args.get == 'degrees':
            app.degrees()
    elif args.tools:
        if args.tools == 'reset':
            app.reset()
        elif args.tools == 'clean':
            app.clean()

if __name__ == '__main__':
    main()
