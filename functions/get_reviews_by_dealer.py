import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException
import requests
import json

def main(dict):
    COUCH_URL = "https://7ba488ca-c0e9-4f83-9c01-09dffdd47f94-bluemix.cloudantnosqldb.appdomain.cloud"
    IAM_API_KEY = "syHHOFlKoEbur35iLvyzCR4WmCFtnkZZMsW1kdbPebG9"
    COUCH_USERNAME = "7ba488ca-c0e9-4f83-9c01-09dffdd47f94-bluemix"
    try:
        authenticator = IAMAuthenticator(apikey=IAM_API_KEY)
        client = CloudantV1(authenticator=authenticator)
        client.set_service_url(COUCH_URL)
        review_database = client.post_all_docs(db="reviews").get_result()
        reviews_list = reviews["rows"]
        dealership_id = params.get("dealership_id")
        res = []
        for review in reviews_list:
            if review["doc"]["dealership_id"] == dealership_id:
                res.append(reivew)
        return {
            "reviews": res
        }
    except Exception as ex:
        return {"error": str(ex)}