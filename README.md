# kafka-python-project

# Set up an environment.
cd send_to_kafka
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

# Run the producer.
python3 main.py
