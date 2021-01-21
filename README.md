# Django-React
A starter Django project with React framework for frontend

### Build frontend
```bash
cd frontend
nvm use 12
npm run build
cd build
mv *.ico *.js *.json root
````

### Activate virtualenv and start server

```bash
cd backend
source source/Scripts/activate
python manage.py collectstatic --no-input
python manage.py runserver

```

### Deploy frontend for dev
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
