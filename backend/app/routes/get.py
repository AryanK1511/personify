from app import app
from app.services.ai import get_gemini_response
from app.services.scraper import scrape_website
from app.utils.response import create_error_response, create_success_response
from flask import jsonify, request


@app.route('/api/profiles', methods=['GET'])
def scrape_url():
    try:
        data = request.get_json()

        if not data or 'url' not in data:
            return jsonify(
                create_error_response(
                    400, 'URL is required in the request body'
                )
            ), 400

        url = data.get('url')

        scraped_data = scrape_website(url)

        if scraped_data is None:
            return jsonify(
                create_error_response(
                    500, 'Failed to scrape the website content'
                )
            ), 500

        try:
            gemini_response = get_gemini_response(scraped_data)
            if gemini_response is None:
                return jsonify(
                    create_error_response(
                        500,
                        'Failed to get a response from the Gemini AI model',
                    )
                ), 500
        except Exception as gemini_error:
            return jsonify(
                create_error_response(
                    500, f'Error with Gemini AI model: {str(gemini_error)}'
                )
            ), 500

        # Return both scraped data and Gemini AI response as a success response
        return jsonify(
            create_success_response(
                {
                    'profiles': gemini_response['response']['profiles'],
                }
            )
        ), 200

    except Exception as e:
        return jsonify(
            create_error_response(
                500, f'An unexpected error occurred: {str(e)}'
            )
        ), 500
