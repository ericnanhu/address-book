# Installation

The backend uses Python and Django.

First, create a virtual environment.

```
cd backend
python3 venv env
source env/bin/activate
```

Install required packages.

```
pip install -r requirements.txt
```

Run migrations.

```
python manage.py makemigrations
python manage.py migrate
```

Start dev server.

```
python manage.py runserver
```

For the frontend (uses Vue.js), install packages.

```
cd frontend
npm install
```

Start frontend dev server.

```
npm run dev
```

# Screenshots
![Home Page](https://github.dev/ericnanhu/address-book/blob/1fa7327416bd76578f45a7b2d143cef9ef6c9914/screenshots/Screen%20Shot%202022-02-24%20at%203.18.28%20PM.png?raw=true)

