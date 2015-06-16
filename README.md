Deploy the `piksi_firmware` or `nap` build
==========================================

Performs the following steps:

 * Upload all artifacts to the S3 downloads bucket
 * Update the `index.json` file to point to the new firmware version
 * Upload the new `index.json` file back to the S3 bucket

Usage
-----

Call `./deploy.sh STM` or `./deploy.sh NAP` from CI server.

Pre-requisites
--------------

Uses python.

Expects the environment variable `S3_BUCKET` to be set to an S3 url, e.g.

```
s3://downloads.testing.swiftnav.com
```

Expects the files to be uploaded are in a directory called `artifacts/` and
there is exactly one `.hex` file present (to which `index.json` will be
pointed).

The file `VERSION` or `HDL_VERSION` in the `artifacts/` directory will be moved
to the root and will not be uploaded.


