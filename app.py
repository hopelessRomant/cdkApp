#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_app.cdk_app_stack import CdkAppStack


app = cdk.App()
CdkAppStack(app, "CdkAppStack",
        env = cdk.Environment(
            account=os.getenv("ACCOUNTID"), 
            region=os.getenv("REGION")
        )
)

app.synth()
