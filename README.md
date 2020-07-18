# scraper

<p>Clone This Project</p>

<code>https://github.com/Starenesha/scraper.git</code>

<p>Install Dependencies</p>

<code>pip install -r requirements.txt</code>

<p>Set Database (Make Sure you are in directory same as manage.py)</p>

<code>python manage.py makemigrations
python manage.py migrate</code>

<p>Create SuperUser</p>

<code>python manage.py createsuperuser</code>

<p>To run scraper run this command (list of url from https://www.investing.com/search/?q=Manufacturing%20Purchasing%20Managers&tab=ec_event and value):
<code> python manage.py parse_series</code>
<code> python manage.py parse_value</code>


