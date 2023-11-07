# Daily Image Fetcher

This is a Flask application that fetches an image from OpenAI's DALL-E API and displays it on a webpage.
The image is of a chubby daschund wearing a sailor hat on the beach, with the caption being today's date.

## Installation

Clone the repository and install the required packages:

```sh
git clone git@github.com:hart-venus/bachicha-daily.git 
cd bachicha-daily
pip install -r requirements.txt
```

## Usage
Set up the environment variable OPENAI_API_KEY to your OpenAI API key. You can get an API key from https://platform.openai.com/.
To run the application, use the following command:

```sh
python app.py
```

The application will start a server at http://localhost:5000/. Open this URL in a web browser to view the image.

## API Routes
- / - Displays the image fetched from the DALL-E API.
- /get-image - Fetches a new image from the DALL-E API.

## Contributing
Contributions are welcome. 

## License
MIT

## Future features
1. Image caching
2. Image Rating System
3. Custom prompts for server side (not just the daschund image)
4. Custom prompts each day algorithmically generated
5. Responsive design
6. Image history
7. Links to my social media