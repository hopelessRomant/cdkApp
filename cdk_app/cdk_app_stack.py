from aws_cdk import (
  Stack,
  aws_lambda as _lambda,
  CfnOutput 
)
from constructs import Construct

class HelloCdkStack(Stack):

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    my_function = _lambda.Function(
      self, "HelloWorldFunction",
      runtime = _lambda.Runtime.NODEJS_20_X, 
      handler = "index.handler",
      code = _lambda.Code.from_inline(
        """
        exports.handler = async function(event) {
          return {
            statusCode: 200,
            body: JSON.stringify('Hello World!'),
          };
        };
        """
      ),
    )
    my_function_url = my_function.add_function_url(
      auth_type = _lambda.FunctionUrlAuthType.NONE,
    )
    CfnOutput(self, "MyFunctionUrlOutput", value = my_function_url.url)