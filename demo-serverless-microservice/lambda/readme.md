# Introduction

This folder is for running the workshop in your own account. If you are running the workshop in an AWS hosted event, the function and data file will be provisioned in your account.

# IMPORTANT

Remove the created resources after the workshop to avoid charges

## Uploading the data file

Upload the data `clickstream_data.csv` from the data folder into an S3 bucket.

## Configuring the Lambda function

Create a Lambda function in the `us-west-2` region with the following configuration:

* Function name: `data-analysis-function`.
* Runtime: Python 3.11
* Permissions:
  * Choose **Create a new role from AWS policy templates**.
  * For **Role name**, enter `dataAnalysisRole`.
  * For **Policy templates**, select AMAZON S3 Read Only permissions
* Select **Create function**.

After the function has been created:

* Copy the code from the file `index.py` in the folder `data-analysis-function` into the **Code source** pane.
* Under the Configuration tab, select **Environmental variables**.
* Add a new environmental variable `S3_BUCKET`, providing the S3 bucket name (e.g. `myS3Bucket`) where you loaded up your data file.
* Add a new environmental variable `S3_OBJECT`, and leave the value empty.

## Next steps

You are now ready to the **Debugging Lambda** lab.

## Cleanup

Delete the Lambda function `data-analysis-function`.
Delete the IAM role `dataAnalysisRole`.
Delete the `clickstream_data.csv` file.
Delete the log group `data-analysis-function`.
