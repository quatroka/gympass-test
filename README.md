# Gympass Test

This project uses Python 3.7+

## Run test

    python main.py
    
or

    docker run --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python main.py

### Propositions used in this test

1. Not have driver with duplicate ID
1. Drivers started the race in the same time and the same distance from start 
