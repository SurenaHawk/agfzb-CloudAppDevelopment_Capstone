const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');

async function main(params) {
    secret = {
        "COUCH_URL": "https://7ba488ca-c0e9-4f83-9c01-09dffdd47f94-bluemix.cloudantnosqldb.appdomain.cloud",
        "IAM_API_KEY": "syHHOFlKoEbur35iLvyzCR4WmCFtnkZZMsW1kdbPebG9",
        "COUCH_USERNAME": "7ba488ca-c0e9-4f83-9c01-09dffdd47f94-bluemix"
    }
     
    const authenticator = new IamAuthenticator({
        apikey: secret.IAM_API_KEY
    });

    const cloudant = new CloudantV1({
        authenticator: authenticator,
        serviceUrl: secret.COUCH_URL
    });
    
    try {
        const response = await cloudant.postAllDocs({
            db: 'dealerships',
            includeDocs: true
        });
        const dealershipsList = response.result.rows.map(row => row.doc);
        return { dealershipsList };
    } catch (error) {
        return { error: error.message };
    }
}