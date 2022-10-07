payload3=b"""{
"latitude": 39.5732160891,
"longitude": -119.672918997,
"radius": 100
}"""

client = boto3.client('lambda')
for x in range (0, 5):
    response = client.invoke(
        FunctionName="loadSpotsAroundPoint",
        InvocationType='Event',
        Payload=payload3
    )
    time.sleep(15)
    print(json.loads(response['Payload'].read()))
    print("\n")
