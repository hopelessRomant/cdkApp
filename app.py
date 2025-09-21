#!/usr/bin/env python3
import os

import aws_cdk as cdk

from cdk_app.cdk_app_stack import HelloCdkStack


app = cdk.App()
HelloCdkStack(app, "HelloCdkStack",
        env = cdk.Environment(
            account=os.getenv("ACCOUNTID"), 
            region=os.getenv("REGION")
        )
)

app.synth()
