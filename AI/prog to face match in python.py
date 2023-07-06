# OpenAI response for prompt: write a program to face match in python 
# ******************************** 


import boto3

if __name__ == "__main__":

    # Setting up the Rekognition client 
    rekognition = boto3.client('rekognition', region_name='us-west-1')

    # Setting up file paths to local images
    # source_image = f"photo/new.png"
    # target_image = f"photo/design.png"

    #read source and target image
    with open(f"photo/new.png", "rb") as source_image:
        source_bytes = source_image.read()

    with open(f"photo/design.png", "rb") as target_image:
        target_bytes = target_image.read()

    # Call API to compare the two faces
    response = rekognition.compare_faces(
        SourceImage={'Bytes': source_bytes},
        TargetImage={'Bytes': target_bytes},
    )

    # Print the response 
    print(response)