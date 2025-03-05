### Disclaimer: This is a project created as part of the interview process. Feel free to use any components other than the logo(which is a property of Kema).


There are three folders in the repo

How to run
## * backend

Have python 3 and pip installed on the machine. 
1. run "`cd backend`"
2. `python manage.py migrate`
3. `python manage.py runserver`
4. You can see the application is running on port 8000. `http://127.0.0.1:8000/`

   Note: PostgreSQL is running on post 5433 rather than the default 5432. Make sure to configure the same in backend/settings.py

   If interested use docker for lauching the ProstgreSQL by

  ``` 
   docker run -d \
  --name postgres-container \
  -e POSTGRES_PASSWORD=your_password \
  -e POSTGRES_USER=your_db_user \
  -e POSTGRES_DB=your_db_name \
  -p 5433:5432 \
  postgres:latest 
  ```

## * frontend - Merchant App

Install node v18 or more and vue cli
1. run `"cd frontend"`
2. `npm install`
3. `npm run serve`
4. Application will be live at `http://localhost:8080/`

## * frontend - Customer

Install vuetify UI library
1. run "`cd customer-frontend`"
2. `npm install`
3. `npm run dev`
4. Application will be live at `http://localhost:3000/`


### Entity Relationship Diagram

![Image](https://github.com/Vishnuraj910/django-vue-stack/blob/main/task_assets/Kema-ERD.drawio.png)



### Merchant App Screen

![Screenshot](https://github.com/Vishnuraj910/django-vue-stack/blob/develop/task_assets/customer.png)


### Customer App Screen

![Screenshot](https://github.com/Vishnuraj910/django-vue-stack/blob/develop/task_assets/merchant.png)







