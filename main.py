import requests
from quixstreams import Application
import json
import logging
import time

def get_weather_info():
 response=requests.get("https://api.open-meteo.com/v1/forecast",params={"latitude":51.5 ,"longitude":-0.11 ,"current":"temperature_2m"})
 return response.json()

def main():
 app=Application(
 broker_address="localhost:9092",
 loglevel="DEBUG",
 )

 with app.get_producer() as producer:
  while True:
   weather=get_weather_info()
   logging.debug("Got Weather: %s",weather)
   producer.produce(topic="weather_data_info",key="London",value=json.dumps(weather),)
   logging.info("Produced Sleeping...")
   time.sleep(10)
if __name__=="__main__":
 logging.basicConfig(level="DEBUG")
 main()
