from constructs import Construct

from aws_cdk import (
	Stack, 
	aws_lambda as _lambda, 
	aws_apigateway as apigw,
)

from cdk_workshop.hitcounter import HitCounter

from cdk_dynamo_table_view import TableViewer 

class CdkWorkshopStack(Stack):
	def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
		super().__init__(scope, construct_id, **kwargs)
		# define an AWS lambda resource
		my_lambda = _lambda.Function(
			self, "hello_handler", 
			runtime = _lambda.Runtime.PYTHON_3_8, 
			code = _lambda.Code.from_asset('lambda'), 
			handler = 'hello.handler',
		)
		
		hello_with_counter = HitCounter(
            self, 'HelloHitCounter',
            downstream=my_lambda,
        )

		apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=hello_with_counter.handler,
        )
		table_viewer = TableViewer(self, "viewHitCounter",
            title = "Hello hits", 
            table = hello_with_counter.table, 
			sort_by = "-hits", 
	) 
