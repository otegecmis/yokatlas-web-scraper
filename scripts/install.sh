#!/bin/bash

virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
deactivate

echo -e "\nDependencies installed and virtual environment setup completed."
