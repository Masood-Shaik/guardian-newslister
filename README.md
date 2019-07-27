# guardian-newslister
Django App to Search for a keyword invoke Guardian API with test api key, display results

Configuration

Create a virtual environment and install all the package inside requirememt.txt file as shown below, to run the project.

pip install -r requirements.txt

Once setup is done, use python3

python3 manage.py runserver

The server starts to listen on port 8000

Open a web browser and paste the url http://localhost:8000, this renders the initial web page with search textbox
Enter the search keyword and click on the Search Button

This will return the results for the search string using Gurdian API in the backend and display the result in the form of a list,
with the headlines,thumbnails and tags(keywords).