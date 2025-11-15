


## Clone the repo

```
git clone https://github.com/majay777/ajay_maruti_mugale.git
```

✏️ Note: Run Following commands from directory where docker-compose.initial.yml and Dockerfile are there.

**Start the MySQL database in Docker:**

```
docker-compose -f docker-compose.initial.yml up --build -d
```

**Create docker network mynet**
```
docker network create mynet 
```

**Add Sql database to above created network**
```
docker network connect mynet mysql_ctn
```

**Build the Python Environment for running python scripts**
```
docker build -t python_etl .   
```

**Run the python scripts for loading data from json to sql database**
```
docker run --name etl_app --network mynet python_etl
```
