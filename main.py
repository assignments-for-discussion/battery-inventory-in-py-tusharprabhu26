def count_batteries_by_health(present_capacities):
    # Initialize counts
    counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }
    
    rated_capacity=120
    
    # Iterate over present capacities
    for present_capacity in present_capacities:
        # Compute SoH
        SoH = 100 * present_capacity / rated_capacity

        # Classify batteries
        if SoH >= 80:  # batteries "healthy"
            counts["healthy"] += 1
        elif 80 > SoH >= 62:  # Batteries "exchange"
            counts["exchange"] += 1
        else: # batteriess "failed"
            counts["failed"] += 1

    return counts


def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")

    # normal test
    present_capacities = [113, 116, 80, 95, 92, 70]
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 2)
    assert(counts["exchange"] == 3)
    assert(counts["failed"] == 1)

    # test for all batteries healthy
    present_capacities = [120, 120, 120, 120, 120]
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 5)
    assert(counts["exchange"] == 0)
    assert(counts["failed"] == 0)

    # test for all batteries failed
    present_capacities = [50, 50, 50, 50, 50]
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 0)
    assert(counts["exchange"] == 0)
    assert(counts["failed"] == 5)

    # test for SoH exactly at boundary values
    present_capacities = [96, 74.4, 74.4, 74.4, 74.4]  # SoH values: 80%, 62%, 62%, 62%, 62%
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 1)
    assert(counts["exchange"] == 4)
    assert(counts["failed"] == 0)

    # Test for SoH exactly 100
    present_capacities = [120]  # SoH value: 100%
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 1)
    assert(counts["exchange"] == 0)
    assert(counts["failed"] == 0)

    # Test for SoH exactly 0
    present_capacities = [0]  # SoH value: 0%
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 0)
    assert(counts["exchange"] == 0)
    assert(counts["failed"] == 1)

    # Test for SoH just above 80
    present_capacities = [96.01]  # SoH value: just above 80%
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 1)
    assert(counts["exchange"] == 0)
    assert(counts["failed"] == 0)

    # Test for SoH just below 80
    present_capacities = [95.99]  # SoH value: just below 80%
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 0)
    assert(counts["exchange"] == 1)
    assert(counts["failed"] == 0)

    # Test for SoH just above 62
    present_capacities = [74.41]  # SoH value: just above 62%
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 0)
    assert(counts["exchange"] == 1)
    assert(counts["failed"] == 0)

    # Test for SoH just below 62
    present_capacities = [74.39]  # SoH value: just below 62%
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 0)
    assert(counts["exchange"] == 0)
    assert(counts["failed"] == 1)

    print("Done counting :)")


if __name__ == '__main__':
    test_bucketing_by_health()
