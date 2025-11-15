# Solution

- **schema.sql (inside sql/ directory) creates the required tables in the database**
- **This sql file schema.sql is run by the read.py and sql tables are crated.**
- **The load_data.py, read's the json file  using pandas and the required table's created using the dataframe and loaded to database using sqlalchemy**

***

# Steps To Follow


## Clone the repo

```
git clone https://github.com/majay777/ajay_maruti_mugale.git
cd ajay_maruti_mugale
```


**Start the MySQL database in Docker:**

```
docker-compose -f docker-compose.initial.yml up --build -d
```
Runs MySQL database on port 3306, stop local MySQL before running above command/Free the 3306 port.

**Create docker network mynet**
```
docker network create mynet 
```

**Connect the MySQL Container to the Network**
```
docker network connect mynet mysql_ctn
```

**Build the Python Environment/Container.**
```
docker build -t python_etl .   
```
It copies all the scripts and sql file and also data to the docker enviroment.
Install's all required libraries mentioned in requirements.txt.

**Run the python scripts for loading data from json to sql database and also to create the tables in database.**
```
docker run --name etl_app --network mynet python_etl
```
Runs the read.py creating tables and load_data.py loading json data to tables.