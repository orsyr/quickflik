To use the project download or clone git repository into a new folder
Open terminal and cd into new folder
Create a virtual environment in terminal using: python3 -m venv myvirtualenv/quickflik
Activate virtual environment in terminal using: source mymyvirtualenv/quickflik/bin/activate
cd into quickflikscraper directory
Install required dependencies using: pip install -r requirements.txt
Migrate admin models using: python manage.py migrate 
Create super user to access django admin page using: python manage.py createsuperuser
Run the server using: python manage.py runserver
Visit localhost:8000 on your browser
