from analyser import build_report, read_temperatures, write_report


def make_csv(tmp_path, content):
    path = tmp_path / "log.csv"
    path.write_text(content)
    return path


def test_reads_valid_rows(tmp_path):
    path = make_csv(tmp_path, "timestamp,sensor_id,temperature_c\nt1,S1,20\nt2,S1,30\n")
    temps, skipped = read_temperatures(path)
    assert temps == [20.0, 30.0]
    assert skipped == 0


def test_skips_bad_rows(tmp_path):
    path = make_csv(tmp_path, "timestamp,sensor_id,temperature_c\nt1,S1,20\nt2,S1,oops\nt3,S1,\n")
    temps, skipped = read_temperatures(path)
    assert temps == [20.0]
    assert skipped == 2


def test_skips_impossible_values(tmp_path):
    path = make_csv(tmp_path, "timestamp,sensor_id,temperature_c\nt1,S1,20\nt2,S1,999\n")
    temps, skipped = read_temperatures(path)
    assert temps == [20.0]
    assert skipped == 1


def test_report_contains_statistics():
    report = build_report([20.0, 30.0], skipped=1)
    assert "Average: 25.00" in report
    assert "Skipped rows:   1" in report


def test_report_with_no_data():
    assert "No valid readings" in build_report([], skipped=3)


def test_write_report_creates_file(tmp_path):
    out = tmp_path / "report.txt"
    write_report("hello", out)
    assert out.read_text() == "hello"

def test_count_above_threshold():
    from analyser import count_above

    assert count_above([20.0, 31.0, 35.0], 30.0) == 2


def test_average_by_sensor(tmp_path):
    from analyser import average_by_sensor

    path = make_csv(
        tmp_path,
        "timestamp,sensor_id,temperature_c\nt1,S1,20\nt2,S1,30\nt3,S2,40\nt4,S2,bad\n",
    )
    assert average_by_sensor(path) == {"S1": 25.0, "S2": 40.0}