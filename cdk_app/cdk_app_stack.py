from aws_cdk import (
  Stack,
  aws_lambda as _lambda,
)
from constructs import Construct

class HelloCdkStack(Stack):

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)

    my_function = _lambda.Function(
      self, "MyFirstFunction",
      runtime= _lambda.Runtime.NODEJS_20_X,
      handler="index.handler",
      code= _lambda.Code.from_inline(
        """
        exports.handler = async function(event) {
          return {
            statusCode: 200,
            body: JSON.stringify('Hello World'),
          };
        };
        """
      ),

    )