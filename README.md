# Reviews microservice for Carpool app API server
This django project is a project for the course M7011E at LTU (Sweden). It is a part of a larger project,
the rest can be found [here](https://github.com/AceBasket/carpool)

## Set up
1. Create a virtual environment:
   ```
   python3 -m venv .env
   ```
2. Activate the virtual environment:
   1. For linux
    ```
    source .env/bin/activate
    ```
    2. For Windows
    ```
    .env/Scripts/Activate.bat
    ```
3. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
4. Migrate:
   ```
   python manage.py migrate
   ```

## Run project
In one terminal, run:
   ```
   python manage.py runserver 8001
   ```

You can find the documentation at [localhost:8001/api/v1/schema/swagger-ui](localhost:8001/api/v1/schema/swagger-ui)

Open a second terminal and run:
    
    python consumer.py
    