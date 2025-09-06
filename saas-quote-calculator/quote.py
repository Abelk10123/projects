#!/usr/bin/env python3
import argparse

TIERS = [(50, 0.15), (25, 0.10), (10, 0.05)]  # (min_seats and discount_rate)

def best_discount(seats: int) -> float:
    for threshold, rate in TIERS:
        if seats >= threshold:
            return rate
    return 0.0

def main():
    p = argparse.ArgumentParser(description="SaaS Quote Calculator")
    p.add_argument("--seats", type=int, required=True, help="number of seats/users (>0)")
    p.add_argument("--price", type=float, required=True, help="list price per seat per month (>=0)")
    args = p.parse_args()

    if args.seats <= 0 or args.price < 0:
        raise SystemExit("Error: seats must be > 0 and price must be >= 0")

    rate = best_discount(args.seats)
    subtotal_m = args.seats * args.price
    discount_m = subtotal_m * rate
    total_m = subtotal_m - discount_m
    total_y = total_m * 12
    eff_pps = total_m / args.seats

    print(f"Seats: {args.seats}")
    print(f"List £/seat/month: £{args.price:.2f}")
    print(f"Discount applied: {rate*100:.0f}%")
    print(f"Subtotal (monthly): £{subtotal_m:.2f}")
    print(f"Discount (monthly): -£{discount_m:.2f}")
    print(f"Total (monthly): £{total_m:.2f}")
    print(f"Total (annual): £{total_y:.2f}")
    print(f"Effective £/seat/month: £{eff_pps:.2f}")

if __name__ == "__main__":
    main()
