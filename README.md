# Django-React
A starter Django project with React framework for frontend

### Build frontend for production
```bash
cd frontend
nvm use 12
npm run build
cd build
mkdir root
mv *.ico *.js *.json root
````

### Activate virtualenv and start backend server
The React frontend will be served from Django after building it

```bash
cd backend
source ~/django-env/bin/activate
python manage.py collectstatic --no-input
python manage.py runserver
```

### Deploy site to elastic beanstalk
```bash
cd backend
eb deploy
```

### Deploy frontend for development
```bash
cd frontend
unset HOST
nvm use 12
npm start
````

## Sources

Frontend UI Kit:  
https://www.creative-tim.com/product/now-ui-kit-react  

Method for connecting frontend and backend:  
https://fractalideas.com/blog/making-react-and-django-play-well-together-hybrid-app-model/

How to deploy to aws EC2
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html
