# test_app.py

def test_app_import():
    """
    A simple smoke test to ensure the app can be imported without syntax errors.
    """
    try:
        from app import st
        # We check if 'st' is the streamlit module, confirming a successful import
        assert "streamlit" in str(type(st))
    except ImportError as e:
        assert False, f"Failed to import the Streamlit app: {e}"