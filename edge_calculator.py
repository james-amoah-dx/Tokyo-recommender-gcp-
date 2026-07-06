"""
EDGE Zero Carbon ROI Calculator
Input: Building area, location, type
Output: Annual CO2 saved, energy saved, payback years
Standards: IFC EDGE v3.0
"""
import pandas as pd

def calculate_edge_savings(area_sqm, building_type="office", location="Tokyo"):
    # Simplified EDGE benchmarks - Tokyo office baseline
    baseline_energy_kwh = area_sqm * 200  # kWh/m2/year Japan average
    
    # EDGE 20% minimum measures
    edge_savings_pct = 0.25  # 25% typical with low-cost measures
    energy_saved_kwh = baseline_energy_kwh * edge_savings_pct
    
    # Japan grid: 0.4 kg CO2/kWh
    co2_saved_tons = energy_saved_kwh * 0.4 / 1000
    
    # Japan electricity: ¥27/kWh commercial
    cost_saved_jpy = energy_saved_kwh * 27
    
    # Typical EDGE retrofit: ¥15,000/sqm
    retrofit_cost_jpy = area_sqm * 15000
    payback_years = retrofit_cost_jpy / cost_saved_jpy
    
    return {
        "area_sqm": area_sqm,
        "co2_saved_tons_yr": round(co2_saved_tons, 1),
        "energy_saved_kwh_yr": int(energy_saved_kwh),
        "cost_saved_jpy_yr": int(cost_saved_jpy),
        "payback_years": round(payback_years, 1)
    }

# Example: Takenaka 10,000 sqm office
if __name__ == "__main__":
    result = calculate_edge_savings(area_sqm=10000)
    print(f"Takenaka 10k sqm office retrofit:")
    print(f"CO2 Saved: {result['co2_saved_tons_yr']} tons/year")
    print(f"Cost Saved: ¥{result['cost_saved_jpy_yr']:,}/year") 
    print(f"Payback: {result['payback_years']} years")
