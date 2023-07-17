import requests
import json
from.models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth


# Create a `get_request` to make HTTP GET requests
def get_request(url, api_key=False, **kwargs):
    if api_key:
        try:
            res = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs, auth=HTTPBasicAuth('apikey', api_key))
        except:
            return{
                "code": 500,
                "message": "Something went wrong on the server",
                "error": str(e)
            }
    else:
        # No authentication GET
        try:
            res = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
        except:
            return{
                "code": 500,
                "message": "Something went wrong on the server",
                "error": str(e)
            }
    # Retrieving the response status code and content
    status_code = res.status_code
    json_data = json.loads(res.text)

    return json_data


# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
def get_dealers_from_cf(url):
    res = []
    json_res = get_request(url)
    dealers = json_res["dealershipsList"]
    for dealer in dealers:
        dealer_obj = CarDealer(address=dealer["address"], city=dealer["city"], full_name=dealer["full_name"],
                               id=dealer["id"], lat=dealer["lat"], long=dealer["long"],
                               short_name=dealer["short_name"],
                               st=dealer["st"], state=dealer["state"], zip=dealer["zip"])
        res.append(dealer_obj)
    return res

# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
def get_dealer_reviews_from_cf (url, dealer_id):
    res = []
    json_res = get_request(url, dealer_id=dealer_id)
    if json_res:
        reviews = json_res["reviews"]
        for review in reviews:
            if isinstance(review, str):
                review_content = json.loads(review)
            else:
                review_content = review
            id = review["_id"]
            review_info = review_content.get("review")
            if review_info and "name" and "purchase" and "dealership" and "car_make" and "car_model" and "car_year" and "purchase_date" in review_info:
                name = review_info["name"]
                purchase = review_info["purchase"]
                dealership = review_info["dealership"]
                car_make = review_info["car_make"]
                car_model = review_info["car_model"]
                car_year = review_info["car_year"]
                purchase_date = review_info["purchase_date"]
                review_obj = DealerReview(
                    car_make=car_make, 
                    car_model=car_model, 
                    car_year=car_year,
                    dealership=dealership, 
                    id=id, 
                    name=name, 
                    purchase=purchase, 
                    purchase_date=purchase_date,
                    review=review_content
                )
            res.append(review_obj)
    return res

# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



