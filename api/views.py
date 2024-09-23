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

# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.apps import apps

# # Access ApiConfig to retrieve the cached dataframes
# @api_view(['GET'])
# def feature_importances(request):
#     try:
#         # Get the cached DataFrame from ApiConfig
#         feature_importance_df = apps.get_app_config('api').FEATURE_IMPORTANCE_DF
        
#         if feature_importance_df is None:
#             return Response({"error": "Data not loaded yet"}, status=500)
        
#         # Extract the top 10 features
#         top_features = feature_importance_df.head(10)
#         response_data = top_features.to_dict(orient='records')

#         return Response(response_data)
    
#     except Exception as e:
#         return Response({'error': str(e)}, status=500)


# @api_view(['GET'])
# def ad_spend_vs_clicks(request):
#     try:
#         # Get the cached DataFrame from ApiConfig
#         cleaned_data_df = apps.get_app_config('api').CLEANED_DATA_DF
        
#         if cleaned_data_df is None:
#             return Response({"error": "Data not loaded yet"}, status=500)

#         # Extract 'spent' and 'clicks' columns
#         data = cleaned_data_df[['spent', 'clicks']].to_dict(orient='list')

#         return Response(data)
    
#     except Exception as e:
#         return Response({'error': str(e)}, status=500)
