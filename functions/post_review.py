import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException

def main(dict):
    COUCH_URL = "https://7ba488ca-c0e9-4f83-9c01-09dffdd47f94-bluemix.cloudantnosqldb.appdomain.cloud"
    IAM_API_KEY = "syHHOFlKoEbur35iLvyzCR4WmCFtnkZZMsW1kdbPebG9"
    COUCH_USERNAME = "7ba488ca-c0e9-4f83-9c01-09dffdd47f94-bluemix"
    review = {
            "id": 1114,
            "name": "Upkar Lidder",
            "dealership": 15,
            "review": "Great service!",
            "purchase": False,
            "another": "field",
            "purchase_date": "02/16/2021",
            "car_make": "Audi",
            "car_model": "Car",
            "car_year": 2021
    }
    try:
        authenticator = IAMAuthenticator(apikey=IAM_API_KEY)
        client = CloudantV1(authenticator=authenticator)
        client.set_service_url(COUCH_URL)
        new_review = client.post_document(db="reviews", document=review)
        res = new_review.get_result()
        result = {
            "headers": {"Content-Type": "application/json"},
            "body": {"message": "Review posted"}
        }
        return {
            "review": result
        }
    except Exception as e:
        return {
            "code": 500,
            "message": "Something went wrong on the server",
            "error": str(e)
        }        
