import configparser
import argparse

"""Main module."""

def parse_args():
    """Parse command line arguments given to the agent"""
    parser = argparse.ArgumentParser(description="Ocean Agent Application")
    parser.add_argument('--config', metavar='path', required=True,
                        help='path to the agent.ini file')

    args = parser.parse_args()

def parse_config(file_path):
    """Loads the configuration file given as parameter"""
    pass

def start_agent(config):
    """This function initialize the Ocean Agent"""
    pass

def print_help():
    """Print the default help in stdout"""
    pass

if __name__ == "__main__":
    args = parse_args()
    config = parse_config(args.config)
    agent = start_agent(config)

