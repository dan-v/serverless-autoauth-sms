A [serverless](https://serverless.com/) powered API endpoint that automates two factor SMS authentication responses using [Twilio](https://www.twilio.com). Please note that this is generally a pretty bad idea, as it removes two factor authentication completely. Right now the app is hardcoded to just parse out the first 6 characters received in an SMS and respond back with that.

## Requirements
* Serverless framework

  ```sh
  npm install serverless -g
  ```
* AWS account with [access key setup](https://serverless.com/framework/docs/providers/aws/guide/credentials/) for deploying serverless stack
* Twilio account with phone number and TwiML App setup for messaging

## Setup
1. Deploy serverless stack

  ```sh
  export AWS_ACCESS_KEY_ID=<your-key-here>
  export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>
  serverless deploy -v
  ```
2. Copy API endpoint URL (e.g. https://xxxxxxx.execute-api.us-west-2.amazonaws.com/dev/auth) and add it to your TwiML app as the request URL.
3. Test out by sending a text to your Twilio number and you should get a response back.
