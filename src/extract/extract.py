from __future__ import annotations

import argparse
import logging
from pathlib import Path
import pandas as pd

LOG = logging.getLogger("etl.extract")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")


def extract(csv_path: Path) -> pd.DataFrame:
  
    if not csv_path.exists():
        raise FileNotFoundError(f"Input CSV not found: {csv_path}")

    # Load with minimal parsing; full cleaning happens in transform step
    
    df = pd.read_csv(csv_path)
    LOG.info("Loaded %s (rows=%s, cols=%s)", csv_path, len(df), df.shape[1])

    # Parse basic datetime columns (safe; leaves others as-is)
    
    for col in ("departure_time", "arrival_time", "scan_date"):
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], dayfirst=True, errors="coerce")

    return df


def _cli():
    p = argparse.ArgumentParser(description="Extract flights data from CSV")
    p.add_argument("--input", type=Path, default=Path("data/raw/Global_flights_data.csv"))
    p.add_argument("--out-parquet", type=Path, default=None, help="Optional interim parquet output")
    args = p.parse_args()

    df = extract(args.input)

    if args.out_parquet:
        args.out_parquet.parent.mkdir(parents=True, exist_ok=True)
        df.to_parquet(args.out_parquet, index=False)
        LOG.info("Wrote interim parquet: %s", args.out_parquet)
    else:
        # quick peek when running by hand
        print(df.head(10).to_string(index=False))


if __name__ == "__main__":
    _cli()
