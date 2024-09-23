from django.apps import AppConfig
from .utils import download_pickle_from_s3

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    # Global variables to hold the DataFrames
    FEATURE_IMPORTANCE_DF = None
    CLEANED_DATA_DF = None

    def ready(self):
        """
        This method is called when the application is starting. Here, we will
        load the pickle files into memory so that they can be reused across views.
        """
        # Use the global variables defined within the class
        global FEATURE_IMPORTANCE_DF, CLEANED_DATA_DF
        
        # Load the pickle files into memory
        try:
            FEATURE_IMPORTANCE_DF = download_pickle_from_s3('feature_importances.pkl')
            CLEANED_DATA_DF = download_pickle_from_s3('cleaned_data.pkl')
            print("Pickle files loaded successfully during startup")
        except Exception as e:
            # Handle exceptions if downloading fails, such as logging the error
            print(f"Error loading pickle files during startup: {e}")
