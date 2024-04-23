# This blueprint
This blueprint creates a REST API project. The project uses AWS Lambda and Amazon API Gateway with a To Do service reference and deploys it into a chosen AWS account. 

# Architecture overview

The project deploys a RESTful API application that uses the following AWS Serverless technologies:

* AWS API Gateway (https://aws.amazon.com/api-gateway) to provide the REST interface to the user.
* Amazon DynamoDB (https://aws.amazon.com/dynamodb) as a data store
* AWS Lambda (https://aws.amazon.com/lambda) process the API gateway requests and read data from or write data to a DynamoDB table. 

Both the AWS Cloud Development Kit (CDK) application and AWS Lambda code are written in three languages. You can choose from the following programming languages:

* Python 3.8
* Java 11
* Node.js 16 (Typescript)

The build pipeline runs unit and integration tests on the application and produces testing reports. Failed tests will stop the artifacts from publishing.

![Architecture Diagram](https://deyn4asqcu6xj.cloudfront.net/serverless-todo-backend-arch.png) 

## Connections and permissions

The `"To Do" service` supports the Amazon CodeCatalyst Development Role, which can be created from the [AWS management console Codecatalyst application](https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/). When clicking “add IAM role”, the first option is to create a CodeCatalyst development role. After clicking create, the role will be automatically added to the Amazon CodeCatalyst space. 

The other option is creating a application specific IAM role, which can be added to the Amazon CodeCatalyst space by selecting "Add an existing IAM role" from the add IAM role options. The IAM role needs to contain the CodeCatalyst trust policy, as well as the following permissions:

## IAM Role

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudformation:*",
                "ssm:*",
                "s3:*",
                "iam:PassRole",
                "iam:GetRole",
                "iam:CreateRole",
                "iam:AttachRolePolicy",
                "iam:PutRolePolicy"
            ],
            "Resource": "*"
        }
    ]
}
```

The IAM roles also require the following CodeCatalyst service principals:
*  codecatalyst.amazonaws.com
*  codecatalyst-runner.amazonaws.com

## Trust policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "codecatalyst.amazonaws.com",
                    "codecatalyst-runner.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

# Project resources

This blueprint creates the following Amazon CodeCatalyst resources:

* Source repository named todo-app
* A workflow defined in .codecatalyst/workflows/main_fullstack_workflow.yaml
* Initial deployment of the architecture stacks to the linked AWS account.

After being created successfully, this project deploys the following AWS resource: 

* Amazon DynamoDB table based on input name
* Amazon Lambda functions to handle back end transactions
* Amazon API Gateway REST API with chosen name

View the deployment status in the project's workflow.

## Installation 

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

If you would like to deploy the CDK application as a standalone deployment not part of the blueprint, set an envrironment variable as follows:
`export LOCAL_TESTING="True"`

## Running tests

* In order to run unit tests, run `pytest --junitxml=test_unit_results.xml --cov-report xml:test_unit_coverage.xml --cov=. tests/unit`
* In order to run integration tests, run `pytest --junitxml=test_integ_results.xml --cov-report xml:test_integ_coverage.xml --cov=. tests/integ`

Note that both report files are not checked in to the repo.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

## Additional resources

See the Amazon CodeCatalyst user guide for additional information on using the features and resources of Amazon CodeCatalyst