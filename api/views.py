from django.shortcuts import render
from .utils import download_pickle_from_s3

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(['GET'])
def feature_importances(request):
    try:
        # Download the feature importance pickle file from S3
        feature_importance_df = download_pickle_from_s3('feature_importances.pkl')
        
        # Convert the DataFrame to a dictionary and return it as JSON
        top_features = feature_importance_df.head(10)
        response_data = top_features.to_dict(orient='records')
        
        return Response(response_data)
    
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['GET'])
def ad_spend_vs_clicks(request):
    try:
        # Load the DataFrame (you can load it from a CSV, database, or any other source)
        df = download_pickle_from_s3('cleaned_data.pkl')  # Replace with actual data source

        # Return 'spent' and 'clicks' columns as JSON
        data = df[['spent', 'clicks']].to_dict(orient='list')

        return Response(data)
    
    except Exception as e:
        return Response({'error': str(e)}, status=500)