import sys
import logging
import datetime
from ai_models.model import load_model

# Configure logging to see what's happening
logging.basicConfig(level=logging.INFO)

def test_opendata_availability():
    # Calculate a recent date (yesterday)
    # Current simulated date is 2025-12-01, so yesterday is 2025-11-30
    today = datetime.datetime(2025, 12, 1)
    target_date = today - datetime.timedelta(days=1)
    
    date_int = int(target_date.strftime("%Y%m%d"))
    time_int = 0 # 00 UTC
    
    print(f"--- Micro-Test: ECMWF Open Data Availability ---")
    print(f"Target Date: {date_int}")
    print(f"Target Time: {time_int:04d}")
    print(f"Model: fourcastnetv2-small")
    print(f"Source: ecmwf-open-data")
    print("-" * 40)

    try:
        # Initialize the model with Open Data input
        # We set lead_time=0 because we only want to check input availability
        model = load_model(
            "fourcastnetv2-small",
            input="ecmwf-open-data",
            date=date_int,
            time=time_int,
            lead_time=0, 
            assets_sub_directory=False,
            download_assets=False, # Assumed already downloaded
            model_version='small',
            output='none',
            model_args={},
            assets='.'
        )
        
        print("\n[1/3] Model initialized.")
        
        # Trigger fetching of Surface fields
        print("[2/3] Checking Surface fields (SFC)...")
        sfc = model.input.fields_sfc
        print(f"   -> Found {len(sfc)} surface fields.")
        
        # Trigger fetching of Pressure Level fields
        print("[3/3] Checking Pressure Level fields (PL)...")
        pl = model.input.fields_pl
        print(f"   -> Found {len(pl)} pressure level fields.")
        
        print("\nSUCCESS: All required input fields are available in Open Data.")
        
    except Exception as e:
        print(f"\nFAILURE: Could not retrieve inputs.")
        print(f"Error details: {e}")
        sys.exit(1)

if __name__ == "__main__":
    test_opendata_availability()
