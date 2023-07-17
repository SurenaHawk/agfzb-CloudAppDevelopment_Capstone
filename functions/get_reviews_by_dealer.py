import sys
from ibmcloudant.cloudant_v1 import CloudantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_cloud_sdk_core import ApiException


def main(dict):
    COUCH_URL = "https://7ba488ca-c0e9-4f83-9c01-09dffdd47f94-bluemix.cloudantnosqldb.appdomain.cloud"
    IAM_API_KEY = "syHHOFlKoEbur35iLvyzCR4WmCFtnkZZMsW1kdbPebG9"
    COUCH_USERNAME = "7ba488ca-c0e9-4f83-9c01-09dffdd47f94-bluemix"
    try:
        authenticator = IAMAuthenticator(apikey=IAM_API_KEY)
        client = CloudantV1(authenticator=authenticator)
        client.set_service_url(COUCH_URL)
        dealership_id = dict.get("dealership")
        reviews = client.post_all_docs(db="reviews", include_docs=True).get_result()
        res = []
        for row in reviews["rows"]:
            doc = row["doc"]
            if "dealership" in doc and doc["dealership"] == dealership_id:
                res.append(doc)
        return{
            "reviews": res
        }
    except Exception as e:
        return{
            "code": 500,
            "message": "Something went wrong on the server",
            "error": str(e)
        }