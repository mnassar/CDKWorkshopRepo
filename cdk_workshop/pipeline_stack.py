from constructs import Construct
from aws_cdk import (
    Stack,
    pipelines as pipelines,
)


class WorkshopPipelineStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Pipeline code will go here

        # Creates a CodeCommit repository called 'WorkshopRepo'
        # repo = codecommit.Repository(
        #     self, 'CDKWorkshopRepo',
        #     repository_name= "CDKWorkshopRepo"
        # )
        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.git_hub("mnassar/CDKWorkshopRepo", "main"),
                commands=[
                    "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                    "pip install -r requirements.txt",  # Instructs Codebuild to install required packages
                    "cdk synth",
                ]
            ),
        )
        

 

