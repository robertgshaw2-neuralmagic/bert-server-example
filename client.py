import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--sentence", type=str, default="Sending requests to deepsparse is super easy")

if __name__ == "__main__":
    args = parser.parse_args()
    
    # model running here
    url = 'http://0.0.0.0:5543/v2/models/sentiment-analysis-0/infer'

    # send the data
    obj = {"sequences": args.sentence}
    resp = requests.post(url=url, json=obj)

    # recieve the post-processed output
    print(resp.text)