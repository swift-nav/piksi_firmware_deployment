#!/bin/bash

# Piksi Firmware Deployment Script
#
# When this file runs we will have the artifacts from the piksi_firmware build
# under a directory `artifacts/`

# Move VERSION file - we don't want to upload it and the Jenkins job config
# expects it in the root
mv artifacts/VERSION ./

# Upload artifacts to S3 downloads bucket
for f in artifacts/*; do
  aws --region "$S3_REGION" s3 cp "$f" "$S3_BUCKET"/"$S3_FW_PATH"
done

# Download the current index.json
aws --region "$S3_REGION" s3 cp "$S3_BUCKET"/index.json ./

python update_index_json.py

# Upload new index.json to S3 downloads bucket
aws --region "$S3_REGION" s3 cp index_new.json "$S3_BUCKET"/index.json

