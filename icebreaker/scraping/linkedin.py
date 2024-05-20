import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """Scrape LinkedIn profile data from a LinkedIn profile URL.

    Args:
        linkedin_profile_url (str): LinkedIn profile URL.
        mock (bool): If True, return mock data.

    Returns:
        dict: LinkedIn profile data.
    """

    if mock:
        linkedin_profile_url = os.environ["MOCK_LINKEDIN_PROFILE_URL"]
        data = requests.get(linkedin_profile_url).json()

    else:
        api_key = os.environ["PROXYCURL_API_KEY"]
        headers = {"Authorization": "Bearer " + api_key}
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        params = {
            "linkedin_profile_url": linkedin_profile_url,
        }
        response = requests.get(api_endpoint, params=params, headers=headers)
        data = response.json()

    data = {
        k: v
        for k, v in data.items()
        if v not in (None, "", [], {})
        and k
        not in (
            "background_cover_image_url",
            "certifications",
            "people_also_viewed",
        )
    }
    return data


if __name__ == "__main__":
    profile = scrape_linkedin_profile(
        linkedin_profile_url="https://linkedin.com/in/timo-van-niedek/", mock=True
    )
    print(profile["full_name"])
