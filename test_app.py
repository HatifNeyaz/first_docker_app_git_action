# test_app.py

def test_app_import():
    """
    A simple smoke test to ensure the app can be imported without errors.
    """
    try:
        from app import st
        # A better way to check if 'st' is the streamlit module
        assert st.__name__ == "streamlit"
    except ImportError as e:
        assert False, f"Failed to import the Streamlit app: {e}"