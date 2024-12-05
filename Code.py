!pip install openai
import openai
openai.api_key = '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'

import requests

def fetch_website_source(url):
    """Fetch the HTML content of the website by emulating a Chrome browser"""
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    
    try:
        # Send request with custom headers to mimic a browser
        response = requests.get(url, headers=headers, timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Failed to fetch the website, status code: {response.status_code}")
    except requests.exceptions.Timeout:
        raise Exception("Request timed out.")
    except Exception as e:
        raise Exception(f"Error: {e}")

def generate_tags_from_html(html_content):
    """Generate tags based on HTML content using ChatGPT API"""
    prompt = f"""
    The following is the HTML source of a website. Please analyze the HTML, extract the Google Tag Manager (GTM) container code, and generate custom tags from it. If GTM code is found, list the tags it is associated with.
    HTML Source:
    {html_content}
    """
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    #url = input("Enter You URL")
    # Step 1: Fetch the HTML content of the website
    try:
        html_content = fetch_website_source('https://www.eiu.com/n/campaigns/global-liveability-index-2024')
        print("Website source code fetched successfully!")
        # Step 2: Generate tags using ChatGPT API
        generated_tags = generate_tags_from_html(html_content)
        print("\nGenerated Tags from the HTML content:\n")
        print(generated_tags)
    except Exception as e:
        print(f"Error: {e}")https://platform.openai.com/docs/guides/error-codes/api-errors
if __name__ == "__main__":
    main()
