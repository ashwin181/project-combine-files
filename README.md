# csv-combiner python code

## Instructions

- Pre requisites: 
   - python should be installed in the system
   - ```pip``` manager should be installed in python

- There is a file called requirements.txt
  - run the command ```pip install -r requirements.txt```
  - This will install pandas and other dependencies for the project

- Run the python code with the following command
```yaml
python ./combineCSV.py ./fixtures/accessories.csv ./fixtures/clothing.csv ./fixtures/household_cleaners.csv combined-results.csv
```

### Unit Testing

To run the unit test, type the following command
```
python ./combineCSV-test.py
